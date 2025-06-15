import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="3D 뷰어 - 조환희 포트폴리오",
    page_icon="🏠",
    layout="wide"
)

st.title("3D 모델 갤러리")

# 갤러리 섹션
st.header("Walk-through 모드")
st.image("static/images/project_gif.gif", caption="Walk-through 모드")

# 이미지 갤러리
st.header("갤러리")
col1, col2 = st.columns(2)
with col1:
    st.image("static/images/compact_house_thumbnail.PNG", caption="전체 뷰")
with col2:
    st.image("static/images/compact_house_Panorama.jpg", caption="파노라마 뷰")

# 추가 섹션
st.header("평면도 및 단면도")
col3, col4 = st.columns(2)
with col3:
    st.image("static/images/floor_plans.PNG", caption="평면도")
with col4:
    st.image("static/images/3D_sections.PNG", caption="3D 단면도")

# 설명
st.markdown("""
### 프로젝트 설명
이 프로젝트는 2학년 실내건축스튜디오에서 진행한 작품입니다.
Walk-through 모드와 갤러리를 통해 공간을 다양한 관점에서 탐색할 수 있습니다.

### 사용된 기술
- 3D 모델링: SketchUp
- 렌더링: V-Ray
- 애니메이션: Blender
""") 