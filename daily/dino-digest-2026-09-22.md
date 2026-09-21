# 🦕 Dino Digest — 22 ก.ย. 2569 (2026-09-22)

## 📈 Market Movers
**Gainers:** FGIWW +181.6901%, IMCC +143.1034%, WALDW +102.8571%
**Losers:** DCX -69.8932%, MKDW -64.1201%, KLXER -55.9748%

## 📅 Earnings Alerts
| Ticker | บริษัท | Est. EPS | เวลา |
|---|---|---|---|
| AZO | AUTOZONE INCORPORATED | 54.97 | pre-market |
| BRTX | BIORESTORATIVE THERAPIES INCORPORATED | 3.0 | – |
| FUL | H. B. FULLER COMPANY | 1.46 | post-market |
| CTAS | CINTAS CORPORATION | 1.35 | pre-market |
| PAYX | PAYCHEX INCORPORATED | 1.33 | pre-market |
| ABVX | ABIVAX SA | -1.08 | post-market |
| THO | THOR INDUSTRIES INCORPORATED | 0.95 | pre-market |
| KBH | KB HOME | 0.88 | post-market |

## 📰 ข่าววันนี้ (25 ชิ้น)

### Morning Brief:
**การมาของ MoE Models พลิกโฉม Inference:** Mixture of Experts (MoE) ในโมเดล AI รุ่นใหม่ไม่ได้เพิ่มแค่จำนวนพารามิเตอร์ แต่ยังเปลี่ยนวิธีที่ข้อมูลถูกประมวลผล จัดเก็บ และเคลื่อนย้ายบนฮาร์ดแวร์เพื่อการอนุมาน (Inference) อย่างสิ้นเชิง
**สี่โหมดการทำงานที่แตกต่าง:** การอนุมานถูกแบ่งเป็น 4 โหมดหลัก ได้แก่ Prefill, Midfill, Decode Attention และ Decode Experts ซึ่งแต่ละโหมดมีความต้องการด้านการประมวลผล หน่วยความจำ และเครือข่ายที่แตกต่างกันอย่างมาก ทำให้การจัดการทรัพยากรต้องปรับเปลี่ยนตามลักษณะงาน
**KV Cache คือหัวใจสำคัญ:** การจัดการสถานะของโมเดล (KV state หรือ KV cache) ในรูปของ "immutable blobs" ที่เคลื่อนที่ระหว่างส่วนต่างๆ ของระบบ เป็นกุญแจสำคัญในการรักษาบริบทการสนทนาที่ยาวนานและซับซ้อนของ AI
**การออกแบบฮาร์ดแวร์และ Network คือตัวชี้วัดประสิทธิภาพ:** ประสิทธิภาพของระบบ AI Inference ขึ้นอยู่กับการจัดเรียงโหนด, แร็ค, และการใช้ Parallelism แบบต่างๆ (Pipeline, Tensor, Expert) รวมถึงการบริหารจัดการ Memory Bandwidth และ Memory Capacity ให้เหมาะสมกับแต่ละโหมดการทำงาน
**การจัดสรรทรัพยากร (Orchestration) ที่ชาญฉลาดเป็นความได้เปรียบ:** การจัดตารางเวลาและปรับแต่ง Worker ให้เข้ากับลักษณะงานแบบเรียลไทม์ (Disaggregation) สามารถเพิ่มประสิทธิภาพและลดต้นทุนได้มหาศาล ขณะที่การรวมศูนย์ (Aggregation) อาจนำไปสู่การสูญเปล่าของทรัพยากรหากขาดความสมดุล

### 📊 1. การจัดสรรงาน (Orchestration) ส่งคำขอผ่านคิวไปยังกลุ่ม Worker
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 ตัวอย่างจาก AgentX: การจัดการบริบทที่ซับซ้อน
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 2. KV State เคลื่อนที่ในรูปแบบ Immutable Blobs
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 3. Prefill, Midfill และ Decode สร้าง Regime การทำงานที่แตกต่างกัน
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 4. Flow ผ่าน MoE Prefill Layer
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 5. Flow ผ่าน MoE Decode Layer
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 6. Midfill คือ Regime การทำงานที่แตกต่าง
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 7. โมเดลคือสแต็คของ Layer Group ที่ทำซ้ำๆ
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 8. การทำงานแบบขนานควรแบ่ง Dataflow ที่แคบของโมเดล
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 9. Logical Accelerator Node
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 10. Nodes ซ้อนกันเป็น Racks
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 11. One Layer Group ใช้ Node ซ้ำได้เมื่อเวลาผ่านไป
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 12. กำหนดขอบเขต Throughput ณ จุดที่ Data Flow มีขนาดเล็กที่สุด
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 13. การทำ Pipeline ตาม Layer Group เมื่อทำได้จริง
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 14. ความลึกของ Pipeline สิ้นสุดที่จุด Crossover ของ KV-Cache
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 15. Prefill และ Midfill เปลี่ยน Sparse Routes เป็น Dense Expert Batches
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 16. Decode ได้ประโยชน์จากการ Batching น้อยกว่า
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📰 17. การจัดตารางเวลา (Scheduling) ทำให้ Disaggregation มีประโยชน์
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 18. Feedback สามารถเปลี่ยนความไม่สมดุลเล็กน้อยให้เป็น Oscillation ได้
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📰 19. การเปรียบเทียบ Aggregation และ Disaggregation
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📰 20. Memory Bandwidth และ Memory Capacity คือวัตถุประสงค์ที่แตกต่างกัน
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://open.substack.com/pub/semianalysis/p/computation-and-data-movement-for

### 📊 ผู้นำเข้าน้ำมันรายใหญ่ที่สุดของโลก
📖 อ่านบทความฉบับเต็ม →
🔗 source: https://mailchi.mp/ed19f89d08bd/oil-importers

### 📰 ความขัดแย้งระหว่าง Amazon และ Meta เรื่อง AI Agent "Muse"

### 📰 อัปเดตเทคโนโลยีและประเด็นน่าสนใจอื่นๆ
