# Tasks Breakdown: จองคิวตรวจสุขภาพ (Booking)
- Feature: จองคิวตรวจสุขภาพ (Booking)
- Spec ID: SPEC-BKG-001
- อ้างอิง plan.md: specs/001-booking/plan.md
- วันที่: 2026-09-23

## สรุป
- ทำทั้งหมด: 14 task
- รอ Open Questions: 1 task (รอ Q-02)

## รายการ task

### T-01 สร้าง schema และ migration ฐานข้อมูล
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01, FR-BKG-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-01
- ไฟล์ที่แตะ: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: migration สร้างตาราง slots, bookings และ audit_logs ได้พร้อมใช้งานและเชื่อม PostgreSQL ได้ผ่านค่า DATABASE_URL อย่างถูกต้อง
- สถานะ: พร้อมทำ

### T-02 สร้าง API /slots และคำนวณช่วงว่าง
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01, CON-TECH-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_AC_BKG_05.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /slots ส่งคืนช่วงเวลาว่างพร้อมจำนวนที่นั่งคงเหลือ และผล p95 ของเวลาตอบสนองไม่เกิน 2 วินาที เมื่อทดสอบพร้อมกัน 200 ครั้งในสภาพแวดล้อมที่เหมาะสม
- สถานะ: พร้อมทำ

### T-03 สร้าง API จองคิวพื้นฐาน
- รองรับ: FR-BKG-04, IF-IDP-01, IF-HIS-01
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_01.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: POST /bookings บันทึกการจองสำเร็จ ลด remaining ของช่วงเวลานั้น และส่งกลับข้อมูลการจองพร้อม queue_no อย่างชั่วคราวจนกว่าจะมีข้อสรุปจาก Q-02
- สถานะ: พร้อมทำ

### T-04 ป้องกันการจองซ้ำวันเดียวกัน
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_AC_BKG_02.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: test_AC_BKG_02 ผ่าน และเมื่อมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน ระบบตอบกลับ 409 พร้อมหมายเลขคิวเดิม
- สถานะ: พร้อมทำ

### T-05 จัดการช่วงเวลาพเต็มและเสนอ 3 ตัวเลือก
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/slots/service.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_03.py
- ต้องทำหลัง: T-02, T-04
- เสร็จเมื่อ: POST /bookings เมื่อช่วงเวลาถูกยึดเต็มคืน 409 พร้อม 3 ช่วงที่ว่างและใกล้ที่สุดภายในวันเดียวกันและวันถัดไป และไม่มีการจองซ้อนเกิดขึ้น
- สถานะ: พร้อมทำ

### T-06 สร้างคิวส่งข้อความและ resend ตาม ASM-03
- รองรับ: FR-BKG-05, IF-NOT-01, NFR-REL-02
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_04.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: การจองยังถูกบันทึกแม้ notifier ไม่ตอบสนอง และมีรายการค้างส่งในคิวที่กำหนดส่งซ้ำภายใน 5 นาที
- สถานะ: พร้อมทำ

### T-07 บันทึก audit log สำหรับการเข้าถึงข้อมูล
- รองรับ: DOM-PDPA-01, FR-BKG-04
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/tests/test_AC_BKG_06.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: ทุก request ที่เข้าถึงข้อมูลการจองมี audit log ที่ระบุ actor_id, accessed_at และ hn
- สถานะ: พร้อมทำ

### T-08A เติม test สำหรับ AC-BKG-06
- รองรับ: DOM-PDPA-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/tests/test_AC_BKG_06.py
- ต้องทำหลัง: T-07
- เสร็จเมื่อ: test_AC_BKG_06 ผ่าน โดยมีการเปิดดูข้อมูลการจองและตรวจว่ามี audit log ที่มี actor_id, accessed_at และ hn
- สถานะ: พร้อมทำ

