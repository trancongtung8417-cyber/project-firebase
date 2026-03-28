"""
firebase_seed.py
Chạy 1 lần để tạo dữ liệu mẫu vào Firestore.
Usage: python firebase_seed.py
"""
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, date

#KEY_PATH = "serviceAccountKey.json"   # đổi thành đường dẫn file key của bạn
KEY_PATH = "C:\python\project\gym\serviceAccountKey.json"

def main():
    cred = credentials.Certificate(KEY_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # ── Users ────────────────────────────────
    users = [
        {"email":"owner@fitpro.vn",  "password":"owner123","role":"owner","name":"Chủ Phòng Gym"},
        {"email":"pt1@fitpro.vn",    "password":"pt123",   "role":"pt",   "name":"Nguyễn Văn A (PT)",
         "specialty":"Cardio, Weight Loss","experience":"3 năm"},
        {"email":"pt2@fitpro.vn",    "password":"pt456",   "role":"pt",   "name":"Trần Thị B (PT)",
         "specialty":"Muscle Building, Yoga","experience":"2 năm"},
        {"email":"khach1@gmail.com", "password":"kh123",   "role":"customer","name":"Lê Văn Cường",
         "phone":"0901234567","gender":"Nam"},
    ]
    for u in users:
        db.collection("users").add(u)
        print(f"  Added user: {u['email']}")

    # ── Packages ─────────────────────────────
    packages = [
        {"name":"Gói Basic 1 tháng","price":1500000,"sessions":12,"duration_days":30,
         "features":["12 buổi tập","Tư vấn dinh dưỡng cơ bản"]},
        {"name":"Gói Premium 3 tháng","price":3800000,"sessions":36,"duration_days":90,
         "features":["36 buổi tập","Tư vấn dinh dưỡng","Đo thành phần cơ thể"]},
        {"name":"Gói VIP 6 tháng","price":6500000,"sessions":72,"duration_days":180,
         "features":["72 buổi tập","Dinh dưỡng cá nhân hóa","Đo định kỳ","Ưu tiên đặt lịch"]},
    ]
    for p in packages:
        db.collection("packages").add(p)
        print(f"  Added package: {p['name']}")

    # ── Sample Customer ───────────────────────
    db.collection("customers").add({
        "name":"Lê Văn Cường","email":"khach1@gmail.com","phone":"0901234567",
        "gender":"Nam","dob":"1995-06-15",
        "package":"Gói Premium 3 tháng","pt":"PT Nguyễn Văn A",
        "start_date":"2025-01-01","status":"active",
        "initial":{"weight":78,"height":172,"fat":28,"muscle":30},
        "note":"Mục tiêu giảm mỡ, tăng cơ","created_at":datetime.now().isoformat(),
        "sessions_done":22,"sessions_total":36
    })
    print("  Added sample customer")

    print("\n✅ Firebase seed complete!")

if __name__ == "__main__":
    main()
