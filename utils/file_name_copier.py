from pathlib import Path


def copy_file_names(prev_path: Path, new_path: Path) -> None:
    # 이전 폴더에 있는 모든 파일 가져옴
    files = prev_path.glob('*')

    for file in files:
        # 폴더만 새로운 곳으로 하고, 같은 이름의 파일 경로 얻음
        new_file = new_path / file.name
        # 파일이 이미 존재하면 넘어감
        if new_file.exists():
            continue
        # 파일 생성
        new_file.touch()


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    prev_path = root / "problems/This_is_coding_test/1_X"
    new_path = root / "problems/This_is_coding_test/2_X"

    copy_file_names(prev_path, new_path)
