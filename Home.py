import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="조환희 디지털 포트폴리오",
    page_icon="🏠",
    layout="wide"
)

# 사이드바 메뉴
with st.sidebar:
    selected = option_menu(
        menu_title="메뉴",
        options=["홈", "프로젝트", "3D 뷰어", "연락처"],
        icons=["house", "folder", "cube", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# 홈 페이지
if selected == "홈":
    st.title("조환희 디지털 포트폴리오")
    st.subheader("연세대학교 생활과학대학 실내건축학전공")
    
    # 소개 섹션
    st.write("""
    ### 안녕하세요, 실내건축학을 전공한 조환희입니다.
    이 포트폴리오는 제가 학부에서 진행한 다양한 프로젝트와 작품들을 소개합니다.
    """)
    
    # 주요 프로젝트 섹션
    st.header("주요 프로젝트")
    projects = [
        {
            "title": "실내건축스튜디오(1)-2학년",
            "description": "X-RAY 뷰어 & Walk-through 모드",
            "image": "static/images/compact_house_thumbnail.PNG"
        },
        {
            "title": "실내건축스튜디오(2)-3학년",
            "description": "공간 설계 프로젝트",
            "image": "static/images/exhibition2_thumbnail.jpg"
        },
        {
            "title": "실내건축스튜디오(3)-4학년",
            "description": "졸업 작품",
            "image": "static/images/exhibition3_thumbnail.jpg"
        }
    ]
    
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        with cols[idx]:
            st.image(project["image"], caption=project["title"])
            st.write(f"**{project['title']}**")
            st.write(project["description"])

# 프로젝트 페이지
elif selected == "프로젝트":
    st.title("프로젝트")
    # 프로젝트 상세 내용 추가 예정

# 3D 뷰어 페이지
elif selected == "3D 뷰어":
    st.title("3D 모델 뷰어")
    st.write("3D 모델을 로드하는 중...")
    # Three.js 통합 예정

# 연락처 페이지
elif selected == "연락처":
    st.title("연락처")
    st.write("""
    ### 연락처 정보
    - **이메일**: happyi0305@yonsei.ac.kr
    - **전화번호**: 010-1234-5678
    - **위치**: 서울시 서대문구 연세로 50, 연세대학교 325동(삼성관) 110호 생활과학대학 실내건축학과 사무실
    """) 