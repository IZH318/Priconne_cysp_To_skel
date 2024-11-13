import os  # 운영 체제와 상호작용하는 기능을 제공하는 모듈 (파일 및 디렉토리 작업 등)
import sqlite3  # SQLite 데이터베이스와 상호작용하는 기능을 제공하는 모듈
import pandas as pd  # 데이터 분석 및 조작을 위한 pandas 라이브러리 (DataFrame 등)
import tkinter as tk  # tkinter 모듈을 불러와 GUI 애플리케이션 생성
from tkinter import filedialog  # 파일 대화 상자를 사용하기 위한 임포트

# 프로그램 시작 시 출력
print("\n ===== SQLite to CSV Extractor =====")
print(" A tool to extract all tables from an SQLite database and export them as CSV files.\n\n")

def extract_all_data_to_csv(db_path, output_path):
    # 데이터베이스에 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 모든 테이블 이름 가져오기
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # 테이블 개수
    num_tables = len(tables)

    # 데이터베이스 파일 이름 출력
    db_file_name = os.path.basename(db_path)  # DB 파일 이름 (확장자 포함)
    db_name_without_extension = os.path.splitext(db_file_name)[0]  # 확장자 제외한 DB 파일 이름
    folder_name = f"{db_name_without_extension}_CSVExport"  # '_CSVExport' 추가하여 폴더 이름 생성

    print(f"\n [INFO] Selected database file: {db_file_name}")
    print(f" [INFO] Total number of tables: {num_tables}")
    print(f"\n [INFO] Using folder name: {folder_name}")

    # DB 파일 이름을 가진 폴더를 출력 경로 안에 생성
    output_folder = os.path.join(output_path, folder_name)
    
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"\n [INFO] Folder '{folder_name}' does not exist. It has been created.")
    
    # 출력되는 CSV 파일들의 저장 경로
    print(f"\n [INFO] CSV files will be saved in the following directory:\n        {output_folder}")


    # 사용자가 작업 진행 여부 확인
    while True:
        response = input(f"\n [INFO] Do you want to proceed with exporting {num_tables} tables to CSV? ([Y]/[N])\n >>> ").strip().upper()
        if response in ['Y', 'N']:
            break
        print("\n [INFO] Invalid input. Please enter 'Y' or 'N'.")

    if response == 'N':
        print("\n [INFO] Exiting the program.")
        return

    # 각 테이블의 데이터를 CSV로 저장
    for index, table in enumerate(tables, start=1):
        table_name = table[0]
        print(f"\n [INFO] Progress: {index}/{num_tables}")  # 처리 중인 테이블 순서 출력
        print(f" [INFO] Processing table: {table_name}")  # 테이블 이름 출력

        # 테이블의 데이터를 DataFrame으로 가져오기
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)

        # CSV 파일 경로 지정 (DB 파일 이름을 가진 폴더 안에 테이블 이름으로 저장)
        csv_file_path = os.path.join(output_folder, f"{table_name}.csv")
        df.to_csv(csv_file_path, index=False)
        print(f" [INFO] Data has been successfully saved to '.\\{folder_name}\\{table_name}.csv'.")

    # 연결 종료
    conn.close()
    print("\n [INFO] All tables have been successfully exported to CSV files.")  # 작업 완료 메시지 출력

    input("\n\n\n [Info] All tasks have been completed. Press Enter key to continue.")

def select_database_file():
    # tkinter 창을 숨김
    root = tk.Tk()
    root.withdraw()

    # 파일 대화상자 열기 (사용자가 SQLite 파일을 선택)
    file_path = filedialog.askopenfilename(
        title="Select SQLite Database File",
        filetypes=[("SQLite Database", "*.db")]
    )

    return file_path

def select_output_directory():
    # tkinter 창을 숨김
    root = tk.Tk()
    root.withdraw()

    # 폴더 선택 대화상자 열기 (사용자가 출력 경로를 선택)
    folder_path = filedialog.askdirectory(
        title="Select Folder to Save CSV Files"
    )

    return folder_path

# 데이터베이스 파일 선택 및 확인
while True:
    db_path = select_database_file()

    if db_path:
        # 출력 경로 선택
        output_path = select_output_directory()

        if output_path:
            extract_all_data_to_csv(db_path, output_path)
            break
        else:
            # 경로가 지정되지 않으면 다시 선택하게 하기
            print("\n [INFO] No output folder selected. Please select a folder to save the CSV files.")
            while True:
                response = input("\n [INFO] Do you want to try selecting the folder again? ([Y]/[N])\n >>> ").strip().upper()
                if response in ['Y', 'N']:
                    break
                print("\n [INFO] Invalid input. Please enter 'Y' or 'N'.")
            
            if response == 'N':
                print("\n [INFO] Exiting the program.")
                break
    else:
        # 파일 선택하지 않았을 경우 재선택 여부 확인
        while True:
            response = input("\n [INFO] No file selected. Would you like to select again? ([Y]/[N])\n >>> ").strip().upper()
            if response in ['Y', 'N']:
                break
            print("\n [INFO] Invalid input. Please enter 'Y' or 'N'.")
        
        if response == 'N':
            print("\n [INFO] Exiting the program.")
            break
