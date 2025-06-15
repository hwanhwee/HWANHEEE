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
            try:
                st.image(project["image"], caption=project["title"])
            except:
                st.write("이미지 준비 중...")
            st.write(f"**{project['title']}**")
            st.write(project["description"])

# 프로젝트 페이지
elif selected == "프로젝트":
    st.title("프로젝트 상세")
    
    # 프로젝트 1
    st.header("실내건축스튜디오(1)-2학년")
    st.write("""
    ### X-RAY 뷰어 & Walk-through 모드
    이 프로젝트는 실내 공간의 구조를 이해하고 시각화하는 도구를 개발했습니다.
    
    #### 주요 기능
    - X-RAY 뷰어: 벽을 투과하여 공간 구조를 볼 수 있는 기능
    - Walk-through 모드: 실제 공간을 걷는 것처럼 체험할 수 있는 기능
    
    #### 사용 기술
    - Three.js
    - WebGL
    - JavaScript
    """)
    
    # 프로젝트 2
    st.header("실내건축스튜디오(2)-3학년")
    st.write("""
    ### 공간 설계 프로젝트
    다양한 공간의 특성을 고려한 설계 프로젝트입니다.
    
    #### 주요 내용
    - 공간 분석
    - 사용자 행동 패턴 연구
    - 공간 구성 및 배치
    - 재료 및 색채 계획
    
    #### 결과물
    - 평면도
    - 입면도
    - 단면도
    - 3D 렌더링
    """)
    
    # 프로젝트 3
    st.header("실내건축스튜디오(3)-4학년")
    st.write("""
    ### 졸업 작품
    학부 과정의 마지막 프로젝트로, 지금까지 배운 모든 것을 종합한 작품입니다.
    
    #### 주제
    - 현대 사회의 문제점을 해결하는 공간 설계
    - 지속가능한 디자인
    - 사용자 중심 공간 구성
    
    #### 특징
    - 혁신적인 공간 구성
    - 친환경 소재 사용
    - 사용자 경험 최적화
    """)

# 3D 뷰어 페이지
elif selected == "3D 뷰어":
    st.title("3D 모델 갤러리")
    
    # Sketchfab 임베드
    st.write("""
    ### 프로젝트 3D 모델
    아래 3D 모델을 마우스로 회전하고 확대/축소하여 살펴볼 수 있습니다.
    """)
    
    # Sketchfab iframe
    st.components.v1.iframe(
        "https://sketchfab.com/3d-models/model-colored-e1367b99316e4c3fa0ce5737abd648bf/embed",
        height=600,
        scrolling=False
    )
    
    st.write("""
    #### 사용 방법
    1. 마우스 왼쪽 버튼 드래그: 모델 회전
    2. 마우스 휠: 확대/축소
    3. 마우스 오른쪽 버튼 드래그: 이동
    4. 더블 클릭: 초기화
    
    #### 지원 형식
    - GLB
    - GLTF
    - OBJ
    """)

# 연락처 페이지
elif selected == "연락처":
    st.title("연락처")
    st.write("""
    ### 연락처 정보
    - **이메일**: happyi0305@yonsei.ac.kr
    - **전화번호**: 010-1234-5678
    - **위치**: 서울시 서대문구 연세로 50, 연세대학교 325동(삼성관) 110호 생활과학대학 실내건축학과 사무실
    """) 