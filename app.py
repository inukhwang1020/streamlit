import streamlit as st

st.set_page_config(
    page_title="황인욱 | Profile",
    page_icon="🐯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  section[data-testid="stSidebar"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  .stApp { background: #f0f4f8; }

  /* ── Hero ─────────────────────────────────────────────── */
  .hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 45%, #1a56a0 100%);
    padding: 64px 56px 56px;
    position: relative; overflow: hidden;
    margin-bottom: 36px;
  }
  .hero-circle1 {
    position: absolute; top: -80px; right: -80px;
    width: 320px; height: 320px; border-radius: 50%;
    background: rgba(255,255,255,0.04);
    pointer-events: none;
  }
  .hero-circle2 {
    position: absolute; bottom: -50px; right: 180px;
    width: 180px; height: 180px; border-radius: 50%;
    background: rgba(255,255,255,0.03);
    pointer-events: none;
  }
  .hero-circle3 {
    position: absolute; top: 30px; right: 260px;
    width: 80px; height: 80px; border-radius: 50%;
    background: rgba(245,158,11,0.08);
    pointer-events: none;
  }
  .avatar {
    width: 108px; height: 108px; border-radius: 50%;
    background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
    display: flex; align-items: center; justify-content: center;
    font-size: 56px; flex-shrink: 0;
    border: 2.5px solid rgba(255,255,255,0.22);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
  }
  .hero-tag {
    display: inline-block;
    font-size: 11.5px; font-weight: 600; letter-spacing: .14em;
    text-transform: uppercase; color: #fbbf24;
    background: rgba(245,158,11,0.15);
    padding: 4px 14px; border-radius: 20px;
    border: 1px solid rgba(245,158,11,0.3);
    margin-bottom: 14px;
  }
  .hero-name {
    font-size: 46px; font-weight: 800; color: #fff;
    line-height: 1.1; margin-bottom: 10px;
    letter-spacing: -.01em;
  }
  .hero-name span {
    background: linear-gradient(90deg, #fbbf24, #f59e0b);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .hero-role {
    font-size: 16px; color: rgba(255,255,255,0.72);
    font-weight: 400; margin-bottom: 14px;
  }
  .hero-tagline {
    display: inline-flex; align-items: center; gap: 7px;
    font-size: 13.5px; color: rgba(255,255,255,0.55);
    background: rgba(255,255,255,0.07);
    padding: 6px 16px; border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
  }

  /* ── Cards ────────────────────────────────────────────── */
  .main-wrap { padding: 0 48px 48px; }
  .card {
    background: #fff;
    border-radius: 18px;
    padding: 28px 30px;
    box-shadow: 0 2px 12px rgba(15,23,42,0.07);
    border: 1px solid rgba(15,23,42,0.06);
    margin-bottom: 24px;
  }
  .sec-title {
    display: flex; align-items: center; gap: 10px;
    font-size: 15px; font-weight: 700; color: #0f172a;
    margin-bottom: 20px; padding-bottom: 12px;
    border-bottom: 1.5px solid #e2e8f0;
  }
  .sec-title-icon {
    width: 32px; height: 32px; border-radius: 9px;
    background: linear-gradient(135deg, #1e3a5f, #1a56a0);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
  }

  /* ── Info rows ────────────────────────────────────────── */
  .info-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 10px 0; border-bottom: 1px solid #f1f5f9;
    font-size: 13.5px;
  }
  .info-row:last-child { border-bottom: none; }
  .info-label { color: #94a3b8; font-weight: 500; }
  .info-value { color: #1e293b; font-weight: 600; }

  /* ── Skill tags ───────────────────────────────────────── */
  .skill-cat {
    font-size: 10.5px; color: #94a3b8; font-weight: 700;
    text-transform: uppercase; letter-spacing: .08em;
    margin: 16px 0 8px;
  }
  .skill-cat:first-child { margin-top: 0; }
  .tag {
    display: inline-block; margin: 3px;
    padding: 5px 14px; border-radius: 20px;
    font-size: 12.5px; font-weight: 500;
  }
  .tag-blue  { background:#eff6ff; color:#1d4ed8; border:1px solid #bfdbfe; }
  .tag-cyan  { background:#ecfeff; color:#0e7490; border:1px solid #a5f3fc; }
  .tag-green { background:#f0fdf4; color:#15803d; border:1px solid #bbf7d0; }
  .tag-amber { background:#fffbeb; color:#b45309; border:1px solid #fde68a; }

  /* ── About text ───────────────────────────────────────── */
  .about-text {
    line-height: 1.9; color: #475569; font-size: 14.5px;
  }
  .about-text strong { color: #0f172a; }

  /* ── Competency ───────────────────────────────────────── */
  .comp-item {
    display: flex; gap: 16px; align-items: flex-start;
    padding: 14px 0; border-bottom: 1px solid #f8fafc;
  }
  .comp-item:last-child { border-bottom: none; }
  .comp-icon {
    width: 44px; height: 44px; border-radius: 12px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center; font-size: 20px;
  }
  .comp-title { font-weight: 700; color: #1e293b; font-size: 14px; margin-bottom: 3px; }
  .comp-desc  { color: #64748b; font-size: 13px; line-height: 1.6; }

  /* ── Career ───────────────────────────────────────────── */
  .career-item {
    display: flex; gap: 20px; align-items: flex-start; flex-wrap: wrap;
    padding: 16px 0; border-bottom: 1px solid #f1f5f9;
  }
  .career-item:last-child { border-bottom: none; }
  .career-badge {
    font-size: 11.5px; font-weight: 700; color: #1a56a0;
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    padding: 4px 14px; border-radius: 20px; flex-shrink: 0;
    border: 1px solid #bfdbfe; min-width: 52px; text-align: center;
  }
  .career-title { font-weight: 700; color: #1e293b; font-size: 15px; margin-bottom: 4px; }
  .career-desc  { color: #64748b; font-size: 13px; line-height: 1.6; }

  /* ── Footer ───────────────────────────────────────────── */
  .footer {
    text-align: center; padding: 32px 0 20px;
    color: #94a3b8; font-size: 12.5px; letter-spacing: .03em;
  }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-circle1"></div>
  <div class="hero-circle2"></div>
  <div class="hero-circle3"></div>
  <div style="display:flex;align-items:center;gap:36px;flex-wrap:wrap;position:relative;z-index:1;">
    <div class="avatar">🐯</div>
    <div>
      <div class="hero-tag">한전KDN &nbsp;·&nbsp; 송변전시스템부</div>
      <div class="hero-name">황<span>인욱</span></div>
      <div class="hero-role">Manager &nbsp;·&nbsp; 송변전시스템부</div>
      <div class="hero-tagline">
        <span>⚡</span>
        <span>변전운영분야 시스템 운영</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Content wrapper ───────────────────────────────────────────
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

left, right = st.columns([2, 3], gap="large")

# ── LEFT ─────────────────────────────────────────────────────
with left:
    # 기본 정보
    st.markdown("""
    <div class="card">
      <div class="sec-title">
        <div class="sec-title-icon">📋</div>기본 정보
      </div>
    """, unsafe_allow_html=True)
    rows = [
        ("🏢 소속",   "한전KDN"),
        ("🏬 부서",   "송변전시스템부"),
        ("💼 직위",   "Manager"),
        ("📍 위치",   "대한민국"),
        ("📧 이메일", "xxxx@kdn.com"),
    ]
    for label, value in rows:
        st.markdown(f"""
        <div class="info-row">
          <span class="info-label">{label}</span>
          <span class="info-value">{value}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 보유 기술
    st.markdown("""
    <div class="card">
      <div class="sec-title">
        <div class="sec-title-icon">🛠</div>보유 기술
      </div>
    """, unsafe_allow_html=True)
    skill_groups = [
        ("전력 시스템", "tag-blue",  ["송변전 시스템", "전력망 관리", "EMS/SCADA"]),
        ("프로그래밍",  "tag-cyan",  ["Python", "SQL", "Streamlit"]),
        ("데이터 분석", "tag-green", ["데이터 분석", "AI 활용", "대시보드"]),
        ("업무 도구",   "tag-amber", ["프로젝트 관리", "MS Office"]),
    ]
    for cat, cls, tags in skill_groups:
        st.markdown(f'<div class="skill-cat">{cat}</div>', unsafe_allow_html=True)
        st.markdown("".join(f'<span class="tag {cls}">{t}</span>' for t in tags),
                    unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── RIGHT ────────────────────────────────────────────────────
with right:
    # 소개
    st.markdown("""
    <div class="card">
      <div class="sec-title">
        <div class="sec-title-icon">👋</div>소개
      </div>
      <p class="about-text">
        안녕하세요, 한전KDN 송변전시스템부에서 근무하고 있는
        <strong>황인욱</strong>입니다.
      </p>
      <p class="about-text" style="margin-top:14px;">
        전력 시스템 IT 분야에서의 전문성을 바탕으로 송변전 시스템의 안정적인 운영과
        디지털 전환을 위한 업무를 담당하고 있습니다.
        데이터 기반의 의사결정과 AI 기술 활용에 관심이 많으며,
        업무 효율화를 위한 다양한 솔루션을 개발·적용하고 있습니다.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # 주요 역량
    st.markdown("""
    <div class="card">
      <div class="sec-title">
        <div class="sec-title-icon">⭐</div>주요 역량
      </div>
    """, unsafe_allow_html=True)
    competencies = [
        ("⚡", "#fff7ed", "전력 시스템 관리",  "송변전 설비 및 전력망 IT 시스템 운영·관리"),
        ("📊", "#eff6ff", "데이터 분석",       "전력 데이터 분석 및 AI 기반 인사이트 도출"),
        ("💻", "#f0fdf4", "시스템 개발",       "업무 자동화 및 데이터 시각화 솔루션 개발"),
        ("🤝", "#faf5ff", "프로젝트 리딩",     "IT 시스템 구축 프로젝트 기획 및 관리"),
    ]
    for icon, bg, title, desc in competencies:
        st.markdown(f"""
        <div class="comp-item">
          <div class="comp-icon" style="background:{bg};">{icon}</div>
          <div>
            <div class="comp-title">{title}</div>
            <div class="comp-desc">{desc}</div>
          </div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── 경력 사항 ─────────────────────────────────────────────────
st.markdown("""
<div class="card">
  <div class="sec-title">
    <div class="sec-title-icon">📌</div>경력 사항
  </div>
""", unsafe_allow_html=True)
careers = [
    ("현재", "한전KDN · 송변전시스템부 Manager",
     "송변전 IT 시스템 운영 및 디지털 전환 업무 담당"),
]
for period, title, desc in careers:
    st.markdown(f"""
    <div class="career-item">
      <div class="career-badge">{period}</div>
      <div>
        <div class="career-title">{title}</div>
        <div class="career-desc">{desc}</div>
      </div>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  © 2026 &nbsp;황인욱 &nbsp;·&nbsp; 한전KDN 송변전시스템부
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