### T-08B ค้น HN จาก HIS
- รองรับ: IF-HIS-01, FR-BKG-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-08B
- ไฟล์ที่แตะ: backend/app/his/client.py, backend/app/booking/service.py, backend/tests/test_his_lookup.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /patients/lookup ส่งต่อเลขบัตรไป HIS และคืน HN โดยไม่เก็บเลขบัตรประชาชนในตารางการจอง
- สถานะ: พร้อมทำ

### T-09 ตรวจยืนยันตัวตนบนทุก endpoint
- รองรับ: IF-IDP-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-09
- ไฟล์ที่แตะ: backend/app/auth/idp.py, backend/app/main.py, backend/tests/test_auth_idp.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: API ปฏิเสธคำขอที่ไม่มีผลยืนยันตัวตนก่อนเข้าถึงข้อมูลผู้รับบริการและทำงานร่วมกับ endpoint การจองได้ตามสัญญา
- สถานะ: พร้อมทำ

### T-10 รอคำตอบ Q-02 ก่อนกำหนดเลขคิว
- รองรับ: FR-BKG-04, FR-BKG-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-10
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/booking/service.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: ระบบยืนยันว่าตราบใดที่ Q-02 ยังไม่ได้ตอบ จะไม่กำหนดรูปแบบเลขคิวใด ๆ และรอคำตอบจากเจ้าหน้าที่เวชระเบียนก่อนปรับ logic การออกเลขคิว
- สถานะ: รอ Q-02

### T-11 สร้างหน้าเลือกแพ็กเกจและช่วงเวลา
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-11
- ไฟล์ที่แตะ: frontend/src/App.jsx, frontend/src/pages/SlotPicker.jsx, frontend/src/api/client.js
- ต้องทำหลัง: T-02
- เสร็จเมื่อ: หน้ารับข้อมูลแพ็กเกจและวันที่ แสดงช่วงเวลาที่ว่างพร้อมจำนวนที่นั่งคงเหลือ จาก API จำลองและสามารถเปลี่ยนแพ็กเกจแล้วโหลดช่วงว่างใหม่ได้
- สถานะ: พร้อมทำ

### T-12 สร้างหน้ายืนยันและแสดง 3 ตัวเลือกเมื่อเต็ม
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/__tests__/AC-BKG-03.test.jsx
- ต้องทำหลัง: T-05, T-11
- เสร็จเมื่อ: หน้ายืนยันแสดงข้อความ "ช่วงเวลาเต็ม" พร้อม 3 ตัวเลือกที่แนะนำ เมื่อ API จำลองตอบ 409
- สถานะ: พร้อมทำ

### T-13 ต่อหน้าจอกับ API จริงและแสดงผลการจอง
- รองรับ: FR-BKG-01, FR-BKG-03, FR-BKG-04, FR-BKG-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-13
- ไฟล์ที่แตะ: frontend/src/App.jsx, frontend/src/pages/BookingResult.jsx, frontend/src/api/client.js
- ต้องทำหลัง: T-03, T-05, T-11, T-12
- เสร็จเมื่อ: หน้าแสดงผลการจองเชื่อมต่อ API จริงได้และแสดงหมายเลขคิวพร้อมสภาพของข้อความยืนยันตามสถานะส่งจริง
- สถานะ: พร้อมทำ

## ตารางตรวจความครบ

### 1) AC ID | task ที่ตรวจ AC นี้
| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-03 |
| AC-BKG-02 | T-04 |
| AC-BKG-03 | T-05, T-12 |
| AC-BKG-04 | T-06 |
| AC-BKG-05 | T-02 |
| AC-BKG-06 | T-07, T-08A |

### 2) Constraint ID | task ที่ทำให้เป็นจริง
| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01, T-02 |
| DOM-PDPA-01 | T-01, T-07, T-08A |
| IF-IDP-01 | T-09 |
| IF-HIS-01 | T-08B |
| IF-NOT-01 | T-06 |

## สิ่งที่ยังไม่ทำ
- Q-02: หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร -> ถามเจ้าหน้าที่เวชระเบียน
  - รอ task: T-10
  - ห้ามเดารูปแบบเลขคิว จนกว่าจะได้รับคำตอบจากทีม
