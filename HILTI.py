import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
import os
import tempfile
from fpdf import FPDF

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Hilti – Biên Bản Nhận Máy",
    page_icon="🔴",
    layout="centered"
)

# ─── CUSTOM CSS (Giao diện khung trắng viền đỏ) ────────────────────────────────
st.markdown("""
<style>
    .report-container {
        background-color: white;
        border: 2px solid #E2001A;
        padding: 30px;
        border-radius: 10px;
        color: black;
    }
    .hilti-header {
        color: #E2001A;
        font-weight: bold;
        font-size: 24px;
        border-bottom: 2px solid #E2001A;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ─── FIREBASE INIT ────────────────────────────────────────────────────────────
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        try:
            if "firebase" in st.secrets:
                key_dict = dict(st.secrets["firebase"])
                cred = credentials.Certificate(key_dict)
                firebase_admin.initialize_app(cred)
            else:
                return None
        except Exception:
            return None
    return firestore.client()

db = init_firebase()

# ─── HÀM TẠO PDF TIẾNG VIỆT ───────────────────────────────────────────────────
class HiltiPDF(FPDF):
    def header(self):
        # Logo (Thay link hình ảnh của bạn vào đây)
        try:
            self.image("https://www.hilti.com.vn/content/dam/images/local/VN/logos/hilti-logo.png", 10, 8, 33)
        except:
            self.set_font('Arial', 'B', 15)
            self.set_text_color(226, 0, 26)
            self.cell(0, 10, 'HILTI', 0, 1)
        
        self.set_font('Arial', 'B', 15)
        self.ln(10)

def create_pdf(record):
    pdf = HiltiPDF()
    # Thêm Font tiếng Việt (Bạn cần upload file .ttf này lên Github cùng file .py)
    font_path = "Roboto-Regular.ttf" 
    if os.path.exists(font_path):
        pdf.add_font("VietFont", "", font_path, uni=True)
        pdf.set_font("VietFont", "", 12)
    else:
        pdf.set_font("Arial", "", 12) # Fallback nếu thiếu file font

    pdf.add_page()
    
    # Tiêu đề
    pdf.set_text_color(226, 0, 26)
    pdf.set_font(pdf.current_font.family, 'B', 16)
    pdf.cell(0, 10, "BIÊN BẢN NHẬN MÁY", 0, 1, 'C')
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(pdf.current_font.family, '', 10)
    pdf.cell(0, 10, f"Ngày: {record['ngay']} | Mã: {record['ma_bb']}", 0, 1, 'C')
    pdf.ln(5)

    # Thông tin khách hàng
    pdf.set_font(pdf.current_font.family, 'B', 12)
    pdf.cell(0, 10, "THÔNG TIN CHUNG", 0, 1)
    pdf.set_font(pdf.current_font.family, '', 11)
    pdf.cell(0, 8, f"Công ty: {record['cong_ty']}", 0, 1)
    pdf.cell(0, 8, f"Địa chỉ: {record['dia_chi']}", 0, 1)
    pdf.cell(0, 8, f"Người gửi: {record['nguoi_gui']} - SĐT: {record['sdt']}", 0, 1)
    pdf.ln(5)

    # Bảng thiết bị
    pdf.set_font(pdf.current_font.family, 'B', 11)
    pdf.cell(10, 10, "STT", 1)
    pdf.cell(60, 10, "Tên Máy", 1)
    pdf.cell(40, 10, "Số Seri", 1)
    pdf.cell(80, 10, "Tình trạng", 1)
    pdf.ln()

    pdf.set_font(pdf.current_font.family, '', 10)
    for i, item in enumerate(record['thiet_bi'], 1):
        pdf.cell(10, 10, str(i), 1)
        pdf.cell(60, 10, item['ten'], 1)
        pdf.cell(40, 10, item['seri'], 1)
        pdf.cell(80, 10, item['tinh_trang'], 1)
        pdf.ln()

    # Ký tên
    pdf.ln(20)
    pdf.cell(95, 10, "NGƯỜI GỬI", 0, 0, 'C')
    pdf.cell(95, 10, "NHÂN VIÊN TIẾP NHẬN", 0, 1, 'C')
    pdf.ln(15)
    pdf.cell(95, 10, f"(Ký tên: {record['nguoi_gui']})", 0, 0, 'C')
    pdf.cell(95, 10, "(Ký tên)", 0, 1, 'C')

    return pdf.output()

# ─── GIAO DIỆN NHẬP LIỆU ──────────────────────────────────────────────────────
st.title("🔧 Hilti Workshop")
with st.form("hilti_form"):
    col1, col2 = st.columns(2)
    with col1:
        cong_ty = st.text_input("Tên công ty")
        nguoi_gui = st.text_input("Người gửi")
    with col2:
        dia_chi = st.text_input("Địa chỉ")
        sdt = st.text_input("Số điện thoại")
    
    st.write("---")
    st.subheader("Danh sách máy")
    # Đơn giản hóa nhập liệu (ví dụ nhập 1 máy)
    ten_may = st.text_input("Tên máy")
    seri_may = st.text_input("Số Seri")
    tinh_trang = st.selectbox("Tình trạng", ["Không hoạt động", "Hoạt động yếu", "Cần bảo trì"])
    
    submitted = st.form_submit_button("Tạo Biên Bản")

if submitted:
    ma_bb = f"BB{datetime.now().strftime('%Y%m%d%H%M%S')}"
    data = {
        "ma_bb": ma_bb,
        "ngay": datetime.now().strftime("%d/%m/%Y"),
        "cong_ty": cong_ty,
        "dia_chi": dia_chi,
        "nguoi_gui": nguoi_gui,
        "sdt": sdt,
        "thiet_bi": [{"ten": ten_may, "seri": seri_may, "tinh_trang": tinh_trang}]
    }

    # Lưu Firebase
    if db:
        db.collection("receipts").document(ma_bb).set(data)
        st.success("✅ Đã lưu vào hệ thống Firebase!")

    # Hiển thị giao diện khung trắng viền đỏ
    st.markdown(f"""
    <div class="report-container">
        <div class="hilti-header">HILTI - BIÊN BẢN NHẬN MÁY</div>
        <p><b>Mã số:</b> {ma_bb}</p>
        <p><b>Khách hàng:</b> {cong_ty}</p>
        <p><b>Người gửi:</b> {nguoi_gui} ({sdt})</p>
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #eee;">
                <th style="border: 1px solid #ddd; padding: 8px;">Tên Máy</th>
                <th style="border: 1px solid #ddd; padding: 8px;">Số Seri</th>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">{ten_may}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">{seri_may}</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # Nút tải PDF
    pdf_output = create_pdf(data)
    st.download_button(
        label="📥 Tải Biên Bản (PDF)",
        data=pdf_output,
        file_name=f"{ma_bb}.pdf",
        mime="application/pdf"
    )