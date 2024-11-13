# GUI 관련
import tkinter as tk  # tkinter 모듈을 불러와 GUI 애플리케이션 생성
from tkinter import filedialog  # 파일 대화 상자를 사용하기 위한 임포트

# 파일 및 디렉토리 작업 관련
import os  # 운영 체제와 상호작용을 위한 모듈 (파일 경로, 환경 변수 등)
import shutil  # 고수준의 파일 및 디렉토리 작업을 위한 모듈 (파일 복사, 이동 등)
import glob  # 파일 경로를 찾기 위한 패턴 매칭을 제공하는 모듈

# 데이터 처리 관련
import csv  # *.csv 파일 읽기 및 쓰기를 위한 모듈
import struct  # C 구조체와 같은 바이너리 데이터의 패킹 및 언패킹을 위한 모듈
import re  # 정규 표현식을 사용하여 문자열 검색 및 조작을 위한 모듈

TOTAL_ANIMATION_COUNT = 0  # '*.cysp' 파일에 포함 된 Animation 수 총합 저장

CYSP_DIR_PATH = None  #사용자가 지정 할 '*.cysp' 파일 위치
CSV_FILE = None  # 사용자가 선택 할 '*.csv' 파일 위치
SKEL_DIR_PATH = None  # 사용자가 지정 할 '*.skel' 파일 저장 위치

def extract_anim_count(Full_Path_cysp_Name):
    global TOTAL_ANIMATION_COUNT
    
    try:
        with open(Full_Path_cysp_Name, 'rb') as fs:
            buf = fs.read(13)
            offset = (buf[12] + 1) * 32
            count = buf[12]

            if offset == 4032:
                return Full_Path_cysp_Name, None, "[WARNING] File not found"
            
            else:
                TOTAL_ANIMATION_COUNT += count
                return Full_Path_cysp_Name, count, "[SUCCESS] Animation count extracted"
            
    except FileNotFoundError:
        return Full_Path_cysp_Name, None, " [ERROR] File not found, skipping processing."
    
    except Exception as e:
        return Full_Path_cysp_Name, None, f" [ERROR] {e}"

def extract_data(Full_Path_cysp_Name, skel_file):
    """
    # (Decoded text) stateStop......
    """
    target_hex = bytes.fromhex("73 74 61 74 65 53 74 6F 70 00 00 00 00 00 01")
    original_data = bytearray()

    try:
        with open(Full_Path_cysp_Name, 'rb') as fs:
            buf = fs.read(13)
            offset = (buf[12] + 1) * 32
            fs.seek(offset)
            while byte := fs.read(1):
                original_data.append(byte[0])
                skel_file.write(byte)

                if len(original_data) >= len(target_hex) and original_data[-len(target_hex):] == target_hex:
                    # 'TOTAL_ANIMATION_COUNT'의 값에서 1을 뺀 값을 바이트로 변환
                    hex_value = (TOTAL_ANIMATION_COUNT-1).to_bytes(1, byteorder='big')
                    skel_file.write(hex_value)
                    
            return Full_Path_cysp_Name, "[SUCCESS] Data extracted successfully"
        
    except Exception as e:
        return Full_Path_cysp_Name, f" [ERROR] Error: {e}"

