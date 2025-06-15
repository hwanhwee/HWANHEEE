import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="3D 뷰어 - 조환희 포트폴리오",
    page_icon="🏠",
    layout="wide"
)

def main():
    st.title("3D 뷰어")
    
    # 뷰어 모드 선택
    viewer_mode = st.radio(
        "뷰어 모드 선택",
        ["X-ray 뷰어", "워크스루 뷰어"],
        horizontal=True
    )
    
    if viewer_mode == "X-ray 뷰어":
        st.markdown("""
        ### X-ray 뷰어
        건물의 내부 구조를 투시할 수 있는 X-ray 뷰어입니다.
        
        #### 조작 방법
        - 마우스 왼쪽 버튼: 회전
        - 마우스 오른쪽 버튼: 이동
        - 마우스 휠: 확대/축소
        """)
        
        # Sketchfab 모델 임베드
        st.markdown("### 3D 모델 뷰어")
        components.iframe(
            "https://sketchfab.com/models/01097ceec47c46b9b0545e99ecd2817a/embed",
            height=600,
            scrolling=False
        )
        
    else:  # 워크스루 뷰어
        st.markdown("""
        ### 워크스루 뷰어
        건물 내부를 자유롭게 탐색할 수 있는 워크스루 뷰어입니다.
        
        #### 조작 방법
        - W, A, S, D: 이동
        - 마우스: 시점 변경
        - Shift: 달리기
        - Space: 점프
        """)
        
        # 워크스루 GIF
        st.markdown("### 워크스루 시연")
        st.image("static/images/워크스루영상(1).gif", caption="워크스루 시연 영상")

if __name__ == "__main__":
    main() 