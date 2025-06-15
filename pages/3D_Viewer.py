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
        
        # X-ray 뷰어 컴포넌트
        components.html("""
        <div id="xray-viewer" style="width: 100%; height: 600px;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
        <script>
            // Three.js 초기화
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(document.getElementById('xray-viewer').offsetWidth, 600);
            document.getElementById('xray-viewer').appendChild(renderer.domElement);

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
                camera.aspect = document.getElementById('xray-viewer').offsetWidth / 600;
                camera.updateProjectionMatrix();
                renderer.setSize(document.getElementById('xray-viewer').offsetWidth, 600);
            }
        </script>
        """, height=600)
        
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
        
        # 워크스루 뷰어 컴포넌트
        components.html("""
        <div id="walkthrough-viewer" style="width: 100%; height: 600px;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/FirstPersonControls.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
        <script>
            // Three.js 초기화
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(document.getElementById('walkthrough-viewer').offsetWidth, 600);
            document.getElementById('walkthrough-viewer').appendChild(renderer.domElement);

            // 조명 설정
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
            directionalLight.position.set(0, 1, 0);
            scene.add(directionalLight);

            // 컨트롤 설정
            const controls = new THREE.FirstPersonControls(camera, renderer.domElement);
            controls.movementSpeed = 10;
            controls.lookSpeed = 0.1;

            // 카메라 위치 설정
            camera.position.set(0, 1.6, 0);  // 사람의 눈 높이

            // 애니메이션 루프
            function animate() {
                requestAnimationFrame(animate);
                controls.update(0.1);
                renderer.render(scene, camera);
            }
            animate();

            // 창 크기 조절 대응
            window.addEventListener('resize', onWindowResize, false);
            function onWindowResize() {
                camera.aspect = document.getElementById('walkthrough-viewer').offsetWidth / 600;
                camera.updateProjectionMatrix();
                renderer.setSize(document.getElementById('walkthrough-viewer').offsetWidth, 600);
            }
        </script>
        """, height=600)
    
    # 워크스루 GIF
    st.markdown("### 워크스루 시연")
    st.image("static/images/워크스루영상(1).gif", caption="워크스루 시연 영상")

if __name__ == "__main__":
    main() 