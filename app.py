import streamlit as st

st.set_page_config(
    page_title="황인욱 | Profile",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, footer, header {visibility: hidden;}
  section[data-testid="stSidebar"] {display: none;}
  .block-container {padding: 2rem 3rem;}

  .hero {
    background: linear-gradient(135deg, #1a237e 0%, #1565c0 60%, #0288d1 100%);
    padding: 52px 44px;
    border-radius: 20px;
    color: white;
    margin-bottom: 28px;
  }
  .avatar {
    width: 96px; height: 96px; border-radius: 50%;
    background: rgba(255,255,255,0.18);
    display: flex; align-items: center; justify-content: center;
    font-size: 44px; flex-shrink: 0;
    border: 3px solid rgba(255,255,255,0.35);
  }
  .card {
    background: white;
    border-radius: 14px;
    padding: 26px 28px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 22px;
  }
  .section-title {
    font-size: 16px; font-weight: 700; color: #1e293b;
    margin-bottom: 18px; padding-bottom: 10px;
    border-bottom: 2px solid #3b82f6;
  }
  .info-row {
    display: flex; justify-content: space-between;
    padding: 9px 0; border-bottom: 1px solid #f1f5f9; font-size: 14px;
  }
  .info-row:last-child {border-bottom: none;}
  .skill-tag {
    display: inline-block; background: #eff6ff; color: #1d4ed8;
    padding: 4px 13px; border-radius: 20px; font-size: 12.5px;
    font-weight: 500; margin: 3px 3px 3px 0; border: 1px solid #bfdbfe;
  }
  .skill-cat {
    font-size: 11px; color: #94a3b8; font-weight: 700;
    text-transform: uppercase; letter-spacing: .07em; margin: 14px 0 7px;
  }
  .comp-item {
    display: flex; gap: 14px; align-items: flex-start;
    padding: 13px 0; border-bottom: 1px solid #f8fafc;
  }
  .comp-item:last-child {border-bottom: none;}
  .comp-icon {
    width: 42px; height: 42px; border-radius: 11px; background: #eff6ff;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
  }
  .timeline-item {
    display: flex; gap: 18px; align-items: flex-start;
    padding: 14px 0; border-bottom: 1px solid #f1f5f9; flex-wrap: wrap;
  }
  .timeline-item:last-child {border-bottom: none;}
  .badge {
    font-size: 11.5px; color: #6366f1; font-weight: 600;
    background: #eff6ff; padding: 3px 12px; border-radius: 20px;
    flex-shrink: 0; text-align: center; min-width: 64px;
    border: 1px solid #c7d2fe;
  }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div style="display:flex;align-items:center;gap:32px;flex-wrap:wrap;">
    <div class="avatar">👤</div>
    <div>
      <div style="font-size:12.5px;font-weight:600;opacity:.75;letter-spacing:.12em;
                  text-transform:uppercase;margin-bottom:8px;">
        한전KDN &nbsp;·&nbsp; 송변전시스템부
      </div>
      <div style="font-size:42px;font-weight:800;line-height:1.1;margin-bottom:10px;">
        황인욱
      </div>
      <div style="font-size:17px;opacity:.88;font-weight:400;">
        과장 &nbsp;/&nbsp; Manager
      </div>
      <div style="font-size:14px;opacity:.7;margin-top:10px;font-weight:400;">
        💡 변전운영분야 시스템 운영
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Two-column layout ─────────────────────────────────────────
left, right = st.columns([2, 3], gap="large")

# ── LEFT ─────────────────────────────────────────────────────
with left:
    # 기본 정보
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 기본 정보</div>', unsafe_allow_html=True)
    rows = [
        ("🏢 소속",   "한전KDN"),
        ("🏬 부서",   "송변전시스템부"),
        ("💼 직위",   "과장"),
        ("📍 위치",   "대한민국"),
        ("📧 이메일", "xxxx@kdn.com"),
    ]
    for label, value in rows:
        st.markdown(f"""
        <div class="info-row">
          <span style="color:#64748b;">{label}</span>
          <span style="color:#1e293b;font-weight:500;">{value}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 보유 기술
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🛠 보유 기술</div>', unsafe_allow_html=True)
    skill_groups = {
        "전력 시스템": ["송변전 시스템", "전력망 관리", "EMS/SCADA"],
        "프로그래밍":  ["Python", "SQL", "Streamlit"],
        "데이터 분석": ["데이터 분석", "AI 활용", "대시보드"],
        "업무 도구":   ["프로젝트 관리", "MS Office"],
    }
    for cat, tags in skill_groups.items():
        st.markdown(f'<div class="skill-cat">{cat}</div>', unsafe_allow_html=True)
        st.markdown("".join(f'<span class="skill-tag">{t}</span>' for t in tags),
                    unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── RIGHT ────────────────────────────────────────────────────
with right:
    # 소개
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">👋 소개</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="line-height:1.85;color:#374151;font-size:15px;">
      안녕하세요, 한전KDN 송변전시스템부에서 근무하고 있는
      <strong>황인욱 과장</strong>입니다.
    </p>
    <p style="line-height:1.85;color:#374151;font-size:15px;margin-top:14px;">
      전력 시스템 IT 분야에서의 전문성을 바탕으로 송변전 시스템의 안정적인 운영과
      디지털 전환을 위한 업무를 담당하고 있습니다.
      데이터 기반의 의사결정과 AI 기술 활용에 관심이 많으며,
      업무 효율화를 위한 다양한 솔루션을 개발·적용하고 있습니다.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 주요 역량
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">⭐ 주요 역량</div>', unsafe_allow_html=True)
    competencies = [
        ("⚡", "전력 시스템 관리",  "송변전 설비 및 전력망 IT 시스템 운영·관리"),
        ("📊", "데이터 분석",       "전력 데이터 분석 및 AI 기반 인사이트 도출"),
        ("💻", "시스템 개발",       "업무 자동화 및 데이터 시각화 솔루션 개발"),
        ("🤝", "프로젝트 리딩",     "IT 시스템 구축 프로젝트 기획 및 관리"),
    ]
    for icon, title, desc in competencies:
        st.markdown(f"""
        <div class="comp-item">
          <div class="comp-icon">{icon}</div>
          <div>
            <div style="font-weight:600;color:#1e293b;font-size:14px;margin-bottom:3px;">{title}</div>
            <div style="color:#64748b;font-size:13px;line-height:1.6;">{desc}</div>
          </div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── 경력 사항 ─────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📌 경력 사항</div>', unsafe_allow_html=True)
careers = [
    ("현재", "한전KDN · 송변전시스템부 과장",
     "송변전 IT 시스템 운영 및 디지털 전환 업무 담당"),
]
for period, title, desc in careers:
    st.markdown(f"""
    <div class="timeline-item">
      <div class="badge">{period}</div>
      <div>
        <div style="font-weight:600;color:#1e293b;font-size:15px;margin-bottom:4px;">{title}</div>
        <div style="color:#64748b;font-size:13px;line-height:1.6;">{desc}</div>
      </div>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:28px 0 12px;color:#94a3b8;font-size:13px;">
  © 2026 황인욱 &nbsp;·&nbsp; 한전KDN 송변전시스템부
</div>
""", unsafe_allow_html=True)