def check_csv_and_confirm(input_number):
    global CSV_FILE
    
    if CSV_FILE is None:
        root = tk.Tk()
        root.withdraw()  # 메인 창 숨기기
        CSV_FILE = filedialog.askopenfilename(title="Select '*.csv' File", filetypes=[("CSV files", "*.csv")])

    if not CSV_FILE or not os.path.isfile(CSV_FILE):
        print(" [ERROR] '*.csv' file not found or invalid.")
        return False, None, None

    CSV_CHARACTER_NAME = None  # 캐릭터 이름 처리시 사용
    CSV_COMMON_BATTLE_ID = None  # 각 캐릭터별 할당 된 Battle ID 처리시 사용
    CSV_BASE_ID = None  # 전투 캐릭터 또는 보스 캐릭터 처리시 사용
    found = False

    try:
        with open(CSV_FILE, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)

            # 첫 번째 행 (헤더)을 가져오기
            header = next(reader)

            # 각 값의 인덱스 찾기
            if input_number.startswith('1'):
                CSV_Input_ID_Index = header.index("63b62d72f43f1ee9d3ffa6528fd788c4c05ab9bf3be4046fa0c670308ffda877")
                CSV_COMMON_BATTLE_ID_Index = header.index("758a833b38682617eb99c0e50e138a1e08008740c69a2a1e1fe3eaa6e913f894")
                CSV_CHARACTER_NAME_Index = header.index("556944d17c3dccfdac0aa708e6e713008a0ed10956c307cca8a49dffa26d09a8")
                
            elif input_number.startswith(('2', '3')):
                CSV_Input_ID_Index = header.index("5f6902a3cabd407a699ecbadbce41011b4703d685e80a48d3a51f5c3d44f3b7b")
                CSV_CHARACTER_NAME_Index = header.index("52c55fdb9c4384a8ba7151004585a3dfc2a464c71a3dc3d229fd33d6947331cd")
                CSV_BASE_ID_Index = header.index("42409c8a6a41c132c614b19c7171cc886b6bb65c172e9aec0406d143d4f27672")

            for row in reader:
                if len(row) >= 11:
                    if input_number.startswith('1'):
                        if row[CSV_Input_ID_Index] == input_number:
                            CSV_CHARACTER_NAME = row[CSV_CHARACTER_NAME_Index]
                            CSV_COMMON_BATTLE_ID = row[CSV_COMMON_BATTLE_ID_Index]
                            CSV_BASE_ID = None  # 'CSV_BASE_ID'는 일반 캐릭터 객체에서 사용하지 않음
                            found = True
                            break
                        
                    elif input_number.startswith(('2', '3')):
                        if row[CSV_Input_ID_Index] == input_number:
                            CSV_CHARACTER_NAME = row[CSV_CHARACTER_NAME_Index]
                            CSV_COMMON_BATTLE_ID = None  # 'CSV_COMMON_BATTLE_ID'는 몬스터 객체에서 사용하지 않음
                            CSV_BASE_ID = row[CSV_BASE_ID_Index]
                            found = True
                            break

        if found:
            print(f"\n [INFO] Character ID: {input_number:<10} Character Name: {CSV_CHARACTER_NAME:<16} Common Battle ID: {CSV_COMMON_BATTLE_ID if CSV_COMMON_BATTLE_ID is not None else 'N/A':<10}")

            while True:
                confirm_start = input("\n\n\n [INFO] Do you want to start this task? ([Y]/[N])\n >>> ").strip().upper()
                
                if confirm_start == 'Y':
                    if input_number.startswith('1'):
                        # 'zfill'을 통해 'COMMON_BATTLE_ID'를 2자리로 변환하여 반환
                        return True, CSV_CHARACTER_NAME, CSV_COMMON_BATTLE_ID.zfill(2), CSV_BASE_ID
                    
                    elif input_number.startswith(('2', '3')):
                        return True, CSV_CHARACTER_NAME, CSV_COMMON_BATTLE_ID, CSV_BASE_ID
                    
                elif confirm_start == 'N':
                    print("\n [INFO] Task canceled.")
                    return False, None, None, None
                
                else:
                    print("\n [ERROR] Invalid input. Please enter [Y] or [N].")
        else:
            print("\n [ERROR] Unable to process the file. Please try again.")
            return False, None, None, None

    except FileNotFoundError:
        print(" [ERROR] '*.csv' file not found.")
        return False, None, None, None
    
    except Exception as e:
        print(f" [ERROR] {e}")
        return False, None, None, None

