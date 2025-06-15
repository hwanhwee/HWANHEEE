from PIL import Image
import os

def optimize_gif(input_path, output_path, max_size=(800, 600)):
    """
    GIF 파일을 최적화하는 함수
    :param input_path: 입력 GIF 경로
    :param output_path: 출력 GIF 경로
    :param max_size: 최대 이미지 크기 (너비, 높이)
    """
    try:
        # GIF 열기
        gif = Image.open(input_path)
        
        # 출력 디렉토리가 없으면 생성
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 각 프레임 최적화
        frames = []
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_img = gif.copy()
            frame_img.thumbnail(max_size, Image.Resampling.LANCZOS)
            frames.append(frame_img)
        
        # 최적화된 GIF 저장
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=gif.info.get('duration', 100),
            loop=0
        )
        
        print(f"GIF 최적화 완료: {output_path}")
        print(f"원본 크기: {os.path.getsize(input_path) / 1024 / 1024:.2f}MB")
        print(f"최적화 크기: {os.path.getsize(output_path) / 1024 / 1024:.2f}MB")
        
    except Exception as e:
        print(f"GIF 오류 발생: {input_path} - {str(e)}")

def optimize_image(input_path, output_path, max_size=(1920, 1080), quality=85):
    """
    이미지를 최적화하는 함수
    :param input_path: 입력 이미지 경로
    :param output_path: 출력 이미지 경로
    :param max_size: 최대 이미지 크기 (너비, 높이)
    :param quality: JPEG 품질 (1-100)
    """
    try:
        # 이미지 열기
        img = Image.open(input_path)
        
        # 이미지 크기 조정 (비율 유지)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # 출력 디렉토리가 없으면 생성
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 이미지 저장
        if input_path.lower().endswith('.png'):
            img.save(output_path, 'PNG', optimize=True)
        else:
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
        print(f"최적화 완료: {output_path}")
        print(f"원본 크기: {os.path.getsize(input_path) / 1024 / 1024:.2f}MB")
        print(f"최적화 크기: {os.path.getsize(output_path) / 1024 / 1024:.2f}MB")
        
    except Exception as e:
        print(f"오류 발생: {input_path} - {str(e)}")

def main():
    # 입력 및 출력 경로 설정
    input_dir = "../11주차"
    output_dir = "static/images"
    
    # 최적화할 이미지 목록
    images = [
        ("project_gif.gif", "project_gif.gif"),
        ("compact house project_thumbnail.PNG", "compact_house_thumbnail.PNG"),
        ("compact house_Panorama.jpg", "compact_house_Panorama.jpg"),
        ("floor plans.PNG", "floor_plans.PNG"),
        ("3D sections.PNG", "3D_sections.PNG")
    ]
    
    # 각 이미지 최적화
    for input_name, output_name in images:
        input_path = os.path.join(input_dir, input_name)
        output_path = os.path.join(output_dir, output_name)
        
        if os.path.exists(input_path):
            if input_name.lower().endswith('.gif'):
                optimize_gif(input_path, output_path)
            else:
                optimize_image(input_path, output_path)
        else:
            print(f"파일을 찾을 수 없음: {input_path}")

if __name__ == "__main__":
    main() 