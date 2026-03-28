import streamlit as st
from datetime import datetime, date, timedelta
from pathlib import Path

# ═══════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════
st.set_page_config(
    page_title="FitPro Manager",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded", #"expanded"
    menu_items={}
)

# ═══════════════════════════════════════════════════
# HIDE STREAMLIT CHROME
# ═══════════════════════════════════════════════════
st.markdown("""
<style>
header[data-testid="stHeader"] {
    background: transparent !important;
    color: white !important;
}
#MainMenu                        {display:none!important;}
.stDeployButton                  {display:none!important;}
footer                           {display:none!important;}
[data-testid="stFooter"]        {display:none!important;}
[data-testid="stToolbar"]       {display:none!important;}
[data-testid="stDecoration"]    {display:none!important;}
.viewerBadge_container__r5tak   {display:none!important;}
.embeddedSocialProofIcon        {display:none!important;}
.block-container {padding-top:1rem!important;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# STYLES
# ═══════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Nunito:wght@400;600;700;800&display=swap');
:root{
  --primary:#FF6B35;--secondary:#1A1A2E;--accent:#FFD700;
  --surface:#16213E;--surface2:#0F3460;--text:#E8E8E8;--subtext:#A0A0B0;
  --success:#2ECC71;--warning:#F39C12;--danger:#E74C3C;
  --radius:12px;--shadow:0 4px 20px rgba(0,0,0,.4);
}
html,body,[data-testid="stAppViewContainer"]{background:var(--secondary)!important;color:var(--text)!important;font-family:'Nunito',sans-serif!important;}

/* ── Sidebar nền + border ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 2px solid var(--surface2) !important;
}
[data-testid="stSidebar"] > div:first-child {
    background: var(--surface) !important;
}

/* ── Nút mũi tên AN sidebar (trong sidebar khi mở) ── */
[data-testid="stSidebarCollapseButton"] {
    display: block !important;
    visibility: visible !important;
    z-index: 100000 !important;
    background: rgba(255,107,53,0.15) !important;
    border-radius: 8px !important;
}
[data-testid="stSidebarCollapseButton"] svg {
    fill: white !important;
    color: white !important;
    stroke: white !important;
    width: 28px !important;
    height: 28px !important;
}
[data-testid="stSidebarCollapseButton"]:hover {
    background: rgba(255,107,53,0.35) !important;
}

/* ── Nút mũi tên MO sidebar (ngoài màn hình khi sidebar đóng) ── */
[data-testid="collapsedControl"] {
    display: block !important;
    visibility: visible !important;
    z-index: 100000 !important;
    background: var(--primary) !important;
    border-radius: 0 8px 8px 0 !important;
    padding: 6px 4px !important;
}
[data-testid="collapsedControl"] svg {
    fill: white !important;
    color: white !important;
    stroke: white !important;
    width: 32px !important;
    height: 32px !important;
}
[data-testid="collapsedControl"]:hover {
    background: #e0552a !important;
}



h1,h2,h3{font-family:'Bebas Neue',sans-serif!important;letter-spacing:1px;}
h1{color:var(--primary)!important;font-size:2.2rem!important;}
h2{color:var(--accent)!important;font-size:1.7rem!important;}
h3{color:var(--text)!important;font-size:1.2rem!important;}
.card{background:var(--surface);border-radius:var(--radius);padding:1.1rem 1.3rem;margin-bottom:.7rem;border-left:4px solid var(--primary);box-shadow:var(--shadow);transition:transform .15s;}
.card:hover{transform:translateY(-1px);}
.card-time{border-left-color:#A78BFA!important;}
.card-pt{border-left-color:#FF6B35!important;}
.card-ok{border-left-color:var(--success)!important;}
.card-warn{border-left-color:var(--warning)!important;}
.mbox{background:linear-gradient(135deg,var(--surface2),var(--surface));border-radius:var(--radius);padding:1rem 1.2rem;text-align:center;border:1px solid rgba(255,107,53,.3);box-shadow:var(--shadow);}
.mbox .val{font-family:'Bebas Neue';font-size:2rem;color:var(--primary);}
.mbox .lbl{font-size:.72rem;color:var(--subtext);text-transform:uppercase;letter-spacing:1px;}
.mbox .sub{font-size:.7rem;color:var(--success);margin-top:.2rem;}
.badge{display:inline-block;padding:.22rem .65rem;border-radius:20px;font-size:.72rem;font-weight:700;letter-spacing:.4px;text-transform:uppercase;}
.b-active{background:rgba(46,204,113,.18);color:#2ECC71;border:1px solid #2ECC71;}
.b-expired{background:rgba(231,76,60,.18);color:#E74C3C;border:1px solid #E74C3C;}
.b-pending{background:rgba(243,156,18,.18);color:#F39C12;border:1px solid #F39C12;}
.b-time{background:rgba(167,139,250,.18);color:#A78BFA;border:1px solid #A78BFA;}
.b-session{background:rgba(255,107,53,.18);color:#FF6B35;border:1px solid #FF6B35;}
.stButton>button{background:linear-gradient(135deg,var(--primary),#e0552a)!important;color:white!important;border:none!important;border-radius:8px!important;font-family:'Nunito'!important;font-weight:700!important;transition:opacity .2s,transform .1s!important;}
.stButton>button:hover{opacity:.88!important;transform:translateY(-1px)!important;}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb],.stDateInput input,.stNumberInput input{background:var(--surface)!important;color:var(--text)!important;border:1px solid var(--surface2)!important;border-radius:8px!important;}
.sidebar-logo{text-align:center;padding:1.1rem 0 .8rem;border-bottom:1px solid var(--surface2);margin-bottom:.8rem;}
.sidebar-logo .brand{font-family:'Bebas Neue';font-size:1.9rem;color:var(--primary);letter-spacing:2px;}
.sidebar-logo .tag{font-size:.65rem;color:var(--subtext);letter-spacing:2px;text-transform:uppercase;}
hr{border-color:var(--surface2)!important;margin:.8rem 0;}
.stTabs [data-baseweb="tab-list"]{background:var(--surface)!important;border-radius:10px;padding:.3rem;}
.stTabs [data-baseweb="tab"]{color:var(--subtext)!important;border-radius:8px;font-weight:600;}
.stTabs [aria-selected="true"]{background:var(--primary)!important;color:white!important;}
.confirm-box{background:linear-gradient(135deg,rgba(255,107,53,.12),rgba(255,107,53,.05));border:2px solid var(--primary);border-radius:var(--radius);padding:1.2rem 1.4rem;margin:.6rem 0;}
.confirm-title{font-family:'Bebas Neue';font-size:1.3rem;color:var(--primary);}
.prog-bar-wrap{background:var(--surface2);border-radius:6px;height:8px;}
.prog-bar{background:var(--primary);height:8px;border-radius:6px;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# LOGO
# ═══════════════════════════════════════════════════
LOGO = """<svg width="56" height="56" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="60" height="60" rx="14" fill="#FF6B35"/>
  <rect x="8" y="27" width="44" height="6" rx="3" fill="white"/>
  <rect x="8" y="24" width="12" height="12" rx="3" fill="white"/>
  <rect x="40" y="24" width="12" height="12" rx="3" fill="white"/>
  <rect x="6" y="22" width="8" height="16" rx="4" fill="#FFD700"/>
  <rect x="46" y="22" width="8" height="16" rx="4" fill="#FFD700"/>
</svg>"""

# ═══════════════════════════════════════════════════
# FIREBASE — optional, safe init
# ═══════════════════════════════════════════════════
def get_db():
    """Returns Firestore client or None (demo mode). Never raises."""
    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
        if not firebase_admin._apps:
            # Only try if secrets key exists
            try:
                fb = st.secrets["firebase"]
            except Exception:
                return None  # No secrets → demo mode
            cred = credentials.Certificate({
                "type": fb["type"],
                "project_id": fb["project_id"],
                "private_key_id": fb["private_key_id"],
                "private_key": fb["private_key"].replace("\\n", "\n"),
                "client_email": fb["client_email"],
                "client_id": fb["client_id"],
                "auth_uri": fb["auth_uri"],
                "token_uri": fb["token_uri"],
                "auth_provider_x509_cert_url": fb["auth_provider_x509_cert_url"],
                "client_x509_cert_url": fb["client_x509_cert_url"],
            })
            firebase_admin.initialize_app(cred)
        from firebase_admin import firestore as fs
        return fs.client()
    except Exception:
        return None

# Init once per session
if "db" not in st.session_state:
    st.session_state.db = get_db()
db = st.session_state.db

# ═══════════════════════════════════════════════════
# MOCK DATA
# ═══════════════════════════════════════════════════
MOCK_USERS = {
    "owner@fitpro.vn":  {"password": "owner123", "role": "owner",    "name": "Chủ Phòng Gym"},
    "pt1@fitpro.vn":    {"password": "pt123",    "role": "pt",       "name": "Nguyễn Văn A", "pt_id": "pt1"},
    "pt2@fitpro.vn":    {"password": "pt456",    "role": "pt",       "name": "Trần Thị B",   "pt_id": "pt2"},
    "khach1@gmail.com": {"password": "kh123",    "role": "customer", "name": "Lê Văn Cường", "customer_id": "kh1"},
    "khach2@gmail.com": {"password": "kh456",    "role": "customer", "name": "Nguyễn Thị Hà","customer_id": "kh2"},
}

MOCK_MEMBERSHIPS = [
    {"id":"m1","customer_id":"kh1","customer_name":"Lê Văn Cường",
     "type":"session","package_name":"Gói PT Premium",
     "pt_id":"pt1","pt_name":"PT Nguyễn Văn A",
     "sessions_total":36,"sessions_done":22,"start_date":"2025-01-01","status":"active","notes":"Mục tiêu giảm mỡ tăng cơ"},
    {"id":"m2","customer_id":"kh2","customer_name":"Nguyễn Thị Hà",
     "type":"time","package_name":"Gói Yoga 3 tháng",
     "pt_id":None,"pt_name":None,
     "start_date":"2025-02-01","end_date":"2026-05-01","status":"active","notes":"Yoga buổi sáng"},
    {"id":"m3","customer_id":"kh1","customer_name":"Lê Văn Cường",
     "type":"time","package_name":"Gói Gym 6 tháng",
     "pt_id":None,"pt_name":None,
     "start_date":"2025-01-15","end_date":"2026-07-15","status":"active","notes":"Tập tự do buổi tối"},
    {"id":"m4","customer_id":"kh2","customer_name":"Nguyễn Thị Hà",
     "type":"session","package_name":"Gói PT Starter",
     "pt_id":"pt2","pt_name":"PT Trần Thị B",
     "sessions_total":10,"sessions_done":8,"start_date":"2025-03-01","status":"active","notes":""},
]

MOCK_PENDING = [
    {"id":"p1","membership_id":"m1","customer_id":"kh1","customer_name":"Lê Văn Cường",
     "pt_id":"pt1","pt_name":"PT Nguyễn Văn A",
     "session_date":"2026-03-22","session_time":"09:00",
     "content":"Leg Day: Squat 4x10@60kg, Deadlift 4x8@80kg, Leg Press 3x12@100kg",
     "note":"Tăng tạ squat lần sau","status":"pending_customer"},
]

MOCK_SESSIONS = [
    {"id":"s1","membership_id":"m1","customer_id":"kh1","pt_id":"pt1",
     "session_date":"2026-03-20","session_time":"09:00",
     "content":"Upper Body: Bench 4x10@60kg, Row 4x10@50kg, OHP 3x10@40kg",
     "note":"Tốt, tăng tạ bench lần sau","weight":74.5,"confirmed":True},
    {"id":"s2","membership_id":"m1","customer_id":"kh1","pt_id":"pt1",
     "session_date":"2026-03-18","session_time":"09:00",
     "content":"Cardio 30ph + Core: Plank 3x60s, Ab wheel 3x15",
     "note":"","weight":75.0,"confirmed":True},
]

# ═══════════════════════════════════════════════════
# SESSION STATE INIT
# ═══════════════════════════════════════════════════
defaults = {
    "logged_in": False,
    "user": None,
    "page": "dashboard",
    "pending_list": [p.copy() for p in MOCK_PENDING],
    "memberships":  [m.copy() for m in MOCK_MEMBERSHIPS],
    "sessions_log": [s.copy() for s in MOCK_SESSIONS],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ═══════════════════════════════════════════════════
# AUTH
# ═══════════════════════════════════════════════════
def do_login(email_raw, password):
    email = email_raw.strip().lower()

    # ── Firebase path ──────────────────────────────
    if db is not None:
        try:
            from firebase_admin import firestore as fs
            col = fs.client().collection("users")
            for doc in col.where("email", "==", email).limit(1).stream():
                u = doc.to_dict()
                if u.get("password") == password:
                    st.session_state.logged_in = True
                    st.session_state.user = {**u, "id": doc.id}
                    return True
            # Found Firebase but user not in DB → also try mock so dev accounts work
        except Exception:
            pass  # Firebase error → fall through

    # ── Mock / demo path ───────────────────────────
    if email in MOCK_USERS:
        u = MOCK_USERS[email]
        if u["password"] == password:
            user = u.copy()
            user["email"] = email
            st.session_state.logged_in = True
            st.session_state.user = user
            return True

    return False

# ═══════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════
def days_left(s):
    try:
        return (date.fromisoformat(s) - date.today()).days
    except Exception:
        return None

def fmt_date(s):
    try:
        return date.fromisoformat(s).strftime("%d/%m/%Y")
    except Exception:
        return s

def status_color(d):
    if d is None: return "var(--subtext)"
    if d < 0:     return "var(--danger)"
    if d <= 7:    return "var(--warning)"
    return "var(--success)"

def get_my_memberships(uid):
    return [m for m in st.session_state.memberships if m.get("customer_id") == uid]

def get_pt_memberships(pid):
    return [m for m in st.session_state.memberships if m.get("pt_id") == pid]

def get_pending_customer(cid):
    return [p for p in st.session_state.pending_list
            if p.get("customer_id") == cid and p.get("status") == "pending_customer"]

def get_pending_pt(pid):
    return [p for p in st.session_state.pending_list if p.get("pt_id") == pid]

def sessions_left(m):
    return m.get("sessions_total", 0) - m.get("sessions_done", 0)

def card(html, cls=""):
    st.markdown(f'<div class="card {cls}">{html}</div>', unsafe_allow_html=True)

def mbox(val, lbl, sub=""):
    st.markdown(f'<div class="mbox"><div class="val">{val}</div><div class="lbl">{lbl}</div><div class="sub">{sub}</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# MEMBERSHIP CARD
# ═══════════════════════════════════════════════════
def render_mem(m, show_customer=False, show_pt=True):
    mtype = m.get("type", "session")
    pkg   = m.get("package_name", "")

    if mtype == "time":
        dl    = days_left(m.get("end_date", ""))
        color = status_color(dl)
        s_txt = ("Còn " + str(dl) + " ngày") if (dl is not None and dl >= 0) else "Đã hết hạn"
        bcls  = "b-active" if (dl or 0) > 0 else "b-expired"
        tbadge = '<span class="badge b-time">⏱ Theo thời gian</span>'
        detail = (
            '<div style="font-size:.82rem;margin:.5rem 0">'
            '📅 <b>' + fmt_date(m.get("start_date","")) + '</b> → '
            '<b>' + fmt_date(m.get("end_date","")) + '</b>'
            ' &nbsp; <span style="color:' + color + ';font-weight:700">' + s_txt + '</span>'
            '</div>'
        )
    else:
        done  = m.get("sessions_done", 0)
        total = m.get("sessions_total", 0)
        left  = total - done
        pct   = int(done / total * 100) if total else 0
        bcls  = "b-active" if left > 0 else "b-expired"
        tbadge = '<span class="badge b-session">🏋️ Theo buổi PT</span>'
        detail = (
            '<div style="font-size:.82rem;margin:.5rem 0 .3rem">'
            '💪 <b>' + str(left) + ' buổi còn lại</b> / ' + str(total) +
            ' <span style="color:var(--subtext)">(' + str(done) + ' đã tập)</span>'
            '</div>'
            '<div class="prog-bar-wrap" style="margin:.3rem 0 .5rem">'
            '<div class="prog-bar" style="width:' + str(pct) + '%"></div>'
            '</div>'
        )

    blbl  = "Còn hạn / Còn buổi" if bcls == "b-active" else "Hết hạn / Hết buổi"
    cline = '<div style="font-size:.82rem;color:var(--subtext)">👤 ' + m.get("customer_name","") + '</div>' if show_customer else ""
    pline = '<div style="font-size:.82rem;color:var(--subtext)">💪 PT: ' + m.get("pt_name","") + '</div>' if (show_pt and m.get("pt_name")) else ""
    nline = '<div style="font-size:.8rem;color:var(--subtext);font-style:italic">📝 ' + m.get("notes","") + '</div>' if m.get("notes") else ""
    cls   = "card-time" if mtype == "time" else "card-pt"

    st.markdown(
        '<div class="card ' + cls + '">'
        '<div style="display:flex;justify-content:space-between;align-items:flex-start">'
        '<div><b style="font-size:1rem">' + pkg + '</b> '
        '<span class="badge ' + bcls + '">' + blbl + '</span></div>'
        '<div>' + tbadge + '</div>'
        '</div>'
        + cline + pline + detail + nline +
        '</div>',
        unsafe_allow_html=True
    )

# ═══════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════
def render_sidebar():
    with st.sidebar:
        st.markdown(
            '<div class="sidebar-logo">' + LOGO +
            '<div class="brand">FitPro</div>'
            '<div class="tag">Gym Management System</div>'
            '</div>',
            unsafe_allow_html=True
        )
        user  = st.session_state.user
        role  = user.get("role")
        rlbl  = {"owner":"👑 Chủ phòng gym","pt":"💪 Personal Trainer","customer":"🏃 Khách hàng"}.get(role, role)
        n_p   = len(get_pending_customer(user.get("customer_id",""))) if role=="customer" else len(get_pending_pt(user.get("pt_id",""))) if role=="pt" else 0
        st.markdown(
            '<div class="card" style="margin-bottom:.8rem;border-left-color:var(--accent)">'
            '<div style="font-weight:700">' + user.get("name","") + '</div>'
            '<div style="font-size:.78rem;color:var(--subtext)">' + rlbl + '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown("---")

        nav = {
            "owner":    [("📊","dashboard","Tổng quan"),("👥","customers","Khách hàng"),("🏋️","pts","Personal Trainer"),("📦","packages","Gói tập"),("📈","reports","Báo cáo")],
            "pt":       [("📊","dashboard","Tổng quan"),("👥","my_customers","Khách của tôi"),("✍️","record_session","Ghi nhận buổi tập"),("📋","pt_sessions","Lịch sử buổi tập")],
            "customer": [("📊","dashboard","Tổng quan"),("🎫","my_memberships","Gói tập của tôi"),("✅","confirm_session","Xác nhận buổi tập"),("📖","my_sessions","Nhật ký tập"),("📈","progress","Kết quả")],
        }
        for icon, key, label in nav.get(role, []):
            badge = f" 🔴{n_p}" if (key == "confirm_session" and n_p) else ""
            if st.button(f"{icon}  {label}{badge}", key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()

        st.markdown("---")
        if st.button("🚪  Đăng xuất", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user      = None
            st.session_state.page      = "dashboard"
            st.rerun()

# ═══════════════════════════════════════════════════
# LOGIN PAGE
# ═══════════════════════════════════════════════════
def page_login():
    _, col, _ = st.columns([1, 1.1, 1])
    with col:
        st.markdown(
            '<div style="text-align:center;padding:2rem 0 1.2rem">' +
            LOGO.replace('width="56"','width="80"').replace('height="56"','height="80"') +
            '<h1 style="margin:.5rem 0 .1rem">FitPro Manager</h1>'
            '<p style="color:var(--subtext);font-size:.85rem">Hệ thống quản lý phòng tập chuyên nghiệp</p>'
            '</div>',
            unsafe_allow_html=True
        )
        email    = st.text_input("Email", placeholder="email@fitpro.vn")
        password = st.text_input("Mật khẩu", type="password", placeholder="••••••••")

        if st.button("Đăng nhập", use_container_width=True):
            if do_login(email, password):
                st.rerun()
            else:
                st.error("Sai email hoặc mật khẩu!")

        # Always show demo accounts
        st.markdown(
            '<div style="background:rgba(255,107,53,.08);border:1px solid rgba(255,107,53,.3);'
            'border-radius:10px;padding:1rem;margin-top:1rem;font-size:.82rem;line-height:1.8">'
            '<b>⚡ Tài khoản demo</b><br>'
            '👑 owner@fitpro.vn &nbsp;/&nbsp; <b>owner123</b><br>'
            '💪 pt1@fitpro.vn &nbsp;/&nbsp; <b>pt123</b><br>'
            '💪 pt2@fitpro.vn &nbsp;/&nbsp; <b>pt456</b><br>'
            '🏃 khach1@gmail.com &nbsp;/&nbsp; <b>kh123</b><br>'
            '🏃 khach2@gmail.com &nbsp;/&nbsp; <b>kh456</b>'
            '</div>',
            unsafe_allow_html=True
        )

# ═══════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════
def page_dashboard():
    user = st.session_state.user
    role = user.get("role")
    st.markdown(f"# 📊 Xin chào, {user.get('name','')}!")
    st.markdown(f"<span style='color:var(--subtext)'>{datetime.now().strftime('%A, %d/%m/%Y')}</span>", unsafe_allow_html=True)
    st.markdown("---")

    if role == "owner":
        all_m = st.session_state.memberships
        c1,c2,c3,c4 = st.columns(4)
        with c1: mbox(len({m["customer_id"] for m in all_m if m["status"]=="active"}), "Khách đang hoạt động")
        with c2: mbox(sum(1 for m in all_m if m["type"]=="time" and m["status"]=="active"), "Gói thời gian", "active")
        with c3: mbox(sum(1 for m in all_m if m["type"]=="session" and m["status"]=="active"), "Gói buổi PT", "active")
        with c4: mbox(len(st.session_state.pending_list), "Chờ xác nhận", "buổi PT")
        st.markdown("---")
        ca, cb = st.columns(2)
        with ca:
            st.markdown("## ⏱ Gói thời gian sắp hết")
            shown = False
            for m in all_m:
                if m["type"] == "time":
                    dl = days_left(m.get("end_date",""))
                    if dl is not None and 0 <= dl <= 14:
                        shown = True
                        c = "var(--danger)" if dl <= 7 else "var(--warning)"
                        card(f'<b>{m["customer_name"]}</b> – {m["package_name"]}<span style="float:right;color:{c};font-weight:700">Còn {dl} ngày</span>', "card-warn")
            if not shown: st.info("Không có gói nào sắp hết hạn.")
        with cb:
            st.markdown("## 🏋️ Gói PT sắp hết buổi")
            shown = False
            for m in all_m:
                if m["type"] == "session":
                    left = sessions_left(m)
                    if 0 < left <= 5:
                        shown = True
                        card(f'<b>{m["customer_name"]}</b> – {m["package_name"]}<span style="float:right;color:var(--warning);font-weight:700">Còn {left} buổi</span>', "card-warn")
            if not shown: st.info("Không có gói nào sắp hết buổi.")

    elif role == "pt":
        pid   = user.get("pt_id","")
        my_m  = get_pt_memberships(pid)
        pend  = get_pending_pt(pid)
        c1,c2,c3 = st.columns(3)
        with c1: mbox(len({m["customer_id"] for m in my_m if m["status"]=="active"}), "Khách của tôi")
        with c2: mbox(len(pend), "Chờ KH xác nhận")
        with c3: mbox(sum(m.get("sessions_done",0) for m in my_m if m["type"]=="session"), "Tổng buổi đã tập")
        if pend:
            st.markdown("---"); st.markdown("## ⏳ Chờ khách xác nhận")
            for p in pend:
                card(f'<b>{p["customer_name"]}</b> | {p["session_date"]} {p["session_time"]}<span class="badge b-pending" style="float:right">Chờ KH xác nhận</span><div style="font-size:.82rem;color:var(--subtext);margin-top:.4rem">📋 {p["content"]}</div>', "card-warn")
        st.markdown("---"); st.markdown("## Khách hàng & số buổi")
        for m in my_m:
            if m["type"] == "session":
                render_mem(m, show_customer=True, show_pt=False)

    else:  # customer
        cid   = user.get("customer_id","")
        my_m  = get_my_memberships(cid)
        pend  = get_pending_customer(cid)
        tpkgs = [m for m in my_m if m["type"]=="time"    and m["status"]=="active"]
        spkgs = [m for m in my_m if m["type"]=="session" and m["status"]=="active"]
        c1,c2,c3 = st.columns(3)
        with c1: mbox(len(tpkgs), "Gói thời gian active")
        with c2: mbox(sum(sessions_left(m) for m in spkgs), "Buổi PT còn lại")
        with c3: mbox(len(pend), "Buổi chờ xác nhận")
        if pend:
            st.markdown("---"); st.markdown("## 🔔 Cần xác nhận")
            for p in pend:
                st.markdown(
                    '<div class="confirm-box">'
                    '<div class="confirm-title">⚠️ PT ghi nhận buổi – cần xác nhận!</div>'
                    '<div style="margin:.5rem 0;font-size:.88rem">📅 <b>' + p["session_date"] + '</b> lúc <b>' + p["session_time"] + '</b> | 💪 ' + p["pt_name"] + '</div>'
                    '<div style="font-size:.85rem;color:var(--subtext)">📋 ' + p["content"] + '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
            if st.button("✅ Xác nhận ngay"):
                st.session_state.page = "confirm_session"; st.rerun()
        st.markdown("---"); st.markdown("## Gói tập của tôi")
        for m in my_m:
            render_mem(m, show_customer=False, show_pt=True)

# ═══════════════════════════════════════════════════
# MY MEMBERSHIPS (customer)
# ═══════════════════════════════════════════════════
def page_my_memberships():
    st.markdown("# 🎫 Gói tập của tôi"); st.markdown("---")
    cid  = st.session_state.user.get("customer_id","")
    my_m = get_my_memberships(cid)
    if not my_m:
        st.info("Bạn chưa có gói tập nào."); return

    tpkgs = [m for m in my_m if m["type"]=="time"]
    spkgs = [m for m in my_m if m["type"]=="session"]

    if tpkgs:
        st.markdown("## ⏱ Gói theo thời gian")
        st.caption("Gym, yoga, zumba... – tập tự do trong thời hạn")
        for m in tpkgs:
            dl    = days_left(m.get("end_date",""))
            color = status_color(dl)
            render_mem(m, show_customer=False, show_pt=False)
            if dl is not None and dl > 0:
                st.markdown(
                    '<div style="background:rgba(46,204,113,.06);border-radius:8px;padding:.6rem 1rem;'
                    'margin-top:-.4rem;margin-bottom:.8rem;font-size:.85rem">'
                    '⏰ Còn <b style="color:' + color + '">' + str(dl) + ' ngày</b>'
                    ' – hết hạn <b>' + fmt_date(m.get("end_date","")) + '</b>'
                    '</div>',
                    unsafe_allow_html=True
                )
            elif dl is not None:
                st.markdown('<div style="background:rgba(231,76,60,.08);border-radius:8px;padding:.6rem 1rem;margin-top:-.4rem;margin-bottom:.8rem;font-size:.85rem;color:var(--danger)">⛔ Gói đã hết hạn</div>', unsafe_allow_html=True)

    if spkgs:
        st.markdown("---"); st.markdown("## 🏋️ Gói với PT (theo buổi)")
        st.caption("PT ghi nhận → Bạn xác nhận → Số buổi được trừ")
        for m in spkgs:
            done  = m.get("sessions_done",0)
            total = m.get("sessions_total",0)
            left  = total - done
            pct   = int(done/total*100) if total else 0
            render_mem(m, show_customer=False, show_pt=True)
            st.markdown(
                '<div style="background:rgba(255,107,53,.06);border-radius:8px;padding:.7rem 1rem;'
                'margin-top:-.4rem;margin-bottom:.8rem;font-size:.85rem">'
                '🏋️ <b style="color:var(--primary)">' + str(left) + ' buổi còn lại</b>'
                ' | ' + str(done) + '/' + str(total) + ' đã sử dụng'
                '<div class="prog-bar-wrap" style="margin:.5rem 0 0">'
                '<div class="prog-bar" style="width:' + str(pct) + '%"></div>'
                '</div></div>',
                unsafe_allow_html=True
            )

# ═══════════════════════════════════════════════════
# CONFIRM SESSION (customer)
# ═══════════════════════════════════════════════════
def page_confirm_session():
    st.markdown("# ✅ Xác nhận buổi tập"); st.markdown("---")
    cid  = st.session_state.user.get("customer_id","")
    pend = get_pending_customer(cid)

    if not pend:
        st.success("🎉 Không có buổi tập nào cần xác nhận!")
        card("<b>Tất cả đã cập nhật!</b><br><span style='font-size:.85rem;color:var(--subtext)'>Chưa có buổi mới từ PT.</span>", "card-ok")
        return

    st.markdown(
        '<div style="background:rgba(243,156,18,.1);border:1px solid var(--warning);'
        'border-radius:10px;padding:.8rem 1rem;margin-bottom:1.2rem;font-size:.88rem">'
        '⚠️ Bạn có <b style="color:var(--warning)">' + str(len(pend)) + ' buổi tập</b> cần xác nhận.'
        '</div>',
        unsafe_allow_html=True
    )

    for idx, p in enumerate(pend):
        mid  = p.get("membership_id","")
        mem  = next((m for m in st.session_state.memberships if m["id"]==mid), None)
        left = sessions_left(mem) if mem else "?"
        note_html = '<div style="font-size:.82rem;color:var(--subtext)">📝 PT ghi chú: ' + p["note"] + '</div>' if p.get("note") else ""

        st.markdown(
            '<div class="confirm-box">'
            '<div class="confirm-title">📋 Buổi tập #' + str(idx+1) + '</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:.4rem;margin:.6rem 0;font-size:.88rem">'
            '<div>📅 Ngày: <b>' + p["session_date"] + '</b></div>'
            '<div>🕐 Giờ: <b>' + p["session_time"] + '</b></div>'
            '<div>💪 PT: <b>' + p["pt_name"] + '</b></div>'
            '<div>🎫 Còn lại: <b style="color:var(--primary)">' + str(left) + ' buổi</b></div>'
            '</div>'
            '<div style="font-size:.88rem;margin:.4rem 0"><b>Nội dung:</b> ' + p["content"] + '</div>'
            + note_html +
            '</div>',
            unsafe_allow_html=True
        )

        col_ok, col_no, _ = st.columns([1, 1, 2])
        with col_ok:
            if st.button("✅ Xác nhận", key=f"ok_{p['id']}", use_container_width=True):
                for pp in st.session_state.pending_list:
                    if pp["id"] == p["id"]:
                        pp["status"] = "confirmed"
                for m in st.session_state.memberships:
                    if m["id"] == mid:
                        m["sessions_done"] = m.get("sessions_done", 0) + 1
                        if m["sessions_done"] >= m.get("sessions_total", 0):
                            m["status"] = "completed"
                st.session_state.sessions_log.append({
                    "id": "s" + str(len(st.session_state.sessions_log)+1),
                    "membership_id": mid, "customer_id": cid, "pt_id": p["pt_id"],
                    "session_date": p["session_date"], "session_time": p["session_time"],
                    "content": p["content"], "note": p.get("note",""),
                    "weight": 0, "confirmed": True
                })
                st.success("✅ Đã xác nhận! Số buổi đã được cập nhật."); st.rerun()
        with col_no:
            if st.button("❌ Từ chối", key=f"no_{p['id']}", use_container_width=True):
                for pp in st.session_state.pending_list:
                    if pp["id"] == p["id"]:
                        pp["status"] = "rejected"
                st.warning("Đã từ chối."); st.rerun()
        st.markdown("<hr>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# MY SESSIONS (customer)
# ═══════════════════════════════════════════════════
def page_my_sessions():
    st.markdown("# 📖 Nhật ký tập"); st.markdown("---")
    cid  = st.session_state.user.get("customer_id","")
    logs = sorted(
        [s for s in st.session_state.sessions_log if s.get("customer_id")==cid and s.get("confirmed")],
        key=lambda x: x.get("session_date",""), reverse=True
    )
    if not logs:
        st.info("Chưa có buổi tập nào được ghi nhận."); return
    for s in logs:
        note_s = '<div style="font-size:.8rem;color:var(--subtext)">📝 ' + s["note"] + '</div>' if s.get("note") else ""
        st.markdown(
            '<div class="card card-ok">'
            '<div style="display:flex;justify-content:space-between">'
            '<b>' + s.get("session_date","") + ' – ' + s.get("session_time","") + '</b>'
            '<span class="badge b-active">Đã xác nhận</span>'
            '</div>'
            '<div style="margin:.4rem 0;font-size:.88rem">📋 ' + s.get("content","") + '</div>'
            + note_s +
            '</div>',
            unsafe_allow_html=True
        )

# ═══════════════════════════════════════════════════
# PROGRESS (customer)
# ═══════════════════════════════════════════════════
def page_progress():
    st.markdown("# 📈 Kết quả & Tiến độ"); st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📊 Chỉ số ban đầu")
        card('<div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;font-size:.9rem"><div>⚖️ Cân nặng: <b>78 kg</b></div><div>📏 Chiều cao: <b>172 cm</b></div><div>🔥 % Mỡ: <b>28%</b></div><div>💪 % Cơ: <b>30%</b></div><div>📅 Ngày đo: <b>01/01/2026</b></div></div>')
    with c2:
        st.markdown("### 🏆 Chỉ số hiện tại")
        card('<div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;font-size:.9rem"><div>⚖️ Cân nặng: <b style="color:#2ECC71">73 kg ▼5</b></div><div>📏 Chiều cao: <b>172 cm</b></div><div>🔥 % Mỡ: <b style="color:#2ECC71">22% ▼6</b></div><div>💪 % Cơ: <b style="color:#2ECC71">36% ▲6</b></div><div>📅 Ngày đo: <b>20/03/2026</b></div></div>', "card-ok")
    st.markdown("---"); st.markdown("### 📝 Nhận xét PT")
    st.text_area("Nhận xét kết thúc khóa", value="Học viên tiến bộ rõ rệt sau 3 tháng: giảm 5kg cân nặng, -6% mỡ, +6% cơ.", height=100, disabled=True)

# ═══════════════════════════════════════════════════
# PT – MY CUSTOMERS
# ═══════════════════════════════════════════════════
def page_my_customers():
    st.markdown("# 👥 Khách hàng của tôi"); st.markdown("---")
    pid  = st.session_state.user.get("pt_id","")
    my_m = get_pt_memberships(pid)
    if not my_m:
        st.info("Bạn chưa được phân công khách hàng nào."); return
    for m in my_m:
        render_mem(m, show_customer=True, show_pt=False)

# ═══════════════════════════════════════════════════
# PT – RECORD SESSION
# ═══════════════════════════════════════════════════
def page_record_session():
    st.markdown("# ✍️ Ghi nhận buổi tập"); st.markdown("---")
    user = st.session_state.user
    pid  = user.get("pt_id","")
    active_m = [m for m in get_pt_memberships(pid)
                if m["type"]=="session" and m["status"]=="active" and sessions_left(m)>0]

    if not active_m:
        st.warning("Không có khách hàng nào còn buổi tập."); return

    st.markdown(
        '<div style="background:rgba(255,107,53,.08);border:1px solid rgba(255,107,53,.3);'
        'border-radius:10px;padding:.8rem 1rem;margin-bottom:1.2rem;font-size:.88rem">'
        '📌 <b>Quy trình:</b> PT ghi nhận → Khách xác nhận → Số buổi tự động trừ cả 2 bên'
        '</div>',
        unsafe_allow_html=True
    )

    opts = {m["customer_name"] + " – " + m["package_name"] + " (còn " + str(sessions_left(m)) + " buổi)": m for m in active_m}
    sel  = st.selectbox("Chọn khách hàng & gói *", list(opts.keys()))
    mem  = opts[sel]

    card(
        '👤 <b>' + mem["customer_name"] + '</b> &nbsp;|&nbsp; 📦 ' + mem["package_name"] +
        ' &nbsp;|&nbsp; <span style="color:var(--primary);font-weight:700">' + str(sessions_left(mem)) + ' buổi còn lại</span>'
    )

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        s_date   = st.date_input("Ngày tập *", value=date.today())
        s_time   = st.time_input("Giờ bắt đầu *")
    with c2:
        s_weight = st.number_input("Cân nặng (kg)", 30.0, 200.0, 70.0)
        s_fat    = st.number_input("% Mỡ cơ thể", 0.0, 60.0, 20.0)

    s_content = st.text_area("Nội dung buổi tập *", placeholder="Squat 4x10@60kg, Deadlift 3x8@80kg...", height=110)
    s_note    = st.text_area("Ghi chú / nhận xét", placeholder="Form tập, cần cải thiện...", height=80)

    st.markdown("---")
    if st.button("📤 Gửi yêu cầu xác nhận đến khách hàng", use_container_width=True):
        if not s_content.strip():
            st.error("Vui lòng nhập nội dung buổi tập!")
        else:
            new_p = {
                "id": "p" + str(len(st.session_state.pending_list)+1),
                "membership_id": mem["id"],
                "customer_id": mem["customer_id"],
                "customer_name": mem["customer_name"],
                "pt_id": pid,
                "pt_name": user.get("name",""),
                "session_date": str(s_date),
                "session_time": str(s_time)[:5],
                "content": s_content.strip(),
                "note": s_note.strip(),
                "weight": s_weight, "fat": s_fat,
                "status": "pending_customer",
                "created_at": datetime.now().isoformat()
            }
            st.session_state.pending_list.append(new_p)
            if db:
                try: db.collection("pending_sessions").add(new_p)
                except Exception: pass
            st.success(f"✅ Đã gửi yêu cầu xác nhận đến {mem['customer_name']}!")
            st.balloons()

# ═══════════════════════════════════════════════════
# PT – SESSION HISTORY
# ═══════════════════════════════════════════════════
def page_pt_sessions():
    st.markdown("# 📋 Lịch sử buổi tập"); st.markdown("---")
    pid  = st.session_state.user.get("pt_id","")
    tab1, tab2 = st.tabs(["✅ Đã xác nhận", "⏳ Chờ xác nhận"])
    confirmed = [s for s in st.session_state.sessions_log if s.get("pt_id")==pid and s.get("confirmed")]
    pending   = [p for p in st.session_state.pending_list if p.get("pt_id")==pid and p.get("status")=="pending_customer"]

    with tab1:
        if not confirmed:
            st.info("Chưa có buổi tập nào.")
        for s in sorted(confirmed, key=lambda x: x.get("session_date",""), reverse=True):
            mem   = next((m for m in st.session_state.memberships if m["id"]==s.get("membership_id","")), None)
            cname = mem["customer_name"] if mem else s.get("customer_id","")
            note_s = '<div style="font-size:.8rem;color:var(--subtext)">📝 ' + s["note"] + '</div>' if s.get("note") else ""
            st.markdown(
                '<div class="card card-ok">'
                '<div style="display:flex;justify-content:space-between">'
                '<b>👤 ' + cname + '</b><span class="badge b-active">Xác nhận</span>'
                '</div>'
                '<div style="font-size:.83rem;color:var(--subtext)">📅 ' + s.get("session_date","") + ' ' + s.get("session_time","") + '</div>'
                '<div style="font-size:.85rem;margin-top:.3rem">📋 ' + s.get("content","") + '</div>'
                + note_s + '</div>',
                unsafe_allow_html=True
            )
    with tab2:
        if not pending:
            st.info("Không có buổi nào đang chờ.")
        for p in pending:
            card(
                '<div style="display:flex;justify-content:space-between">'
                '<b>👤 ' + p.get("customer_name","") + '</b>'
                '<span class="badge b-pending">Chờ KH xác nhận</span>'
                '</div>'
                '<div style="font-size:.83rem;color:var(--subtext)">📅 ' + p.get("session_date","") + ' ' + p.get("session_time","") + '</div>'
                '<div style="font-size:.85rem;margin-top:.3rem">📋 ' + p.get("content","") + '</div>',
                "card-warn"
            )

# ═══════════════════════════════════════════════════
# OWNER – CUSTOMERS
# ═══════════════════════════════════════════════════
def page_customers_owner():
    st.markdown("# 👥 Quản lý Khách hàng"); st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["📋 Gói tập hiện có", "🎫 Giao gói tập", "➕ Thêm khách"])

    with tab1:
        for m in st.session_state.memberships:
            render_mem(m, show_customer=True, show_pt=True)

    with tab2:
        st.markdown("### 🎫 Giao gói tập")
        st.markdown(
            '<div style="background:rgba(167,139,250,.08);border:1px solid rgba(167,139,250,.3);'
            'border-radius:10px;padding:.8rem 1rem;margin-bottom:1rem;font-size:.85rem">'
            '📌 <b>⏱ Theo thời gian:</b> Gym, Yoga... → cộng thêm ngày<br>'
            '📌 <b>🏋️ Theo buổi PT:</b> PT ghi nhận, KH xác nhận từng buổi'
            '</div>',
            unsafe_allow_html=True
        )
        c1, c2 = st.columns(2)
        with c1:
            g_cname = st.text_input("Tên khách hàng *")
            g_cid   = st.text_input("Customer ID", placeholder="kh1, kh2...")
            g_pkg   = st.text_input("Tên gói tập *", placeholder="Gói Yoga 3 tháng")
        with c2:
            g_type  = st.selectbox("Loại gói *", ["⏱ Theo thời gian", "🏋️ Theo buổi PT"])
            g_start = st.date_input("Ngày bắt đầu", value=date.today())

        g_end = None
        pt_id_sel = pt_name_sel = ""
        if "thời gian" in g_type:
            g_dur = st.selectbox("Thời hạn", ["1 tháng (30 ngày)","3 tháng (90 ngày)","6 tháng (180 ngày)","1 năm (365 ngày)"])
            days  = {"1 tháng (30 ngày)":30,"3 tháng (90 ngày)":90,"6 tháng (180 ngày)":180,"1 năm (365 ngày)":365}[g_dur]
            g_end = g_start + timedelta(days=days)
            st.markdown('<div class="card card-time" style="padding:.7rem 1rem;font-size:.85rem">⏰ Ngày kết thúc: <b>' + fmt_date(str(g_end)) + '</b> (sau ' + str(days) + ' ngày)</div>', unsafe_allow_html=True)
        else:
            g_sessions = st.number_input("Số buổi tập *", 1, 500, 12)
            g_pt  = st.selectbox("Phân công PT *", ["PT Nguyễn Văn A (pt1)", "PT Trần Thị B (pt2)"])
            pt_id_sel, pt_name_sel = {"PT Nguyễn Văn A (pt1)":("pt1","PT Nguyễn Văn A"),"PT Trần Thị B (pt2)":("pt2","PT Trần Thị B")}[g_pt]

        g_note = st.text_input("Ghi chú")
        if st.button("💾 Giao gói tập", use_container_width=True):
            if not g_cname or not g_pkg:
                st.error("Điền đầy đủ thông tin!")
            else:
                nm = {
                    "id": "m" + str(len(st.session_state.memberships)+1),
                    "customer_id": g_cid or "kh" + str(len(st.session_state.memberships)+1),
                    "customer_name": g_cname, "package_name": g_pkg,
                    "start_date": str(g_start), "status": "active", "notes": g_note,
                }
                if "thời gian" in g_type:
                    nm.update({"type":"time","end_date":str(g_end),"pt_id":None,"pt_name":None})
                else:
                    nm.update({"type":"session","sessions_total":g_sessions,"sessions_done":0,"pt_id":pt_id_sel,"pt_name":pt_name_sel})
                st.session_state.memberships.append(nm)
                if db:
                    try: db.collection("memberships").add(nm)
                    except Exception: pass
                st.success(f"✅ Đã giao gói '{g_pkg}' cho {g_cname}!"); st.rerun()

    with tab3:
        st.markdown("### ➕ Thêm khách hàng mới")
        c1, c2 = st.columns(2)
        with c1:
            n_name  = st.text_input("Họ và tên *")
            n_email = st.text_input("Email *")
            n_phone = st.text_input("Số điện thoại")
            n_pwd   = st.text_input("Mật khẩu *", type="password")
        with c2:
            n_gender = st.selectbox("Giới tính", ["Nam","Nữ","Khác"])
            n_dob    = st.date_input("Ngày sinh", value=date(1995,1,1))
            n_note   = st.text_area("Ghi chú")
        c1b,c2b,c3b,c4b = st.columns(4)
        with c1b: n_w = st.number_input("Cân nặng (kg)", 30.0, 200.0, 65.0)
        with c2b: n_h = st.number_input("Chiều cao (cm)", 100.0, 220.0, 165.0)
        with c3b: n_f = st.number_input("% Mỡ", 0.0, 60.0, 20.0)
        with c4b: n_m = st.number_input("% Cơ", 0.0, 60.0, 35.0)
        if st.button("💾 Thêm khách hàng", use_container_width=True):
            if n_name and n_email and n_pwd:
                if db:
                    try: db.collection("users").add({"name":n_name,"email":n_email,"phone":n_phone,"password":n_pwd,"role":"customer","gender":n_gender,"dob":str(n_dob),"initial":{"weight":n_w,"height":n_h,"fat":n_f,"muscle":n_m},"note":n_note,"created_at":datetime.now().isoformat()})
                    except Exception: pass
                st.success(f"✅ Đã thêm {n_name}!")
            else:
                st.error("Điền đầy đủ thông tin bắt buộc!")

# ═══════════════════════════════════════════════════
# OWNER – PT
# ═══════════════════════════════════════════════════
def page_pts():
    st.markdown("# 🏋️ Quản lý Personal Trainer"); st.markdown("---")
    tab1, tab2 = st.tabs(["📋 Danh sách PT", "➕ Thêm PT"])
    with tab1:
        for pt in [{"name":"Nguyễn Văn A","email":"pt1@fitpro.vn","phone":"0934567890","specialty":"Cardio, Weight Loss","exp":"3 năm","customers":2},{"name":"Trần Thị B","email":"pt2@fitpro.vn","phone":"0945678901","specialty":"Yoga, Muscle","exp":"2 năm","customers":1}]:
            card(
                '<div style="display:flex;justify-content:space-between">'
                '<b>💪 ' + pt["name"] + '</b><span class="badge b-active">Đang làm việc</span>'
                '</div>'
                '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.3rem;margin-top:.5rem;font-size:.82rem;color:var(--subtext)">'
                '<div>📧 ' + pt["email"] + '</div><div>📱 ' + pt["phone"] + '</div><div>⏱ ' + pt["exp"] + '</div>'
                '</div>'
                '<div style="margin-top:.4rem;font-size:.83rem">🎯 ' + pt["specialty"] + ' | 👥 ' + str(pt["customers"]) + ' khách</div>',
                "card-pt"
            )
    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            p_name  = st.text_input("Họ và tên PT *")
            p_email = st.text_input("Email *")
            p_phone = st.text_input("Số điện thoại")
            p_pwd   = st.text_input("Mật khẩu *", type="password")
        with c2:
            p_spec = st.text_input("Chuyên môn")
            p_exp  = st.text_input("Kinh nghiệm")
            p_cert = st.text_area("Chứng chỉ")
        if st.button("💾 Thêm PT", use_container_width=True):
            if p_name and p_email and p_pwd:
                if db:
                    try: db.collection("users").add({"name":p_name,"email":p_email,"phone":p_phone,"password":p_pwd,"role":"pt","specialty":p_spec,"experience":p_exp,"certificates":p_cert})
                    except Exception: pass
                st.success(f"✅ Đã thêm PT {p_name}!")
            else: st.error("Điền đầy đủ thông tin!")

# ═══════════════════════════════════════════════════
# OWNER – PACKAGES
# ═══════════════════════════════════════════════════
def page_packages():
    st.markdown("# 📦 Quản lý Gói tập"); st.markdown("---")
    st.markdown(
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem">'
        '<div class="card card-time" style="padding:1rem 1.2rem">'
        '<div style="font-family:\'Bebas Neue\';font-size:1.2rem;color:#A78BFA">⏱ GÓI THEO THỜI GIAN</div>'
        '<div style="font-size:.85rem;margin:.4rem 0;color:var(--subtext)">Gym, yoga, zumba...<br>Tập tự do trong thời hạn<br>Tính ngày kết thúc tự động</div>'
        '</div>'
        '<div class="card card-pt" style="padding:1rem 1.2rem">'
        '<div style="font-family:\'Bebas Neue\';font-size:1.2rem;color:#FF6B35">🏋️ GÓI THEO BUỔI PT</div>'
        '<div style="font-size:.85rem;margin:.4rem 0;color:var(--subtext)">Tập 1-1 với PT<br>PT ghi nhận → KH xác nhận → trừ buổi</div>'
        '</div></div>',
        unsafe_allow_html=True
    )
    tab1, tab2 = st.tabs(["📋 Gói hiện có", "➕ Tạo gói mới"])
    with tab1:
        st.markdown("#### ⏱ Gói theo thời gian")
        c1,c2,c3 = st.columns(3)
        for (n,p,d), col in zip([("Gói Gym Basic 1T","800,000","30 ngày"),("Gói Yoga 3T","2,200,000","90 ngày"),("Gói All-in-One 6T","3,800,000","180 ngày")],[c1,c2,c3]):
            with col:
                st.markdown('<div class="card card-time"><div style="font-family:\'Bebas Neue\';font-size:1.1rem;color:#A78BFA">' + n + '</div><div style="font-size:1.4rem;font-weight:800;margin:.3rem 0">' + p + '<span style="font-size:.75rem"> đ</span></div><div style="font-size:.82rem;color:var(--subtext)">🗓 ' + d + '</div></div>', unsafe_allow_html=True)
        st.markdown("#### 🏋️ Gói theo buổi PT")
        c1,c2,c3 = st.columns(3)
        for (n,p,d), col in zip([("Gói PT Starter","1,500,000","10 buổi"),("Gói PT Premium","3,800,000","36 buổi"),("Gói PT VIP","6,500,000","72 buổi")],[c1,c2,c3]):
            with col:
                st.markdown('<div class="card card-pt"><div style="font-family:\'Bebas Neue\';font-size:1.1rem;color:#FF6B35">' + n + '</div><div style="font-size:1.4rem;font-weight:800;margin:.3rem 0">' + p + '<span style="font-size:.75rem"> đ</span></div><div style="font-size:.82rem;color:var(--subtext)">🏋️ ' + d + '</div></div>', unsafe_allow_html=True)
    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            pg_name = st.text_input("Tên gói *")
            pg_price= st.number_input("Giá (VNĐ)", 0, 99999999, 1000000, step=100000)
            pg_type = st.selectbox("Loại gói", ["⏱ Theo thời gian","🏋️ Theo buổi PT"])
        with c2:
            if "thời gian" in pg_type:
                st.number_input("Thời hạn (ngày)", 1, 730, 30)
            else:
                st.number_input("Số buổi", 1, 500, 10)
            st.text_area("Mô tả gói")
        if st.button("💾 Tạo gói", use_container_width=True):
            if pg_name: st.success(f"✅ Đã tạo gói '{pg_name}'!")

# ═══════════════════════════════════════════════════
# OWNER – REPORTS
# ═══════════════════════════════════════════════════
def page_reports():
    st.markdown("# 📈 Báo cáo & Thống kê"); st.markdown("---")
    all_m = st.session_state.memberships
    c1,c2,c3,c4 = st.columns(4)
    with c1: mbox(sum(1 for m in all_m if m["type"]=="time"    and m["status"]=="active"), "Gói thời gian", "active")
    with c2: mbox(sum(1 for m in all_m if m["type"]=="session" and m["status"]=="active"), "Gói buổi PT",   "active")
    with c3: mbox(sum(m.get("sessions_done",0) for m in all_m if m["type"]=="session"),    "Tổng buổi đã tập")
    with c4: mbox(len(st.session_state.pending_list), "Chờ xác nhận", "buổi PT")
    st.markdown("---")
    ca, cb = st.columns(2)
    with ca:
        st.markdown("### 📦 Gói thời gian sắp hết (≤14 ngày)")
        shown = False
        for m in all_m:
            if m["type"] == "time":
                dl = days_left(m.get("end_date",""))
                if dl is not None and 0 <= dl <= 14:
                    shown = True
                    c = "var(--danger)" if dl<=7 else "var(--warning)"
                    card('<b>' + m["customer_name"] + '</b><br><span style="font-size:.82rem;color:var(--subtext)">' + m["package_name"] + '</span><span style="float:right;color:' + c + ';font-weight:700">Còn ' + str(dl) + ' ngày</span>', "card-warn")
        if not shown: st.info("Không có gói nào sắp hết hạn.")
    with cb:
        st.markdown("### 🏋️ Gói PT sắp hết buổi (≤5 buổi)")
        shown = False
        for m in all_m:
            if m["type"] == "session":
                left = sessions_left(m)
                if 0 < left <= 5:
                    shown = True
                    card('<b>' + m["customer_name"] + '</b><br><span style="font-size:.82rem;color:var(--subtext)">' + m["package_name"] + '</span><span style="float:right;color:var(--warning);font-weight:700">Còn ' + str(left) + ' buổi</span>', "card-warn")
        if not shown: st.info("Không có gói nào sắp hết buổi.")

# ═══════════════════════════════════════════════════
# ROUTER
# ═══════════════════════════════════════════════════
def main():
    if not st.session_state.logged_in:
        page_login()
        return

    render_sidebar()

    routes = {
        "dashboard":       page_dashboard,
        "my_memberships":  page_my_memberships,
        "confirm_session": page_confirm_session,
        "my_sessions":     page_my_sessions,
        "progress":        page_progress,
        "my_customers":    page_my_customers,
        "record_session":  page_record_session,
        "pt_sessions":     page_pt_sessions,
        "customers":       page_customers_owner,
        "packages":        page_packages,
        "reports":         page_reports,
        "pts":             page_pts,
    }
    routes.get(st.session_state.page, page_dashboard)()

if __name__ == "__main__":
    main()