def process_EtcAnime_files(input_number):
    global CYSP_DIR_PATH
    global SKEL_DIR_PATH
    
    # 기본 파일
    # ※ [ 매우 중요 ] 절대 수정 금지!
    ETC_ANIMATION_BASE_Files = [
        os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_BASE.cysp").replace("\\", "/"),
    ]

    # 수정 가능 영역
    ROOM_SPINEUNIT_ANIMATION_SELECT_Files = [
        os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_COMMON.cysp").replace("\\", "/"),
        os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_002801.cysp").replace("\\", "/"),
        os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_002803.cysp").replace("\\", "/"),
        os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_002811.cysp").replace("\\", "/"),
    ]

    # 모든 'MINIGAME_*.cysp' 파일을 가져와서 필터링
    Filtered_MINIGAME_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "MINIGAME_*.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 모든 'NAVI_*.cysp' 파일을 가져와서 필터링
    Filtered_NAVI_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "NAVI_*.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 'Filtered_SPINEUNIT_Files' 에서 처리할 파일명 규칙 지정
    """
    규칙:
    'ROOM_SPINEUNIT_ANIMATION_(6자리 숫자)'
    (Ex. ROOM_SPINEUNIT_ANIMATION_002801)

    기능:
    지정한 규칙과 동일한 규칙을 가진 파일명들을 처리하기 위함.

    기능 구현 이유:
    'ROOM_SPINEUNIT_ANIMATION_' 규칙을 가진 파일 중 'ROOM_SPINEUNIT_ANIMATION_(6자리 숫자)'를 제외 한 나머지 파일들을 어떻게 처리해야 하는지 모르겠음

    예시:
    01. 'ROOM_SPINEUNIT_ANIMATION_(6자리 숫자)': 불러옴
    (Ex. ROOM_SPINEUNIT_ANIMATION_002801)

    02. 'ROOM_SPINEUNIT_ANIMATION_BASE_(6자리 숫자)': 불러오지 않음
    (Ex. ROOM_SPINEUNIT_ANIMATION_BASE_190901)
    
    03. 'ROOM_SPINEUNIT_ANIMATION_(6자리 숫자)_(6자리 숫자)': 불러오지 않음
    (Ex. ROOM_SPINEUNIT_ANIMATION_000009_192501)
    
    """
    Filtered_SPINEUNIT_Files_Pattern = r"^ROOM_SPINEUNIT_ANIMATION_\d{6}\.cysp$"

    # 모든 'ROOM_SPINEUNIT_ANIMATION_*.cysp' 파일을 가져와서 필터링
    Filtered_SPINEUNIT_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "ROOM_SPINEUNIT_ANIMATION_*.cysp").replace("\\", "/")) 
        if re.match(Filtered_SPINEUNIT_Files_Pattern, os.path.basename(f)) and f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 모든 'ROOM_SYNC_ANIME_*.cysp' 파일을 가져와서 필터링
    Filtered_SYNC_ANIME_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "ROOM_SYNC_ANIME_*.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 모든 'ROOM_TRACK_ANIME_*.cysp' 파일을 가져와서 필터링
    Filtered_TRACK_ANIME_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "ROOM_TRACK_ANIME_*.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 'SPINE_ANIME_CARAVAN_BUDDY.cysp' 파일을 가져와서 필터링
    Filtered_CARAVAN_BUDDY_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "SPINE_ANIME_CARAVAN_BUDDY.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 'SPINE_ANIME_CARAVAN_DRAMA.cysp' 파일을 가져와서 필터링
    Filtered_CARAVAN_DRAMA_Files = [
        f for f in glob.glob(os.path.join(CYSP_DIR_PATH, "SPINE_ANIME_CARAVAN_DRAMA.cysp").replace("\\", "/"))
        if f not in ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files
    ]

    # 작업 목록 정의
    tasks = [
        (ETC_ANIMATION_BASE_Files + Filtered_MINIGAME_Files, "MINIGAME_NEST"),
        (ETC_ANIMATION_BASE_Files + Filtered_NAVI_Files, "NAVI_NEST"),
        (ETC_ANIMATION_BASE_Files + ROOM_SPINEUNIT_ANIMATION_SELECT_Files, "ROOM_SPINEUNIT_ANIMATION_SELECT_NEST"),
        (ETC_ANIMATION_BASE_Files + Filtered_SYNC_ANIME_Files, "ROOM_SYNC_ANIME_NEST"),
        (ETC_ANIMATION_BASE_Files + Filtered_TRACK_ANIME_Files, "ROOM_TRACK_ANIME_NEST"),
        (ETC_ANIMATION_BASE_Files + Filtered_CARAVAN_BUDDY_Files, "SPINE_ANIME_CARAVAN_BUDDY"),
        (ETC_ANIMATION_BASE_Files + Filtered_CARAVAN_DRAMA_Files, "SPINE_ANIME_CARAVAN_DRAMA"),
    ]

    # 'ROOM_SPINEUNIT_ANIMATION_' 파일 그룹화
    spineunit_groups = {}
    
    for file in Filtered_SPINEUNIT_Files:
        base_name = os.path.basename(file)
        key = base_name[len("ROOM_SPINEUNIT_ANIMATION_"):len("ROOM_SPINEUNIT_ANIMATION_") + 4]
        
        if key not in spineunit_groups:
            spineunit_groups[key] = []
            
        spineunit_groups[key].append(file)

    # 각 그룹에 대해 추가 작업 수행
    for key, group_files in spineunit_groups.items():
        group_task_files = ETC_ANIMATION_BASE_Files + group_files
        tasks.append((group_task_files, f"ROOM_SPINEUNIT_ANIMATION_{key}_NEST"))  # 작업 이름과 파일 목록 튜플로 추가

    for idx, (task, task_name) in enumerate(tasks):
        global TOTAL_ANIMATION_COUNT  # 전역 변수 사용
        TOTAL_ANIMATION_COUNT = 0  # 각 작업마다 초기화

        # 임시 폴더 생성
        TEMP_Folder = os.path.join(SKEL_DIR_PATH, "_TEMP").replace("\\", "/")
        
        if not os.path.exists(TEMP_Folder):
            os.makedirs(TEMP_Folder)

        EtcAnime_final_files = [f for f in task if os.path.exists(f)]

        if not EtcAnime_final_files:
            print(" [ERROR] No valid EtcAnime files found. Skipping this task.")
            continue

        # 파일을 임시 폴더로 복사
        for file in EtcAnime_final_files:
            shutil.copy2(file, TEMP_Folder)

        skel_filename = os.path.join(TEMP_Folder, f"{task_name.replace(' ', '_')}_task_{idx + 1}.skel").replace("\\", "/")

        print("\n\n\n ========== Task Start ==========")
        
        print(f"\n [INFO] Starting the processing of task {idx + 1}/{len(tasks)}: {task_name}")
        print(f" [INFO] Creating skel file at '{skel_filename}'\n")
        
        print(f"{' File Name':<50} {'Animation Count':<20} {'Status':<40}")
        print(" " + "=" * 118)

        try:
            with open(skel_filename, 'wb') as skel:
                for item in EtcAnime_final_files:
                    status_message = ""
                    count_message = ""
                    Full_Path_cysp_Name, count, status_message = extract_anim_count(os.path.join(TEMP_Folder, item).replace("\\", "/"))
                    cysp_File_Name_Only = os.path.join(os.path.basename(TEMP_Folder), os.path.basename(Full_Path_cysp_Name)).replace("\\", "/")
                    count_message = str(count) if count is not None else "N/A"
                    print(f"  {cysp_File_Name_Only:<50} {count_message:<20} {status_message:<40}")

                # 데이터 추출 로직
                for item in EtcAnime_final_files:
                    Full_Path_cysp_Name, status_message = extract_data(os.path.join(TEMP_Folder, item).replace("\\", "/"), skel)
                    cysp_File_Name_Only = os.path.join(os.path.basename(TEMP_Folder), os.path.basename(Full_Path_cysp_Name)).replace("\\", "/")
                    print(f"  {cysp_File_Name_Only:<50} {'N/A':<20} {status_message:<40}")

            # 파일을 상위 폴더로 이동
            final_skel_filename = os.path.join(SKEL_DIR_PATH, f"{task_name.replace(' ', '_')}.skel").replace("\\", "/")
            
            shutil.move(skel_filename, final_skel_filename)
            
            print(f"\n [INFO] Total animation count: {TOTAL_ANIMATION_COUNT}")
            print(f" [INFO] {TOTAL_ANIMATION_COUNT - 1} items (Hex: 0x{hex(TOTAL_ANIMATION_COUNT - 1)[2:].upper()}) animations have been allocated.")

            print(f"\n [INFO] Processed task '{task_name}' saved as '{final_skel_filename}'")

        except Exception as e:
            print(f" [ERROR] Failed to write skel file: {e}")

        # 작업 후 임시 폴더 삭제
        try:
            if os.path.exists(TEMP_Folder):
                shutil.rmtree(TEMP_Folder)
                print(" [INFO] Temporary folder deleted.")
                
        except Exception as e:
            print(f" [ERROR] Failed to delete temporary folder: {e}")

