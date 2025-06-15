import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="프로젝트 - 조환희 포트폴리오",
    page_icon="🏠",
    layout="wide"
)

st.title("프로젝트 상세")

# 프로젝트 선택
project = st.selectbox(
    "프로젝트 선택",
    ["실내건축스튜디오(1)-2학년", "실내건축스튜디오(2)-3학년", "실내건축스튜디오(3)-4학년"]
)

if project == "실내건축스튜디오(1)-2학년":
    st.header("실내건축스튜디오(1)-2학년")
    
    # 프로젝트 설명
    st.write("""
    ### 프로젝트 개요
    이 프로젝트는 2학년 실내건축스튜디오에서 진행한 작품입니다.
    X-RAY 뷰어와 Walk-through 모드를 통해 공간을 다양한 관점에서 탐색할 수 있습니다.
    """)
    
    # 이미지 갤러리
    st.subheader("갤러리")
    cols = st.columns(3)
    with cols[0]:
        st.image("static/images/compact_house_thumbnail.PNG", caption="전체 뷰")
    with cols[1]:
        st.image("static/images/project_gif.gif", caption="Walk-through 모드")
    with cols[2]:
        st.image("static/images/xray_view.png", caption="X-RAY 뷰")
    
    # 3D 뷰어 링크
    st.subheader("3D 뷰어")
    st.write("아래 버튼을 클릭하여 3D 뷰어를 실행하세요.")
    if st.button("3D 뷰어 실행"):
        st.switch_page("pages/3D_Viewer.py")

elif project == "실내건축스튜디오(2)-3학년":
    st.header("실내건축스튜디오(2)-3학년")
    st.write("준비 중입니다...")

elif project == "실내건축스튜디오(3)-4학년":
    st.header("실내건축스튜디오(3)-4학년")
    st.write("준비 중입니다...") 