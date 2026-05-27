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
  .stApp { background: #ffffff; font-family: 'Pretendard', 'Apple SD Gothic Neo', sans-serif; }

  /* ── Navbar ───────────────────────────────────────────── */
  .navbar {
    position: sticky; top: 0; z-index: 100;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid #f0f0f0;
    padding: 18px 80px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .nav-logo {
    font-size: 18px; font-weight: 800; color: #111;
    letter-spacing: -.02em;
  }
  .nav-logo span { color: #7c3aed; }
  .nav-links {
    display: flex; gap: 36px;
    font-size: 14px; font-weight: 500; color: #555;
  }
  .nav-links a { color: #555; text-decoration: none; }
  .nav-links a:hover { color: #7c3aed; }

  /* ── Page wrapper ─────────────────────────────────────── */
  .page { max-width: 900px; margin: 0 auto; padding: 0 40px 80px; }

  /* ── Hero ─────────────────────────────────────────────── */
  .hero-wrap {
    display: flex; justify-content: space-between; align-items: center;
    padding: 100px 0 80px; gap: 40px;
  }
  .hero-left { flex: 1; }
  .hero-right { flex-shrink: 0; }
  .hero-eyebrow {
    font-size: 16px; font-weight: 600; color: #7c3aed;
    margin-bottom: 14px; letter-spacing: -.01em;
  }
  .hero-name {
    font-size: 72px; font-weight: 900; color: #111;
    line-height: 1.0; letter-spacing: -.04em; margin-bottom: 12px;
  }
  .hero-role {
    font-size: 20px; color: #555; font-weight: 400;
    margin-bottom: 22px; letter-spacing: -.01em;
  }
  .hero-desc {
    font-size: 15px; color: #777; line-height: 1.85;
    max-width: 480px; margin-bottom: 36px;
  }
  .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
  .btn-primary {
    background: linear-gradient(135deg, #7c3aed, #a855f7);
    color: #fff; padding: 13px 28px; border-radius: 10px;
    font-size: 14px; font-weight: 600; border: none;
    cursor: default; box-shadow: 0 4px 14px rgba(124,58,237,.35);
    letter-spacing: -.01em;
  }
  .btn-secondary {
    background: transparent; color: #444;
    padding: 12px 28px; border-radius: 10px;
    font-size: 14px; font-weight: 600;
    border: 1.5px solid #ddd; cursor: default;
    letter-spacing: -.01em;
  }
  .orb {
    width: 320px; height: 320px; border-radius: 50%;
    background: radial-gradient(circle at 38% 35%, #f9a8d4 0%, #c084fc 40%, #818cf8 80%);
    filter: blur(38px); opacity: .82;
  }

  /* ── Divider ──────────────────────────────────────────── */
  .divider { border: none; border-top: 1px solid #f0f0f0; margin: 0; }

  /* ── Section ──────────────────────────────────────────── */
  .section { padding: 64px 0 48px; }
  .sec-title {
    display: flex; align-items: center; gap: 12px;
    font-size: 26px; font-weight: 800; color: #111;
    margin-bottom: 32px; letter-spacing: -.03em;
  }
  .sec-title::before {
    content: ''; display: block;
    width: 5px; height: 30px; border-radius: 3px;
    background: linear-gradient(180deg, #7c3aed, #a855f7);
    flex-shrink: 0;
  }

  /* ── About 2-col ──────────────────────────────────────── */
  .about-wrap { display: flex; gap: 56px; align-items: flex-start; }
  .about-text { flex: 1.2; font-size: 15px; color: #555; line-height: 1.9; }
  .about-text p { margin-bottom: 16px; }
  .about-text strong { color: #111; }
  .about-info { flex: 1; display: flex; flex-direction: column; gap: 10px; }
  .info-row {
    display: flex; justify-content: space-between; align-items: center;
    background: #f8f8fb; border-radius: 10px; padding: 12px 18px;
    font-size: 13.5px;
  }
  .info-label { color: #999; font-weight: 600; letter-spacing: -.01em; }
  .info-value { color: #222; font-weight: 600; letter-spacing: -.01em; }

  /* ── Skills ───────────────────────────────────────────── */
  .skill-grid { display: flex; flex-direction: column; gap: 18px; }
  .skill-row { display: flex; align-items: center; gap: 20px; }
  .skill-label {
    min-width: 90px; font-size: 13px; color: #999;
    font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
  }
  .skill-tags { display: flex; flex-wrap: wrap; gap: 8px; }
  .tag {
    padding: 6px 16px; border-radius: 20px;
    font-size: 13px; font-weight: 500;
    border: 1.5px solid;
  }
  .tag-purple { background:#f5f3ff; color:#6d28d9; border-color:#e9d5ff; }
  .tag-blue   { background:#eff6ff; color:#1d4ed8; border-color:#bfdbfe; }
  .tag-green  { background:#f0fdf4; color:#15803d; border-color:#bbf7d0; }
  .tag-gray   { background:#f8fafc; color:#475569; border-color:#e2e8f0; }

  /* ── Competency cards ─────────────────────────────────── */
  .comp-grid {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 18px;
  }
  .comp-card {
    background: #fafafa; border: 1.5px solid #f0f0f0;
    border-radius: 16px; padding: 24px;
    transition: transform .15s;
  }
  .comp-card:hover { transform: translateY(-2px); }
  .comp-icon-wrap {
    width: 46px; height: 46px; border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; margin-bottom: 14px;
  }
  .comp-card-title { font-size: 15px; font-weight: 700; color: #111; margin-bottom: 6px; }
  .comp-card-desc  { font-size: 13.5px; color: #888; line-height: 1.65; }

  /* ── Career timeline ──────────────────────────────────── */
  .career-list { display: flex; flex-direction: column; gap: 0; }
  .career-item {
    display: flex; gap: 24px;
    padding: 24px 0; border-bottom: 1px solid #f4f4f4;
  }
  .career-item:last-child { border-bottom: none; }
  .career-dot-col {
    display: flex; flex-direction: column; align-items: center; flex-shrink: 0;
  }
  .career-dot {
    width: 12px; height: 12px; border-radius: 50%; margin-top: 5px;
    background: linear-gradient(135deg, #7c3aed, #a855f7);
    box-shadow: 0 0 0 3px #ede9fe;
  }
  .career-line {
    width: 2px; flex: 1; margin-top: 8px;
    background: linear-gradient(180deg, #e9d5ff, transparent);
  }
  .career-content { flex: 1; }
  .career-period {
    font-size: 12px; font-weight: 600; color: #a78bfa;
    letter-spacing: .04em; text-transform: uppercase; margin-bottom: 6px;
  }
  .career-title { font-size: 17px; font-weight: 700; color: #111; margin-bottom: 4px; }
  .career-sub   { font-size: 13.5px; color: #888; line-height: 1.65; }

  /* ── Contact ──────────────────────────────────────────── */
  .contact-box {
    background: linear-gradient(135deg, #7c3aed, #a855f7);
    border-radius: 20px; padding: 48px 52px;
    color: white; text-align: center;
  }
  .contact-box h3 { font-size: 26px; font-weight: 800; margin-bottom: 10px; letter-spacing: -.03em; }
  .contact-box p  { font-size: 15px; opacity: .8; margin-bottom: 28px; line-height: 1.7; }
  .contact-email {
    display: inline-block; background: rgba(255,255,255,.15);
    border: 1.5px solid rgba(255,255,255,.3);
    color: white; padding: 13px 32px; border-radius: 10px;
    font-size: 14px; font-weight: 600; letter-spacing: -.01em;
  }

  /* ── Footer ───────────────────────────────────────────── */
  .footer {
    border-top: 1px solid #f0f0f0;
    padding: 28px 0; text-align: center;
    font-size: 13px; color: #bbb; letter-spacing: -.01em;
  }
</style>
""", unsafe_allow_html=True)

# ── Navbar ────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
  <div class="nav-logo">황인욱<span>.kr</span></div>
  <div class="nav-links">
    <a href="#">소개</a>
    <a href="#">역량</a>
    <a href="#">경력</a>
    <a href="#">연락처</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="page">
  <div class="hero-wrap">
    <div class="hero-left">
      <div class="hero-eyebrow">안녕하세요, 저는</div>
      <div class="hero-name">황인욱</div>
      <div class="hero-role">Manager · 송변전시스템부</div>
      <div class="hero-desc">
        한전KDN 송변전시스템부에서 변전운영분야 시스템 운영을 담당하고 있습니다.<br>
        전력 데이터 기반의 의사결정과 AI 기술 활용에 관심이 많으며,
        업무 효율화를 위한 솔루션을 개발·적용하고 있습니다.
      </div>
      <div class="hero-btns">
        <div class="btn-primary">📋 프로필 보기</div>
        <div class="btn-secondary">✉️ 연락하기</div>
      </div>
    </div>
    <div class="hero-right">
      <div class="orb"></div>
    </div>
  </div>
  <hr class="divider">
""", unsafe_allow_html=True)

# ── 소개 ──────────────────────────────────────────────────────
st.markdown("""
  <div class="section">
    <div class="sec-title">소개</div>
    <div class="about-wrap">
      <div class="about-text">
        <p>
          한전KDN 송변전시스템부에서 <strong>변전운영분야 IT 시스템 운영</strong>을 담당하고 있는
          황인욱입니다.
        </p>
        <p>
          전력 시스템의 안정적 운영과 디지털 전환을 위해 데이터 분석, AI 기술 활용,
          업무 자동화 솔루션 개발 등 다양한 분야에서 역량을 발휘하고 있습니다.
        </p>
        <p>
          변전운영 시스템의 신뢰성 향상과 운영 효율화를 목표로,
          현장의 목소리를 IT 시스템에 반영하는 데 중점을 두고 있습니다.
        </p>
      </div>
      <div class="about-info">
        <div class="info-row"><span class="info-label">소속</span><span class="info-value">한전KDN</span></div>
        <div class="info-row"><span class="info-label">부서</span><span class="info-value">송변전시스템부</span></div>
        <div class="info-row"><span class="info-label">직위</span><span class="info-value">Manager</span></div>
        <div class="info-row"><span class="info-label">분야</span><span class="info-value">변전운영 시스템</span></div>
        <div class="info-row"><span class="info-label">이메일</span><span class="info-value">xxxx@kdn.com</span></div>
      </div>
    </div>
  </div>
  <hr class="divider">
""", unsafe_allow_html=True)

# ── 기술 스택 ─────────────────────────────────────────────────
st.markdown("""
  <div class="section">
    <div class="sec-title">기술 스택</div>
    <div class="skill-grid">
      <div class="skill-row">
        <span class="skill-label">전력 시스템</span>
        <div class="skill-tags">
          <span class="tag tag-purple">송변전 시스템</span>
          <span class="tag tag-purple">전력망 관리</span>
          <span class="tag tag-purple">EMS/SCADA</span>
          <span class="tag tag-purple">변전운영</span>
        </div>
      </div>
      <div class="skill-row">
        <span class="skill-label">프로그래밍</span>
        <div class="skill-tags">
          <span class="tag tag-blue">Python</span>
          <span class="tag tag-blue">SQL</span>
          <span class="tag tag-blue">Streamlit</span>
        </div>
      </div>
      <div class="skill-row">
        <span class="skill-label">데이터 분석</span>
        <div class="skill-tags">
          <span class="tag tag-green">데이터 분석</span>
          <span class="tag tag-green">AI 활용</span>
          <span class="tag tag-green">대시보드</span>
        </div>
      </div>
      <div class="skill-row">
        <span class="skill-label">업무 도구</span>
        <div class="skill-tags">
          <span class="tag tag-gray">프로젝트 관리</span>
          <span class="tag tag-gray">MS Office</span>
        </div>
      </div>
    </div>
  </div>
  <hr class="divider">
""", unsafe_allow_html=True)

# ── 주요 역량 ─────────────────────────────────────────────────
st.markdown("""
  <div class="section">
    <div class="sec-title">주요 역량</div>
    <div class="comp-grid">
      <div class="comp-card">
        <div class="comp-icon-wrap" style="background:#fef3c7;">⚡</div>
        <div class="comp-card-title">전력 시스템 관리</div>
        <div class="comp-card-desc">송변전 설비 및 전력망 IT 시스템의 안정적 운영·관리</div>
      </div>
      <div class="comp-card">
        <div class="comp-icon-wrap" style="background:#eff6ff;">📊</div>
        <div class="comp-card-title">데이터 분석</div>
        <div class="comp-card-desc">전력 데이터 분석 및 AI 기반 인사이트 도출</div>
      </div>
      <div class="comp-card">
        <div class="comp-icon-wrap" style="background:#f0fdf4;">💻</div>
        <div class="comp-card-title">시스템 개발</div>
        <div class="comp-card-desc">업무 자동화 및 데이터 시각화 솔루션 개발</div>
      </div>
      <div class="comp-card">
        <div class="comp-icon-wrap" style="background:#faf5ff;">🤝</div>
        <div class="comp-card-title">프로젝트 리딩</div>
        <div class="comp-card-desc">IT 시스템 구축 프로젝트 기획 및 관리</div>
      </div>
    </div>
  </div>
  <hr class="divider">
""", unsafe_allow_html=True)

# ── 경력 ──────────────────────────────────────────────────────
st.markdown("""
  <div class="section">
    <div class="sec-title">경력 사항</div>
    <div class="career-list">
      <div class="career-item">
        <div class="career-dot-col">
          <div class="career-dot"></div>
          <div class="career-line"></div>
        </div>
        <div class="career-content">
          <div class="career-period">현재 재직 중</div>
          <div class="career-title">한전KDN · 송변전시스템부</div>
          <div class="career-sub">변전운영분야 시스템 운영 및 디지털 전환 업무 담당</div>
        </div>
      </div>
    </div>
  </div>
  <hr class="divider">
""", unsafe_allow_html=True)

# ── 연락처 ────────────────────────────────────────────────────
st.markdown("""
  <div class="section">
    <div class="contact-box">
      <h3>🐯 함께 일해요</h3>
      <p>전력 시스템 IT, 데이터 분석, 업무 자동화에 관심이 있으시다면<br>언제든지 연락 주세요.</p>
      <div class="contact-email">✉️ &nbsp; xxxx@kdn.com</div>
    </div>
  </div>

  <div class="footer">
    © 2026 &nbsp;황인욱 &nbsp;·&nbsp; 한전KDN 송변전시스템부
  </div>
</div>
""", unsafe_allow_html=True)
