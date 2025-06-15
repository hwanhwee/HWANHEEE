import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Projects - 조환희 포트폴리오",
    page_icon="🏠",
    layout="wide"
)

def load_css():
    with open("static/css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.title("프로젝트")
    
    # 프로젝트 소개
    st.markdown("""
    ### 실내건축스튜디오(1) - 2학년
    컴팩트 하우스 리모델링 프로젝트
    """)
    
    # 프로젝트 이미지
    try:
        st.image("static/images/compact_house_thumbnail.PNG", 
                caption="컴팩트 하우스 프로젝트",
                use_container_width=True)
    except Exception as e:
        st.error(f"썸네일 이미지를 불러올 수 없습니다: {str(e)}")
    
    # 도면 및 섹션
    st.markdown("### 도면 및 섹션")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 평면도")
        try:
            st.image("static/images/floor_plans.PNG",
                    caption="평면도",
                    use_container_width=True)
        except Exception as e:
            st.error(f"평면도 이미지를 불러올 수 없습니다: {str(e)}")
    
    with col2:
        st.markdown("#### 입면도")
        try:
            st.image("static/images/3D_sections.PNG",
                    caption="입면도",
                    use_container_width=True)
        except Exception as e:
            st.error(f"입면도 이미지를 불러올 수 없습니다: {str(e)}")
    
    # 3D 섹션
    st.markdown("#### 3D 섹션")
    try:
        st.image("static/images/3D_sections.PNG",
                caption="3D 섹션",
                use_container_width=True)
    except Exception as e:
        st.error(f"3D 섹션 이미지를 불러올 수 없습니다: {str(e)}")
    
    # 프로젝트 설명
    st.markdown("""
    ### 프로젝트 설명
    이 프로젝트는 기존 주택을 리모델링하여 더 효율적이고 현대적인 공간을 만드는 것을 목표로 합니다.
    
    #### 주요 특징
    - 효율적인 공간 활용
    - 현대적인 디자인 요소
    - 자연 채광 최적화
    - 유동적인 공간 구성
    """)

if __name__ == "__main__":
    main() 