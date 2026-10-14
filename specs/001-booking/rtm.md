# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-14 06:38 | test: 5 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | ไม่มีตรวจสอบการจองซ้ำวันเดียวกันใน backend/app/booking/service.py:create_booking | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มีการคำนวณช่วงว่าง 3 ตัวเลือกหรือแจ้ง "ช่วงเวลาเต็ม" ใน backend/app/booking/service.py หรือ frontend/src/pages/ | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py: create_booking, next_queue_no; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_01.py::test_AC_BKG_01 (ผ่าน) | รอ Q-xx |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่มีคิวส่งข้อความซ้ำหรือ retry queue | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02, T-10 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน) | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี | ไม่มีการตั้งค่า TLS/HTTPS ใน backend/app/ หรือ frontend/ | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มีคิวส่งซ้ำภายใน 5 นาที | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี | ไม่มีการประเมินความง่ายในการใช้หรือการทดสอบผู้ใช้ใหม่ | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL (ค่าเริ่มต้นเป็น SQLite) | backend/tests/test_T01_schema.py (ผ่าน) | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | ไม่มี middleware audit log ใน backend/app/ | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/auth/idp.py: get_verified_hn; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_01.py (ผ่าน) | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/booking/router.py: BookingRequest.national_id; backend/app/db/models.py: Booking.hn | backend/tests/test_T01_schema.py::test_T01_no_national_id (ผ่าน) | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มีระบบส่งข้อความแบบ async หรือ retry queue | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: GET /slots | FR-BKG-01, FR-BKG-06 | ไม่ตรง | คืนช่วงเวลาที่ยังมีที่นั่งได้ แต่เป็น 14 วันเท่านั้น ไม่ใช่ 30 วันตาม spec |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ไม่ครบ | ตัดที่นั่งและบันทึกสำเร็จ แต่ไม่ตรวจว่ามีคิวที่ยังไม่ได้ใช้ในวันเดียวกันหรือมีช่วงค้างไว้เช่นเดียวกับ FR-BKG-02 |
| backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | ไม่ครบ | ใช้รูปแบบ A001 โดยอิงการเดา Q-02 ไม่ใช่คำตอบจาก staff ที่ยังไม่ได้ชัดเจน |
| backend/app/booking/router.py: create_booking | FR-BKG-04, IF-IDP-01 | ไม่ครบ | ตรวจยืนยันตัวตนแล้ว แต่ไม่มีการจัดการช่วงเต็มพร้อมตัวเลือก 3 ช่วงและไม่มีคิวส่งซ้ำ |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ไม่ตรง | ค่าเริ่มต้นเป็น SQLite ทำให้โค้ดไม่บังคับใช้ PostgreSQL ตาม constraint |
| backend/app/db/models.py: Booking | IF-HIS-01 | ไม่ครบ | เก็บ hn อย่างเดียว แต่ไม่ค้น HN จาก HIS ด้วยเลขบัตรประชาชน และไม่มี validation ต่อ HIS |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ตรง | ตรวจ Authorization header ตามรูปแบบที่สั่งการยืนยันตัวตนก่อนเข้าถึงได้ |
| backend/app/main.py: app | FR-BKG-04, FR-BKG-05 | ไม่ครบ | ไม่มี audit middleware และไม่มี retry queue/notify integration |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | spec ระบุภายใน 30 วันข้างหน้า แต่โค้ดใช้ 14 วันเท่านั้น จึงไม่มีการแสดงช่วงเวลาเต็มตามข้อกำหนด | แก้โค้ด |
| F-002 | โค้ดไม่มี FR | backend/app/booking/service.py: create_booking | FR-BKG-02 | ไม่มีการปฏิเสธเมื่อผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกันและไม่มีการแสดงหมายเลขคิวเดิม | แก้โค้ด |
| F-003 | โค้ดไม่มี FR | backend/app/booking/service.py และ backend/app/booking/router.py | FR-BKG-03 | เมื่อช่วงเวลาที่เลือกเต็ม ไม่มีการแจ้ง "ช่วงเวลาเต็ม" และไม่มีการเสนอ 3 ช่วงว่างใกล้ที่สุด ทั้งใน backend และหน้า UI | แก้โค้ด |
| F-004 | โค้ดไม่มี FR | backend/app/ และ frontend/src/ | FR-BKG-05, IF-NOT-01, NFR-REL-02 | ไม่มีคิวส่งข้อความแบบ async, ไม่มี retry และไม่มีการส่งซ้ำภายใน 5 นาที ตาม spec | แก้โค้ด |
| F-005 | ละเมิด Constraint | backend/app/config.py: DATABASE_URL | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite แทน PostgreSQL และไม่บังคับใช้การตั้งค่า DATABASE_URL ในรันจริง | แก้โค้ด |
| F-006 | โค้ดไม่มี FR | backend/app/main.py และ backend/app/ | DOM-PDPA-01 | ไม่มี audit middleware หรือบันทึก log เมื่อเข้าถึงข้อมูลการจอง แม้ตาราง audit_logs มีอยู่แต่ไม่ถูกใช้งาน | แก้โค้ด |
| F-007 | FR ไม่มี AC | backend/app/slots/service.py: list_available_slots | FR-BKG-06 | requirement มีพฤติกรรมเปลี่ยนแพ็กเกจแล้วคำนวณช่วงเวลาว่างใหม่ แต่ไม่มี AC ที่ตรวจตรงเรื่องนี้โดยตรง | เพิ่ม Q-xx |
| F-008 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | queue_no ใช้รูปแบบ A001 ที่คิดขึ้นเองจาก assumption แม้ spec ยังให้ Q-02 เป็น open question | เพิ่ม Q-xx |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
