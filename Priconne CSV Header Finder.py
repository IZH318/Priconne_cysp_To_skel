# 파일 및 디렉토리 작업 관련
import os  # 운영 체제와 상호작용을 위한 모듈 (파일 경로, 환경 변수 등)
import shutil  # 고수준의 파일 및 디렉토리 작업을 위한 모듈 (파일 복사, 이동 등)

# 프로그램 시작 시 출력
print("\n ===== Welcome to Priconne CSV Header Finder =====")
print(" A tool to search and copy CSV files for Princess Connect! Re: Dive based on specific headers.\n\n")

def find_files_with_strings_in_content(directory, *search_strings):
    """
    주어진 디렉토리에서 'v1_'로 시작하고 .csv 확장자를 가진 파일을 대상으로
    주어진 문자열들이 파일 내용에 모두 포함된 파일을 찾습니다.
    
    :param directory: 검색할 디렉토리 경로
    :param search_strings: 포함되어야 할 문자열들
    :return: 조건을 만족하는 .csv 파일 이름 리스트
    """

    matching_files = []

    # 디렉토리 내의 모든 파일을 탐색
    for root, _, files in os.walk(directory):
        for file in files:
            # 파일이 'v1_'로 시작하고 .csv 확장자인지 확인
            if file.startswith('v1_') and file.endswith('.csv'):
                file_path = os.path.join(root, file)
                
                try:
                    # .csv 파일을 열어서 내용 검색
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if all(s in content for s in search_strings):
                            matching_files.append(file_path)
                            
                except (UnicodeDecodeError, FileNotFoundError):
                    # 파일이 텍스트 파일이 아니거나 열 수 없는 경우 예외 처리
                    continue

    return matching_files

def get_new_file_name(file_path):
    """
    이미 파일이 존재하면 파일 이름에 _숫자 추가하여 새로운 파일 이름을 생성합니다.
    
    :param file_path: 기존 파일 경로
    :return: 새로운 파일 경로
    """
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    
    while os.path.exists(new_file_path):
        # 파일 이름에 _숫자 추가
        new_file_path = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_file_path

def copy_files(files, new_name, overwrite_choice=None):
    """
    주어진 파일을 새로운 이름으로 복사합니다.
    
    :param files: 복사할 파일 목록
    :param new_name: 복사본의 새 파일 이름
    :param overwrite_choice: 이미 파일이 존재할 경우 덮어쓸지 여부(True/False) 또는 None
    """
    for file in files:
        try:
            new_file_path = os.path.join('.', new_name)

            # 파일이 이미 존재하는 경우 덮어쓰기 여부 결정
            if os.path.exists(new_file_path):
                if overwrite_choice is None:
                    # 사용자가 덮어쓰기/이름에 숫자 추가 선택을 하지 않은 경우, 스킵
                    print(f"\n [Info] File '{new_name}' already exists. Do you want to overwrite it or add a number to the name?")
                    
                elif overwrite_choice:
                    # 덮어쓸 경우
                    shutil.copy(file, new_file_path)
                    print(f"\n [Info] File '{new_name}' has been overwritten.")
                    
                else:
                    # 이름에 숫자 추가
                    new_file_path = get_new_file_name(new_file_path)
                    shutil.copy(file, new_file_path)
                    print(f"\n [Info] A copy of '{new_name}' has been created: {new_file_path}")
            else:
                # 파일이 존재하지 않으면 복사
                shutil.copy(file, new_file_path)
                print(f"\n [Info] File '{new_name}' has been copied.")
                
        except Exception as e:
            print(f"\n [Error] An error occurred while copying the file: {e}")

# Character
Search_Character_Header = [
    '63b62d72f43f1ee9d3ffa6528fd788c4c05ab9bf3be4046fa0c670308ffda877',
    '758a833b38682617eb99c0e50e138a1e08008740c69a2a1e1fe3eaa6e913f894',
    '556944d17c3dccfdac0aa708e6e713008a0ed10956c307cca8a49dffa26d09a8'
]

# Boss
Search_Boss_Header = [
    '5f6902a3cabd407a699ecbadbce41011b4703d685e80a48d3a51f5c3d44f3b7b',
    '52c55fdb9c4384a8ba7151004585a3dfc2a464c71a3dc3d229fd33d6947331cd',
    '42409c8a6a41c132c614b19c7171cc886b6bb65c172e9aec0406d143d4f27672'
]

# Nebbia ID Info
Search_Nebbia_ID_Header= [
    '9e7e08f2eb6ecb3955d4e5488835e791a3d55869d1a7ca49c35f0a079be4771d',
    '2ade35e1ce2dd7a2d3fd37d4adc92149b8054b798f5adc813257047567894f9f'
]

# 현재 디렉토리에서 검색
directory = '.'

# 첫 번째 조건을 만족하는 파일 찾기
Character_Header_Include = find_files_with_strings_in_content(directory, *Search_Character_Header)
if Character_Header_Include:
    print("\n [Info] Files containing Character ID:")
    for file in Character_Header_Include:
        print(f" {file}")
        
else:
    print("\n [Info] Could not find any files containing Character ID.")

# 두 번째 조건을 만족하는 파일 찾기
Boss_Header_Include = find_files_with_strings_in_content(directory, *Search_Boss_Header)
if Boss_Header_Include:
    print("\n [Info] Files containing Boss ID:")
    for file in Boss_Header_Include:
        print(f" {file}")
        
else:
    print("\n [Info] Could not find any files containing Boss ID.")

# 세 번째 조건을 만족하는 파일 찾기
Nebbia_ID_Header_Include = find_files_with_strings_in_content(directory, *Search_Nebbia_ID_Header)
if Nebbia_ID_Header_Include:
    print("\n [Info] Files containing Nebbia ID:")
    for file in Nebbia_ID_Header_Include:
        print(f" {file}")
        
else:
    print("\n [Info] Could not find any files containing Nebbia ID.")

# 파일 복사 여부 묻기
def prompt_copy_all_files():
    while True:
        user_input = input("\n\n\n [Info] Do you want to create copies of all the files? ([Y]: Yes, [N]: No): ").strip().upper()
        if user_input == 'Y':
            # 파일 복사를 시작하고 덮어쓸지 이름에 숫자 추가할지 물어봄
            overwrite_choice = None  # 아직 선택 안 함
            break
        
        elif user_input == 'N':
            print("\n [Info] You chose not to create copies of the files.")
            return  # 파일 복사를 하지 않고 종료
        
        else:
            print(" [Info] Invalid input. Please enter either 'Y' or 'N'.")
    
    # 파일 덮어쓰기 여부 묻기
    overwrite_choice = None
    while True:
        user_input = input("\n\n\n [Info] What should be done if the file already exists? ([Y]: Overwrite, [N]: Add number to the name): ").strip().upper()
        if user_input == 'Y':
            overwrite_choice = True
            break
        
        elif user_input == 'N':
            overwrite_choice = False
            break
        
        else:
            print(" [Info] Invalid input. Please enter either 'Y' or 'N'.")

    # 복사 작업을 실행
    if Character_Header_Include:
        copy_files(Character_Header_Include, 'Character.csv', overwrite_choice=overwrite_choice)
        
    if Boss_Header_Include:
        copy_files(Boss_Header_Include, 'Boss.csv', overwrite_choice=overwrite_choice)
        
    if Nebbia_ID_Header_Include:
        copy_files(Nebbia_ID_Header_Include, 'Nebbia_ID.csv', overwrite_choice=overwrite_choice)

    input("\n\n\n [Info] All tasks have been completed. Press Enter key to continue.")

# 파일 복사 요청
prompt_copy_all_files()