def main():
    global CYSP_DIR_PATH
    global CSV_FILE
    global SKEL_DIR_PATH
    
    print("\n ========== Welcome to 'Priconne cysp To skel' Tool ==========")

    root = tk.Tk()
    root.withdraw()  # 메인 창 숨기기

    print("\n [INFO] Select the Folder with '*.cysp' Files")

    while True:
        # 사용자에게 디렉토리 선택을 위한 파일 다이얼로그 창 띄우기
        CYSP_DIR_PATH = filedialog.askdirectory(title="Select the Folder with .cysp Files")

        # 디렉토리가 선택된 경우
        if CYSP_DIR_PATH and os.path.isdir(CYSP_DIR_PATH):
            print(f" [INFO] Selected Folder: {CYSP_DIR_PATH}")

            # 디렉토리에서 .cysp 파일 찾기
            cysp_files = [f for f in os.listdir(CYSP_DIR_PATH) if f.endswith('.cysp')]

            # .cysp 파일이 존재하는지 확인
            if cysp_files:
                break
            
            else:
                print(" [ERROR] No .cysp files found in the selected folder.")
                while True:
                    retry = input("\n [INFO] Do you want to select another folder? ([Y]/[N])\n >>> ").strip().upper()

                    if retry in ('Y', 'N'):
                        break

                    print("\n [ERROR] Invalid input. Please enter [Y] or [N].")

                if retry == 'N':
                    print("\n [INFO] Exiting the program.")
                    return

        else:
            print(" [ERROR] Invalid folder or folder not selected.")
            while True:
                retry = input("\n [INFO] Do you want to select the folder again? ([Y]/[N])\n >>> ").strip().upper()

                if retry in ('Y', 'N'):
                    break

                print("\n [ERROR] Invalid input. Please enter [Y] or [N].")

            if retry == 'N':
                print("\n [INFO] Exiting the program.")
                return

    print("\n [INFO] Select Masterdata '*.csv' File")
    
    while True:
        CSV_FILE = filedialog.askopenfilename(title="Select '*.csv' File", filetypes=[("CSV file", "*.csv")])

        if CSV_FILE and os.path.isfile(CSV_FILE):
            csv_filename = os.path.basename(CSV_FILE)  # 파일 이름만 추출

            print(f" [INFO] Selected '*.csv' File: {csv_filename}")
            break
        
        else:
            print(" [ERROR] '*.csv' file not found or invalid.")
            while True:
                retry = input("\n [INFO] Do you want to select the '*.csv' file again? ([Y]/[N])\n >>> ").strip().upper()

                if retry in ('Y', 'N'):
                    break

                print("\n [ERROR] Invalid input. Please enter [Y] or [N].")

            if retry == 'N':
                print("\n [INFO] Exiting the program.")
                return

    print("\n [INFO] Select the Folder to Save the skel File")

    while True:
        # 사용자에게 디렉토리 선택을 위한 파일 다이얼로그 창 띄우기
        SKEL_DIR_PATH = filedialog.askdirectory(title="Select the Folder to Save the skel File")

        # 디렉토리가 선택된 경우
        if SKEL_DIR_PATH and os.path.isdir(SKEL_DIR_PATH):
            print(f" [INFO] Selected Folder: {SKEL_DIR_PATH}")
            break

        else:
            print(" [ERROR] Invalid folder or folder not selected.")
            
            while True:
                retry = input("\n [INFO] Do you want to select the folder again? ([Y]/[N])\n >>> ").strip().upper()

                if retry in ('Y', 'N'):
                    break

                print("\n [ERROR] Invalid input. Please enter [Y] or [N].")

            if retry == 'N':
                print("\n [INFO] Exiting the program.")
                return

    while True:
        global TOTAL_ANIMATION_COUNT
        TOTAL_ANIMATION_COUNT = 0

        print("\n\n\n ========== Command List ==========")
        print("\n ● 'Character ID (6 digits)': Perform tasks related to the specified Character ID.")
        print("    (Example: Entering '123456' will process the character animation files for Character ID '123456'.)\n")
        
        print(" ● 'EtcAnime': Processes all animations except for battle animations.\n")
        
        print(" ● 'EXIT': Quit the program.\n")
        
        print(" (Note: Ensure to enter a valid 6-digit Character ID or use 'EtcAnime' or 'EXIT'. (all inputs are not case-sensitive))")
        print("        (There is no guarantee that all skel files created will work as expected.)")

        
        input_number = input(" >>> ").strip()

        if input_number.upper() == 'EXIT':
            while True:
                confirm_exit = input("\n [INFO] Are you sure you want to exit? ([Y]/[N])\n >>> ").strip().upper()

                if confirm_exit in ('Y', 'N'):
                    break

                print("\n [ERROR] Invalid input. Please enter [Y] or [N].")

            if confirm_exit == 'Y':

                print("\n [INFO] Exiting the program.")
                return
            
            else:
                continue

        if input_number.upper() == 'ETCANIME':
            while True:
                confirm_start = input("\n\n\n [INFO] Do you want to start the 'EtcAnime' task? ([Y]/[N])\n >>> ").strip().upper()

                if confirm_start in ('Y', 'N'):
                    if confirm_start == 'Y':
                        process_EtcAnime_files(input_number)

                    else:
                        print("\n [INFO] Task canceled.")

                    break
                
                print("\n [ERROR] Invalid input. Please enter [Y] or [N].")
                
            continue

        if not (input_number.isdigit() and len(input_number) == 6):
            print("\n [ERROR] Invalid input. Please enter a 6-digit number or type 'EtcAnime' or type 'EXIT'")
            continue

        if input_number.startswith('1'):
            # 오른쪽에서 두 번째 숫자가 1, 2, 3, 4, 5, 6 중 하나일 경우 0으로 변경
            if input_number[-2] in '123456':
                old_value = input_number
                input_number = input_number[:-2] + '0' + input_number[-1]

                print("\n [INFO] The number of stars for the Character ID has been set to 0")
                print(f" [INFO] changing from '{old_value}' to '{input_number}'")

        # *.csv 확인 및 사용자 확인
        proceed, CSV_CHARACTER_NAME, CSV_COMMON_BATTLE_ID, CSV_BASE_ID = check_csv_and_confirm(input_number)
        
        if not proceed:
            continue  # 숫자가 없거나 오류가 발생한 경우 다시 입력 받기

        TEMP_Folder = os.path.join(SKEL_DIR_PATH, "_TEMP").replace("\\", "/")
        if not os.path.exists(TEMP_Folder):
            os.makedirs(TEMP_Folder)

        # 기본 파일 및 로직 분기
        if input_number.startswith('1'):
            while True:
                print("\n\n\n ========== Select Option ==========")
                print("\n [1] Normal Animation\t\t [2] Full Animation")
                print("\tIncluded files:\t\t\t Included files:")
                print("\t- _CHARA_BASE.cysp\t\t - _CHARA_BASE.cysp")
                print("\t- _COMMON_BATTLE.cysp\t\t - _COMMON_BATTLE.cysp")
                print("\t- _BATTLE.cysp\t\t\t - _BATTLE.cysp")
                print("\t- _DEAR.cysp\t\t\t - _DEAR.cysp")
                print("\t- _NO_WEAPON.cysp\t\t - _NO_WEAPON.cysp")
                print("\t- _POSING.cysp\t\t\t - _POSING.cysp")
                print("\t\t\t\t\t - _RACE.cysp")
                print("\t\t\t\t\t - _RUN_JUMP.cysp")
                print("\t- _SMILE.cysp\t\t\t - _SMILE.cysp")
                print("\n (Note: If you encounter an error using the [2] Full Animation, please try using the [1] Normal Animation.)")
                animation_type = input(" >>> ")

                if animation_type not in ['1', '2']:
                    print("\n [ERROR] Invalid input. Please enter [1] for Normal Animation or [2] for Full Animation.")
                    
                else:
                    break
                
            # 기본 파일
            base_files = [
                # ※ [ 매우 중요 ] 절대 수정 금지!
                "000000_CHARA_BASE.cysp",
                f"{CSV_COMMON_BATTLE_ID}_COMMON_BATTLE.cysp",
                "000000_BATTLE.cysp",
                
                # 수정 가능 영역
                "000000_DEAR.cysp",
                "000000_NO_WEAPON.cysp",
                "000000_POSING.cysp",
                "000000_RACE.cysp",
                "000000_RUN_JUMP.cysp",
                "000000_SMILE.cysp",
            ]

            # 개별 할당 파일
            number_files = [
                # ※ [ 매우 중요 ] 절대 수정 금지!
                f"{input_number}_CHARA_BASE.cysp",
                f"{input_number}_COMMON_BATTLE.cysp",
                f"{input_number}_BATTLE.cysp",

                # 수정 가능 영역
                f"{input_number}_DEAR.cysp",
                f"{input_number}_NO_WEAPON.cysp",
                f"{input_number}_POSING.cysp",
                f"{input_number}_RACE.cysp",
                f"{input_number}_RUN_JUMP.cysp",
                f"{input_number}_SMILE.cysp",
            ]

            # final_files 리스트 초기화
            final_files = []

            # [1] Normal Animation 선택시 '_RACE.cysp'와 '_RUN_JUMP.cysp' 파일을 제외
            if animation_type == '1':  # Normal Animation 선택
                # base_files에서 '_RACE.cysp'와 '_RUN_JUMP.cysp' 파일이 있을 경우만 제거
                if "000000_RACE.cysp" in base_files:
                    base_files.remove("000000_RACE.cysp")
                
                if "000000_RUN_JUMP.cysp" in base_files:
                    base_files.remove("000000_RUN_JUMP.cysp")
                
                # number_files에서 '{input_number}_RACE.cysp'와 '{input_number}_RUN_JUMP.cysp' 파일이 있을 경우만 제거
                if f"{input_number}_RACE.cysp" in number_files:
                    number_files.remove(f"{input_number}_RACE.cysp")
                
                if f"{input_number}_RUN_JUMP.cysp" in number_files:
                    number_files.remove(f"{input_number}_RUN_JUMP.cysp")


            # 디버깅용 출력: TEMP_Folder가 올바르게 설정되었는지 확인
            print(f"\n Copying files to: {TEMP_Folder}")

            # final_files 리스트 채우기
            for i in range(len(base_files)):
                base_file = base_files[i]
                number_file = number_files[i]

                # 경로 확인
                number_file_path = os.path.join(CYSP_DIR_PATH, number_file).replace("\\", "/")
                base_file_path = os.path.join(CYSP_DIR_PATH, base_file).replace("\\", "/")

                # 경로 출력
                print(f"\n Checking {number_file} at {number_file_path}")
                print(f" Checking {base_file} at {base_file_path}")

                # 경로가 존재하는지 확인
                if os.path.exists(number_file_path):
                    print(f" Found {number_file}")
                    final_files.append(number_file)
                    
                elif os.path.exists(base_file_path):
                    print(f" Found {base_file}")
                    final_files.append(base_file)
                    
                else:
                    print(f" Neither {number_file} nor {base_file} found.")
                    final_files.append(None)

            # 최종 결과 출력 - 필터링 전
            print(f"\n Final files before filtering: {final_files}")

            # None 값을 필터링하여 유효한 파일만 포함
            final_files = [file for file in final_files if file is not None]

            # 최종 결과 출력 - 필터링 후
            print(f"\n Final files after filtering: {final_files}")

            # 파일 유효성 검사
            if not final_files:
                print("\n [ERROR] No valid files found. Exiting.")
                
            else:
                for file in final_files:
                    print(f"\n Valid file: {file}")

        elif input_number.startswith(('2', '3')):
            Boss_files = CSV_BASE_ID
            print(f"{Boss_files}")
            
            Boss_files = [
                f"{Boss_files}_CHARA_BASE.cysp",
                f"{Boss_files}_BATTLE.cysp",
                f"{Boss_files}_RACE.cysp",
            ]

            # final_files 리스트 초기화
            final_files = []

            # final_files 리스트 채우기
            for Boss_files in Boss_files:
                # CYSP_DIR_PATH 경로에서 파일 존재 여부 확인
                number_file_path = os.path.join(CYSP_DIR_PATH, Boss_files).replace("\\", "/")

                if os.path.exists(number_file_path):
                    final_files.append(Boss_files)

                else:
                    final_files.append(None)

        else:
            print("\n [ERROR] Invalid Character ID. Exiting.")
            continue

        # final_files 리스트가 올바르게 채워졌는지 확인
        if final_files:
            print("\n Final files to be copied:", final_files)
            
        else:
            print("[ERROR] final_files is empty.")
            
        # None 값을 필터링하여 유효한 파일만 포함
        final_files = [file for file in final_files if file is not None]

        # 파일 유효성 검사
        if not final_files:
            print("\n [ERROR] No valid files found in final_files. Exiting.")
        else:
            # 파일 복사
            for file in final_files:
                if file:
                    source_path = os.path.join(CYSP_DIR_PATH, file).replace("\\", "/")
                    destination_path = os.path.join(TEMP_Folder, file).replace("\\", "/")
                    
                    print(f"\n Attempting to copy {file} from {source_path} to {destination_path}")
                    
                    # 파일이 실제로 존재하는지 확인
                    if os.path.exists(source_path):
                        shutil.copy2(source_path, destination_path)
                        print(f" Copied {file} successfully.")
                        
                    else:
                        print(f"[ERROR] {file} does not exist at source path: {source_path}\n")

        for file in final_files:
            if file and os.path.exists(file):  # 파일이 None이 아니고 존재할 경우만 복사
                destination = os.path.join(TEMP_Folder, file).replace("\\", "/")
                print(f"\n Copying {file} to {destination}")
                shutil.copy2(file, destination)
                
        skel_filename = os.path.join(TEMP_Folder, f"{input_number}.skel").replace("\\", "/")

        print("\n\n\n ========== Task Start ==========")
        
        print(f"\n [INFO] Processing files for input number: {input_number}\n")
        print(f" [INFO] Creating skel file at '{skel_filename}'\n")
        
        print(f"  {'File Name':<50} {'Animation Count':<20} {'Status':<40}")
        print(" " + "=" * 118)

        with open(skel_filename, 'wb') as skel:
            for item in final_files:
                status_message = ""
                count_message = ""
                
                if item != "offset":
                    Full_Path_cysp_Name, count, status_message = extract_anim_count(os.path.join(TEMP_Folder, item).replace("\\", "/"))
                    cysp_File_Name_Only = os.path.join(os.path.basename(TEMP_Folder), os.path.basename(Full_Path_cysp_Name)).replace("\\", "/")
                    count_message = str(count) if count is not None else "N/A"
                    print(f"  {cysp_File_Name_Only:<50} {count_message:<20} {status_message:<40}")

            for item in final_files:
                if item == "offset":
                    skel.write(struct.pack('B', TOTAL_ANIMATION_COUNT - 1))
                    
                else:
                    Full_Path_cysp_Name, status_message = extract_data(os.path.join(TEMP_Folder, item).replace("\\", "/"), skel)
                    cysp_File_Name_Only = os.path.join(os.path.basename(TEMP_Folder), os.path.basename(Full_Path_cysp_Name)).replace("\\", "/")
                    print(f"  {cysp_File_Name_Only:<50} {'N/A':<20} {status_message:<40}")

        if input_number.startswith('1'):
            if input_number == '118601':
                final_skel_filename = os.path.join(SKEL_DIR_PATH, f"{input_number}_190901_{CSV_CHARACTER_NAME}.skel").replace("\\", "/")
                
            else:
                final_skel_filename = os.path.join(SKEL_DIR_PATH, f"{input_number}_{CSV_CHARACTER_NAME}.skel").replace("\\", "/")

            shutil.move(skel_filename, final_skel_filename)

            print(f"\n [INFO] Total animation count: {TOTAL_ANIMATION_COUNT}")
            print(f" [INFO] {TOTAL_ANIMATION_COUNT - 1} items (Hex: 0x{hex(TOTAL_ANIMATION_COUNT - 1)[2:].upper()}) animations have been allocated.")

            print(f"\n [INFO] Processed  saved as '{final_skel_filename}'")
            
            if input_number == '118601':
                print(f" [INFO] Naming Convention: 'Character ID'_'Room Spineunit ID'_'Character Name'")
                
            else:
                print(f" [INFO] Naming Convention: 'Character ID'_'Character Name'")

        elif input_number.startswith(('2', '3')):
            final_skel_filename = os.path.join(SKEL_DIR_PATH, f"{CSV_BASE_ID}_{input_number}_{CSV_CHARACTER_NAME}.skel").replace("\\", "/")

            shutil.move(skel_filename, final_skel_filename)

            print(f"\n [INFO] Total animation count: {TOTAL_ANIMATION_COUNT}")
            print(f" [INFO] {TOTAL_ANIMATION_COUNT - 1} items (Hex: 0x{hex(TOTAL_ANIMATION_COUNT - 1)[2:].upper()}) animations have been allocated.")

            print(f"\n [INFO] Processed file saved as '{final_skel_filename}'")
            print(f" [INFO] Naming Convention: 'Base Unit ID'_'Character ID'_'Character Name'")

        # 작업 후 임시 폴더 삭제
        try:
            if os.path.exists(TEMP_Folder):
                shutil.rmtree(TEMP_Folder)
                print("\n [INFO] Temporary folder deleted.")
                
        except Exception as e:
            print(f" [ERROR] Failed to delete temporary folder: {e}")

if __name__ == "__main__":
    main()
