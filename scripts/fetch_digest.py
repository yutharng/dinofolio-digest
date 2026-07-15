# -*- coding: utf-8 -*-
"""
Dino Digest Fetcher — ดึง digest จาก Supabase ของ dinofolio.com แล้วบันทึกเป็น Markdown
รันโดย GitHub Actions ทุกเช้า 06:00 เวลาไทย (ดู .github/workflows/daily-digest.yml)

Logic: ดึง "ทุกวัน" ที่มีใน DB (rolling window ~15 วัน) แล้วเขียนเฉพาะวันที่ยังไม่มีไฟล์
→ ถ้าวันไหน workflow ล่ม วันถัดไปจะเก็บย้อนหลังให้เอง (self-healing ภายใน 15 วัน)
"""
import json
import os
import urllib.request

SUPABASE = "https://ykeklatvusxwftaepcgs.supabase.co/rest/v1/daily_digests"
# anon key (public — ฝังอยู่ใน JS ของเว็บ dinofolio อยู่แล้ว)
KEY = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
       "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlrZWtsYXR2dXN4d2Z0YWVwY2dzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUzMjY5NzEsImV4cCI6MjA2MDkwMjk3MX0."
       "Y_HYeTf1mDfYoxzCG6EtQYR5Vd4J3MsrDoZjNZqARa4")

TH_MONTHS = ["", "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.",
             "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]


def api(query: str):
    req = urllib.request.Request(
        SUPABASE + query,
        headers={"apikey": KEY, "Authorization": "Bearer " + KEY},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def thai_date(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{int(d)} {TH_MONTHS[int(m)]} {int(y) + 543}"


def parse_articles(html: str):
    """แปลง html_content → [{title, summary, sources}] โดยแบ่งตาม <h3>"""
    if not html:
        return []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for h in soup.find_all("h3"):
        title = h.get_text(strip=True)
        parts, sources = [], []
        el = h.find_next_sibling()
        while el is not None and el.name != "h3":
            if el.name in ("p", "ul"):
                txt = el.get_text("\n", strip=True)
                if txt:
                    parts.append(txt)
            if hasattr(el, "find_all"):
                for a in el.find_all("a"):
                    u = a.get("href") or ""
                    if u.startswith("http"):
                        sources.append(u.split("?")[0])  # ตัด query string/tracking
            el = el.find_next_sibling()
        seen = []
        for s in sources:
            if s not in seen:
                seen.append(s)
        out.append({"title": title, "summary": "\n".join(parts), "sources": seen})
    return out


def fmt_movers(raw: str) -> str:
    if not raw:
        return ""
    try:
        j = json.loads(raw)
        g = ", ".join(f"{x['ticker']} +{x['change_percentage']}" for x in j.get("top_gainers", []))
        l = ", ".join(f"{x['ticker']} {x['change_percentage']}" for x in j.get("top_losers", []))
        if not (g or l):
            return ""
        return f"## 📈 Market Movers\n**Gainers:** {g}\n**Losers:** {l}\n"
    except (ValueError, KeyError):
        return ""


def fmt_earnings(raw: str) -> str:
    if not raw:
        return ""
    try:
        j = json.loads(raw)
        if not j:
            return ""
        rows = "\n".join(
            f"| {x.get('symbol','')} | {x.get('name','')} | {x.get('estimate','')} | {x.get('timeOfDay','') or '–'} |"
            for x in j
        )
        return ("## 📅 Earnings Alerts\n"
                "| Ticker | บริษัท | Est. EPS | เวลา |\n|---|---|---|---|\n" + rows + "\n")
    except (ValueError, KeyError):
        return ""


def render(row: dict) -> str:
    date = row["published_date"]
    md = [f"# 🦕 Dino Digest — {thai_date(date)} ({date})\n"]
    mv = fmt_movers(row.get("market_movers"))
    if mv:
        md.append(mv)
    ea = fmt_earnings(row.get("earnings_alerts"))
    if ea:
        md.append(ea)
    articles = parse_articles(row.get("html_content")) + parse_articles(row.get("html_2nd_contents"))
    md.append(f"## 📰 ข่าววันนี้ ({len(articles)} ชิ้น)\n")
    for a in articles:
        md.append(f"### {a['title']}")
        if a["summary"]:
            md.append(a["summary"])
        for s in a["sources"]:
            md.append(f"🔗 source: {s}")
        md.append("")
    return "\n".join(md).strip() + "\n"


def main():
    rows = api("?select=*&order=published_date.asc")
    os.makedirs("daily", exist_ok=True)
    new = 0
    for row in rows:
        path = f"daily/dino-digest-{row['published_date']}.md"
        if os.path.exists(path):
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(row))
        print("saved:", path)
        new += 1
    print(f"done — {new} new digest(s), {len(rows)} day(s) in DB")


if __name__ == "__main__":
    main()
