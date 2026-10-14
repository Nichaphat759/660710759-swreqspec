# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-14 06:47 | test: 7 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | ยังไม่มีการตรวจ booking ซ้ำใน backend/app/booking/service.py:create_booking (T-04 ยังพร้อมทำ) | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | frontend/src/pages/ConfirmBooking.jsx: confirm (ข้อความและรายการทางเลือก); backend ยังไม่มีการคำนวณ alternatives (T-05 ยังพร้อมทำ) | frontend/src/__tests__/AC-BKG-03.test.jsx (ผ่าน แต่ assert ไม่ครบทุก Then) | ช่องโหว่ |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py: create_booking, next_queue_no; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_01.py::test_AC_BKG_01 (ผ่าน แต่ตรวจเพียง HTTP 201) | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 | ยังไม่มีระบบ notification/retry (T-07 ยังพร้อมทำ) | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02, T-10 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (ผ่าน แต่ยิงแบบลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน) | ช่องโหว่ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี | ไม่มีการตั้งค่า TLS/HTTPS ใน backend/app/ หรือ frontend/ | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มีคิวส่งซ้ำภายใน 5 นาที | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี | ไม่มีการประเมินความง่ายในการใช้หรือการทดสอบผู้ใช้ใหม่ | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL (ค่าเริ่มต้นเป็น SQLite) | backend/tests/test_T01_schema.py (ผ่าน) | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | ไม่มี middleware audit log ใน backend/app/ | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/auth/idp.py: get_verified_hn; backend/app/booking/router.py: create_booking | ไม่มี test ยืนยันว่า token ที่ไม่ผ่านการยืนยันถูกปฏิเสธ | ช่องโหว่ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/booking/router.py: BookingRequest.national_id; backend/app/db/models.py: Booking.hn | backend/tests/test_T01_schema.py::test_T01_no_national_id (ผ่าน; ทดสอบเฉพาะ schema) | ช่องโหว่ |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มีระบบส่งข้อความแบบ async หรือ retry queue | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: GET /slots; backend/app/slots/service.py: list_available_slots | FR-BKG-01, FR-BKG-06 | ไม่ตรง/บางส่วน | คืนเฉพาะช่วงที่ remaining > 0 พร้อมจำนวนคงเหลือและกรอง package แต่จำกัด 14 วันแทน 30 วัน |
| frontend/src/pages/SlotPicker.jsx: SlotPicker | FR-BKG-01, FR-BKG-06, UI-BKG-01 | ไม่ครบ | เลือกแพ็กเกจและโหลดช่วงใหม่ได้; ไม่มีส่วนเลือกวันใน UI และแสดง "ว่าง N" แทนข้อความที่ mockup กำหนด "เหลือ N ที่" |
| backend/app/booking/router.py: POST /bookings; BookingRequest | FR-BKG-02, FR-BKG-03, FR-BKG-04, IF-HIS-01 | ไม่ครบ/มีข้อมูลเกินสัญญา | รับ slot_id ได้ แต่ไม่มี logic กันจองซ้ำหรือ alternatives; รับ national_id ที่ไม่อยู่ในสัญญา API และไม่ได้ส่งต่อ HIS |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ไม่ครบ | บันทึกและลด remaining แต่ตรวจเต็มด้วย remaining < 0 จึงยังยอมให้จองเมื่อเหลือ 0; ไม่มีการส่ง notification |
| backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | ไม่ตรง | กำหนดรูปแบบ A001 เริ่มใหม่ทุกวันเอง ทั้งที่ Q-02 ยังไม่มีคำตอบ |
| backend/app/booking/router.py: DELETE /bookings/{booking_id}; backend/app/booking/service.py: cancel_booking; frontend/src/api/client.js: cancelBooking | ไม่มี; Out of scope UC-02 | ไม่ตรง | เพิ่มความสามารถยกเลิกการจองและคืนที่นั่ง ซึ่งอยู่ใน Out of scope |
| backend/app/booking/router.py: create_booking (logging) | IF-HIS-01 | ไม่ตรง | log ค่า national_id ที่รับมา แม้ไม่มีการใช้ lookup HIS และไม่จำเป็นต่อการจอง |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | บางส่วน | ปฏิเสธ header ที่ไม่มี prefix ตาม mock แต่ไม่ได้เชื่อมต่อหรือรับผลจากระบบยืนยันตัวตนจริงตาม interface |
| backend/app/config.py: DATABASE_URL; backend/app/db/session.py: engine | CON-TECH-01 | ไม่แน่นอน | ใช้ PostgreSQL ได้เมื่อกำหนด DATABASE_URL แต่ fallback เป็น SQLite แม้ไม่มีค่า config |
| backend/app/db/models.py: Booking; backend/app/db/migrations/001_init.py: upgrade | IF-HIS-01, DOM-PDPA-01 | บางส่วน | bookings ไม่มี national_id และเก็บ hn; audit_logs ถูกสร้างแต่ไม่มีการเขียน log จริง |
| backend/app/main.py: lifespan, app | CON-TECH-01, DOM-PDPA-01 | ไม่ครบ | สร้างตารางเมื่อเริ่มระบบ แต่ไม่ได้ติดตั้ง audit middleware |
| frontend/src/pages/ConfirmBooking.jsx: confirm | FR-BKG-03, FR-BKG-04, UI-BKG-02 | บางส่วน | แสดงข้อความ "ช่วงเวลาเต็ม" และสูงสุด 3 ตัวเลือกพร้อมวันที่/เวลา; จำนวนอาจต่ำกว่า 3 หาก API ส่งข้อมูลมาไม่ครบ และไม่มี backend ที่คัด 3 รายการใกล้ที่สุด |
| frontend/src/api/client.js: createBooking | FR-BKG-04 | บางส่วน | เรียก POST /bookings ตาม slot_id; ไม่มีการจัดการข้อผิดพลาดอื่นนอกจาก status ที่ส่งกลับ |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง / ของแถม

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | spec ระบุภายใน 30 วันข้างหน้า แต่โค้ดใช้ 14 วันเท่านั้น จึงไม่มีการแสดงช่วงเวลาเต็มตามข้อกำหนด | แก้โค้ด |
| F-005 | ละเมิด Constraint | backend/app/config.py: DATABASE_URL | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite แทน PostgreSQL และไม่บังคับใช้การตั้งค่า DATABASE_URL ในรันจริง | แก้โค้ด |
| F-007 | FR ไม่มี AC | backend/app/slots/service.py: list_available_slots | FR-BKG-06 | requirement มีพฤติกรรมเปลี่ยนแพ็กเกจแล้วคำนวณช่วงเวลาว่างใหม่ แต่ไม่มี AC ที่ตรวจตรงเรื่องนี้โดยตรง | เพิ่ม Q-xx |
| F-008 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | queue_no ใช้รูปแบบ A001 ที่คิดขึ้นเองจาก assumption แม้ spec ยังให้ Q-02 เป็น open question | เพิ่ม Q-xx |
| F-009 | ของแถม | backend/app/booking/router.py: DELETE /bookings/{booking_id}; backend/app/booking/service.py: cancel_booking; frontend/src/api/client.js: cancelBooking | Out of scope: ยกเลิกคิว (UC-02) | มี endpoint และ service สำหรับยกเลิกการจอง/คืนที่นั่ง แม้การยกเลิกคิวถูกระบุไว้อย่างชัดเจนว่าอยู่นอกขอบเขต | |
| F-010 | test อ่อน | backend/tests/test_AC_BKG_01.py::test_AC_BKG_01 | AC-BKG-01, FR-BKG-04 | assert เฉพาะ status 201 ไม่ตรวจว่ามีรายการจองจริง หมายเลขคิวถูกแสดง หรือ remaining ลดเป็น 0 ตาม Then | |
| F-011 | test อ่อน | frontend/src/__tests__/AC-BKG-03.test.jsx | AC-BKG-03, UI-BKG-02 | ตรวจข้อความแจ้งเตือนและจำนวนปุ่ม 3 ปุ่ม แต่ไม่ assert ว่าตัวเลือกทั้งสามแสดงวันและเวลาตามข้อมูลที่ API ส่งมา | |
| F-012 | test อ่อน | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 | AC-BKG-05, NFR-PERF-01 | ยิง request 200 ครั้งเรียงกัน ไม่ได้จำลองผู้ใช้พร้อมกัน 200 คนตาม AC จึงยังยืนยัน p95 ภายใต้ concurrency ที่ระบุไม่ได้ | |
| F-013 | ละเมิด Constraint | backend/app/booking/router.py: BookingRequest และ create_booking logging | IF-HIS-01 | รับ national_id ใน request จองและเขียนลง log ทั้งที่สัญญา POST /bookings รับ slot_id และเลขบัตรควรส่งต่อ HIS โดยไม่เก็บ/บันทึกโดยไม่จำเป็น | |
| F-014 | AC ไม่มี test | backend/app/auth/idp.py: get_verified_hn; backend/tests/test_AC_BKG_01.py | IF-IDP-01 | มีการตรวจ header prefix ในโค้ด แต่ไม่มี test ยืนยันว่าคำขอที่ไม่มีผลยืนยันตัวตนถูกปฏิเสธก่อนเข้าถึงข้อมูล | |
| F-015 | ไม่ตรง mockup | frontend/src/pages/SlotPicker.jsx: SlotPicker | FR-BKG-01, UI-BKG-01 | หน้าจอไม่มีการเลือก/แสดงวันของแต่ละช่วง และแสดงจำนวนเป็น "ว่าง N" แทน "เหลือ N ที่" ตามข้อกำหนด UI ที่ต้องตรง | |
| F-016 | โค้ดไม่มี FR | backend/app/booking/service.py: create_booking | FR-BKG-03 | เงื่อนไข `slot.remaining < 0` ยังยอมให้จองเมื่อเหลือ 0 ที่นั่ง ทำให้ช่วงที่เต็มแล้วถูกจองซ้ำได้ แทนการปฏิเสธและไม่สร้างรายการจอง | |

## 4. แก้แล้ว / ทบทวนข้อค้นพบเดิม
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-003 | ปรับ ConfirmBooking ให้แสดงข้อความ "ช่วงเวลาเต็ม" และ render ทางเลือกได้สูงสุด 3 รายการ แทนข้อความ "เต็มแล้ว" และการจำกัด 2 รายการเดิม | ตรวจ frontend/src/pages/ConfirmBooking.jsx และรัน AC-BKG-03 ผ่าน; งานคำนวณ alternatives ฝั่ง backend ยังไม่เสร็จ จึงยังตามรอย FR-BKG-03 เป็น "ช่องโหว่" |
| F-002, F-004, F-006 | ถอนการจัดเป็นข้อค้นพบในรอบนี้ ไม่ได้ถือว่าแก้แล้ว เพราะ T-04, T-07 และ T-08 ยังไม่เสร็จ | tasks.md ระบุงานเหล่านี้เป็น "พร้อมทำ"; ตามเกณฑ์ /verify ให้รายงานเป็น "ยังไม่ถึง" จนกว่า task จะเสร็จ |
