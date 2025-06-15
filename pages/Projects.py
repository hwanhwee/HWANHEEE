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
    st.image("static/images/compact_house_thumbnail.PNG", caption="컴팩트 하우스 프로젝트")
    
    # X-ray 뷰어
    st.markdown("### X-ray 뷰어")
    st.markdown("""
    X-ray 뷰어를 통해 건물의 내부 구조를 투시할 수 있습니다.
    - 마우스 왼쪽 버튼: 회전
    - 마우스 오른쪽 버튼: 이동
    - 마우스 휠: 확대/축소
    """)
    
    # 3D 모델 뷰어
    components.html("""
    <div id="viewer-container" style="width: 100%; height: 600px;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
    <script>
        // Three.js 초기화
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(document.getElementById('viewer-container').offsetWidth, 600);
        document.getElementById('viewer-container').appendChild(renderer.domElement);

        // 조명 설정
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
        directionalLight.position.set(0, 1, 0);
        scene.add(directionalLight);

        // 컨트롤 설정
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;

        // 카메라 위치 설정
        camera.position.z = 5;

        // 애니메이션 루프
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // 창 크기 조절 대응
        window.addEventListener('resize', onWindowResize, false);
        function onWindowResize() {
            camera.aspect = document.getElementById('viewer-container').offsetWidth / 600;
            camera.updateProjectionMatrix();
            renderer.setSize(document.getElementById('viewer-container').offsetWidth, 600);
        }
    </script>
    """, height=600)
    
    # 워크스루 뷰어
    st.markdown("### 워크스루 뷰어")
    st.markdown("""
    워크스루 뷰어를 통해 건물 내부를 자유롭게 탐색할 수 있습니다.
    - W, A, S, D: 이동
    - 마우스: 시점 변경
    - Shift: 달리기
    - Space: 점프
    """)
    
    # 워크스루 GIF
    st.image("static/images/워크스루영상(1).gif", caption="워크스루 시연")
    
    # 파노라마 뷰어
    st.markdown("### 360° 파노라마 뷰어")
    components.html("""
    <div id="panorama-viewer" style="width: 100%; height: 500px;"></div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css"/>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js"></script>
    <script>
        pannellum.viewer('panorama-viewer', {
            type: 'equirectangular',
            panorama: 'static/images/compact_house_Panorama.jpg',
            autoLoad: true,
            autoRotate: -2,
            compass: true
        });
    </script>
    """, height=500)
    
    # 프로젝트 설명
    st.markdown("""
    ### 프로젝트 설명
    이 프로젝트는 기존 주택을 리모델링하여 더 효율적이고 현대적인 공간을 만드는 것을 목표로 합니다.
    
    #### 주요 특징
    - X-ray 뷰어를 통한 구조 분석
    - 워크스루 기능으로 공간 체험
    - 360° 파노라마 뷰어로 전체 공간 감상
    """)

if __name__ == "__main__":
    main() 