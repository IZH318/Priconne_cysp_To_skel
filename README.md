# Priconne Cysp To Skel
이 프로젝트는 **Princess Connect! Re: Dive** 게임에서 사용하는 `.cysp` 파일을 `.skel` 형식으로 추출, 처리 및 변환하려는 사용자를 돕기 위해 만들어졌습니다. <BR> <BR>
`Priconne Cysp To Skel` 을 사용하여 작업할 때 필요한 기타 도구들도 함께 제공합니다.

<BR>

## 📅 마지막 정상 작동 확인 날짜 및 버전
- **DATE**: 2024-11-11  
- **Client Ver**: 10.8.5

<BR>

## 🔍 주요 기능
- **Priconne CSV Header Finder**  
  캐릭터, 보스, Nebbia ID와 관련된 특정 헤더 값이 포함된 `.csv` 파일 자동 검색  
  🔗 URL: [Introduce Priconne CSV Header Finder](https://github.com/IZH318/Priconne_cysp_To_skel/blob/main/Introduce%20Priconne%20CSV%20Header%20Finder.md) <BR> <BR>

- **Priconne cysp To skel**  
  사용자가 입력하는 정보에 맞게 `.skel` 파일 생성  
  🔗 URL: [Introduce Priconne cysp To skel](https://github.com/IZH318/Priconne_cysp_To_skel/blob/main/Introduce%20Priconne%20Cysp%20To%20Skel.md)

<BR>

## 💾 다운로드 <BR>
| Program                                | URL                                                | 필수여부 | 비고                                                                                           |
|----------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------------------------------------|
| `Python`            | [Download](https://www.python.org/downloads/release/python-390/)   | 필수     | ◼ Python Script 동작, 파이썬 3.9.0 버전 또는 그 이상 사용 가능 |
| `반디집`             | [Download](https://kr.bandisoft.com/bandizip/)   | 필수     | ◼ (* 다른 압축 프로그램 사용 가능) |

<BR>

## 🛠️ 설치

1. Python 설치 파일을 실행 합니다. <BR> <BR>

2. Python을 설치합니다. <BR> <BR>
![2024-11-06 07 20 58](https://github.com/user-attachments/assets/66362323-9dea-4bd5-bd76-4f1c268c567b) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
![2024-11-06 07 21 25](https://github.com/user-attachments/assets/0d83ce4b-c5f1-44cc-855e-87b974cf24b3) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR> <BR>

3. cmd 실행 후 아래 내용을 참고하여 필요한 패키지를 업데이트(선택) 또는 설치 합니다. <BR> <BR>
- ❗ Windows 환경 사용자는 `00. Install_required_Python_packages.bat` 을 실행하여 필요 패키지를 한 번에 설치할 수 있습니다. <BR> <BR>
  - **🎞 참고 자료:** <BR>
    ![_2024_11_11_00_03_44_651-ezgif com-optimize](https://github.com/user-attachments/assets/dd2c4c7f-362a-4589-8c43-c588ace0eb29) <BR>
    (📌 파이썬 패키지 일괄 설치) <BR>
<BR> <BR> <BR>
3-1. **(선택사항, 생략가능) Python Package Update** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip` <BR>
or <BR>
`python -m pip install --upgrade pip` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip --user` <BR>
or <BR>
`python -m pip install --upgrade pip --user` <BR>
<BR> <BR> <BR>
3-2. **(필수) pandas Package 설치** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install pandas` <BR>
or <BR>
`python -m pip install pandas` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install pandas --user` <BR>
or <BR>
`python -m pip install pandas --user` <BR>
<BR> <BR> <BR>
3-3. **(필수) tqdm Package 설치** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install tqdm` <BR>
or <BR>
`python -m pip install tqdm` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install tqdm --user` <BR>
or <BR>
`python -m pip install tqdm --user` <BR>
<BR> <BR> <BR>
3-4. **(필수) xxhash Package 설치** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install xxhash` <BR>
or <BR>
`python -m pip install xxhash` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install xxhash --user` <BR>
or <BR>
`python -m pip install xxhash --user` <BR>

<BR>

## ⏩ 사용 방법

### 1. **게임 데이터 사본 생성**  

**⚠ 경고**:
- 이 작업은 원본 데이터 경로에 있는 파일 이름을 변경하여 작업을 진행해야 합니다. <BR>
- 원본 데이터 경로에 있는 파일 이름을 변경할 경우, 원본 데이터의 파일을 클라이언트에서 인식하지 못하므로 모든 데이터를 처음부터 다시 다운로드 받아야 합니다. <BR> <BR>

아래 안내하는 내용을 참고하여 폴더를 작업할 경로로 복사하여 사본을 생성하십시오.

- **Windows 사용자**  
  JP Server  
  `C:\Users\(PC User Name)\AppData\LocalLow\Cygames`

  - **💡 작업 팁**
    - `C:\Users\(PC User Name)\AppData\LocalLow\Cygames` 폴더 내 `a` 폴더, `manifest` 폴더, `manifest.db` 파일만 사본을 만들면 시간과 용량 모두 절약 할 수 있습니다. <BR> <BR>

- **Android 사용자** (* 루팅 필요, Android Emulator 사용 권장)  
  - JP Server  
    `/data/data/jp.co.cygames.princessconnectredive`

  - KR Server  
    `/data/data/com.kakaogames.pcr` <BR> <BR>

- **🎞 참고 자료:** <BR>
  ![_2024_11_11_00_01_28_722-ezgif com-optimize](https://github.com/user-attachments/assets/31bae049-e6a2-4dee-b04c-8efe2d56de7c) <BR>
  (📌 게임 데이터 사본 생성) <BR> <BR>

### 2. **게임 데이터 파일 이름 변경**  

`PRICONNE EXTRACTION TOOLS(Portable)`의 `01. Manifest File Renamer.py`를 사용하여 원본 데이터의 파일 이름을 변경하십시오.

`PRICONNE EXTRACTION TOOLS(Portable)` 사용 방법 및 필요 파일들은 아래 링크로 이동하여 확인하십시오.  
🔗 URL: https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable <BR> <BR>

- ❗ '🛠️ 설치' 단계에서 패키지를 모두 설치했다면 추가 작업 없이 바로 사용할 수 있습니다. <BR> <BR>

- **🎞 참고 자료:** <BR>
  ![_2024_11_11_00_14_53_225-ezgif com-optimize](https://github.com/user-attachments/assets/78bdb89a-3694-4491-8f7b-0d06b1378ed5) <BR>
  (📌 게임 데이터 파일 이름 변경) <BR> <BR>

### 3. **게임 데이터 추출**  
`.unity3d` 파일을 변환하여 리소스 파일을 추출해야 합니다.  

- **방법 1**:  
  - `PRICONNE EXTRACTION TOOLS(Portable)`의 `02. unity3d File Converter.py`를 사용하여 `.unity3d` 파일 리소스를 추출하십시오.  
  - `PRICONNE EXTRACTION TOOLS(Portable)` 사용 방법 및 필요 파일들은 아래 링크로 이동하여 확인하십시오.  
    🔗 URL: https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable <BR> <BR>
  
  - ❗ '🛠️ 설치' 단계에서 패키지를 모두 설치했다면 추가 작업 없이 바로 사용할 수 있습니다. <BR> <BR>

  - **🎞 참고 자료:** <BR>
    ![_2024_11_11_00_17_51_833-ezgif com-optimize](https://github.com/user-attachments/assets/c261774d-81d4-4df7-96ba-03639b13034b) <BR>
    (📌 `.unity3d` 파일 리소스 추출) <BR> <BR>


- **방법 2**:  
  - `AssetStudio`를 사용하여 `.unity3d` 파일 리소스를 추출하십시오.
  - `AssetStudio` 사용 방법 및 필요 파일들은 아래 링크로 이동하여 확인하십시오.  
    🔗 URL: https://github.com/Perfare/AssetStudio <BR> <BR>

  - `AssetStudio` 사용 시 `Options - Specify Unity version`에 추출할 데이터의 Unity Version을 직접 할당해야 합니다.  
    (📌 현 시점 기준 Specify Unity version: 2021.3.20f1) <BR> <BR>

  - **🎞 참고 자료:** <BR>
    ![_2024_11_11_00_22_30_859-ezgif com-optimize](https://github.com/user-attachments/assets/f02dd4ba-15fd-4352-81ff-2f8c62246b27) <BR>
    (📌 `cysp.unity3d` 파일 리소스 추출) <BR> <BR>

- **💡 작업 팁**
  - `.cysp.unity3d` 확장자를 가진 파일만 먼저 변환 후 `.skel` 파일을 생성하고, 필요한 리소스를 가진 `.unity3d` 파일을 변환하면 시간과 용량 모두 절약 할 수 있습니다. <BR> <BR>

### 4. **`.mdb` 파일을 `.csv` 파일로 저장**  
사용자가 편의상 직접 `.mdb` 파일을 `.db` 파일로 변환 후 `.csv` 파일로 저장하는 방식이 아닌, `.mdb` 파일이 `.db` 파일로 변경된 파일을 다운로드 후 `.csv` 파일로 저장하는 방식을 안내합니다.

- 4-01. 아래 링크로 이동하여 작업할 클라이언트 데이터에 맞는 `.db` 파일을 다운로드하십시오.  
  🔗 URL: https://github.com/Expugn/priconne-database

- 4-02. `SQLite to CSV Extractor`를 실행합니다.

- 4-03. `Select SQLite Database File` 창이 나타나면 다운로드한 `.db` 파일을 지정하고 열기(O) 버튼을 클릭합니다.

- 4-04. `Select Folder to Save CSV Files` 창이 나타나면 `.csv` 파일들이 저장될 경로를 지정하고 폴더 선택 버튼을 클릭합니다.

- 4-05. `.db` 파일 이름, 테이블 수, `.csv` 파일이 저장될 폴더 명, `.csv` 파일이 저장될 경로 정보가 반환됩니다. 정보를 확인한 후 Y를 입력하여 작업을 진행하십시오.

- 4-06. 모든 테이블이 `.csv` 파일로 생성되었다면 `SQLite to CSV Extractor`를 종료하십시오. <BR> <BR>

- **🎞 참고 자료:** <BR>
  ![_2024_11_11_00_56_23_685-ezgif com-optimize](https://github.com/user-attachments/assets/23d098cc-c900-496f-8863-3aac50105917) <BR>
  (📌 `.db` 파일에 저장 된 각 테이블을 `.csv` 파일로 저장) <BR> <BR>


### 5. **특정 헤더 포함된 `.csv` 파일 검색**  
`Priconne CSV Header Finder`를 사용하여 캐릭터 정보 또는 보스 정보가 포함된 파일을 찾아야 합니다.

`.bat`, `.py` 중 마음에 드는 파일을 한 가지 골라 작업하십시오.  
(*작업 속도상 `.py`를 추천합니다.)

- 5-01. `Priconne CSV Header Finder`를 `.csv` 파일이 저장된 경로로 복사합니다.

- 5-02. `Priconne CSV Header Finder`를 실행합니다.

- 5-03. 캐릭터 ID, 보스 ID, Nebbia ID와 관련된 파일 이름이 반환됩니다.  
  `Do you want to create copies of all the files? ([Y]: Yes, [N]: No):`에서 Y를 입력하면 적절한 이름으로 사본을 생성합니다.  
  - `.bat` 파일은 자동으로 사본 생성, 사본 중복 파일 발견 시 파일 이름 끝에 '_숫자'가 할당됨.
  - Nebbia ID와 관련된 CSV 파일을 사본으로 생성하는 이유는 Q&A를 참고하십시오.

- 5-04. CSV 파일 내용을 메모장, Excel 또는 기타 소프트웨어를 사용하여 확인합니다. <BR> <BR>

- **🎞 참고 자료:** <BR>
  ![_2024_11_11_00_58_45_344-ezgif com-optimize](https://github.com/user-attachments/assets/6b84faa0-81d2-4e07-bc28-0c9bd4868766) <BR>
  (📌 `.csv` 파일에 저장 된 데이터 검색 및 사본 생성) <BR> <BR>


### 6. **`.skel` 파일 생성**  

- 6-01. `Priconne cysp To skel`을 실행합니다.

- 6-02. `Select the Folder with .cysp Files` 창이 나타나면 `.cysp` 파일만 모인 경로를 지정하고 폴더 선택 버튼을 클릭합니다.

- 6-03. `Select CSV File` 창이 나타나면 `.skel` 파일을 생성할 대상(캐릭터 또는 보스)에 맞는 `.csv` 파일을 선택하고 열기(O) 버튼을 클릭합니다.

- 6-04. `Select the Folder to Save the skel File` 창이 나타나면 `.skel` 파일이 저장될 경로를 지정하고 폴더 선택 버튼을 클릭합니다.

- 6-05. `========== Command List ==========` 내용을 확인하고 처리할 대상을 입력합니다.

- 6-06. `.skel` 파일이 저장될 경로로 지정한 곳으로 이동 후 `.skel` 파일이 생성되었는지 확인합니다.

- 6-07. `Priconne cysp To skel`의 자세한 설명은 Introduce Priconne cysp To skel을 참고하십시오. <BR> <BR>

- **🎞 참고 자료:** <BR>
  ![_2024_11_11_01_02_11_814-ezgif com-optimize](https://github.com/user-attachments/assets/23417048-892f-4e5f-b251-28e0f1fa3215) <BR>
  (📌 캐릭터 `.skel` 파일 생성) <BR> <BR>
  ![_2024_11_11_01_02_33_62-ezgif com-optimize](https://github.com/user-attachments/assets/39d5e3fb-8276-4146-aea5-241af70984bb) <BR>
  (📌 기타 애니메이션 `.skel` 파일 생성) <BR> <BR>
  ![_2024_11_11_01_17_45_794-ezgif com-optimize](https://github.com/user-attachments/assets/a80ba59b-fd1e-4ab2-844b-256fe6d650ae) <BR>
  (📌 보스 `.skel` 파일 생성) <BR> <BR>

### 7. **확인**  

- 7-01. 생성한 `.skel` 파일에 맞게 추출한 리소스를 찾습니다.  
  캐릭터 ID 또는 보스 ID를 입력했을 경우: 'spine_sdnormal_캐릭터 ID 또는 보스 ID'
  `EtcAnime`를 입력했을 경우: 'room_spineunit_캐릭터 ID'

- 7-02. 해당 폴더에 있는 `.atlas`, `.png` 파일을 적절한 위치로 이동 또는 복사 후, 생성한 `.skel` 파일을 동일한 경로에 이동 또는 복사합니다.

- 7-03. 정상적으로 `.skel` 파일이 작동하는지 확인하십시오. 다음 방법 중 마음에 드는 방법을 한 가지 선택하여 작업하십시오.  
  (* 보스 ID를 입력하여 생성한 `.skel` 파일은 방법 1로 확인하기 어렵습니다.)

  - **방법 1**  
    아래 링크로 이동 후 Add skeleton 버튼을 클릭한 후, `.atlas`, `.png`, `.skel` 파일을 모두 선택하여 불러옵니다.  
    🔗 URL: https://naganeko.pages.dev/chibi-gif/ <BR> <BR>

    - **🎞 참고 자료:** <BR>
      ![_2024_11_11_01_04_41_605-ezgif com-optimize](https://github.com/user-attachments/assets/df722d34-77d9-4286-94bb-52514af6a729) <BR>
      (📌 캐릭터(フブキ) 전투(배틀) 애니메이션 확인) <BR> <BR>
      ![_2024_11_11_01_07_12_193-ezgif com-optimize](https://github.com/user-attachments/assets/9a961ac0-6d7b-400a-8ef2-98bc3c6e7cc9) <BR>
      (📌 캐릭터(フブキ) 미니게임 애니메이션 확인) <BR> <BR>

  - **방법 2**  
    아래 링크로 이동 후 `SuperSpineViewer`를 다운로드 받습니다.  
    🔗 URL: https://github.com/Aloento/SuperSpineViewer

    - **Java 21 설치**  
      아래 링크로 이동 후 **Java 21(JDK 21)** 을 다운로드 받고 설치합니다.  
      🔗 URL: https://www.oracle.com/jp/java/technologies/downloads/#jdk21-windows  
      (* 반드시 Java 21(JDK 21)을 다운로드 받고 설치해야 합니다.)

    - **`SuperSpineViewer` 파일 이동**  
      다운로드 받은 `SuperSpineViewer` 파일을 적절한 위치로 이동합니다.

    - **탐색기에서 명령어 입력**  
      `SuperSpineViewer` 파일이 위치 한 곳에서 탐색기의 주소 표시줄(단축키 F4)을 누르고, `cmd`를 입력한 후 Enter 키를 눌러 **명령 프롬프트**를 엽니다.

    - **명령어 입력**  
      명령 프롬프트에 아래 명령어를 입력하여 `SuperSpineViewer`를 실행합니다. <BR> <BR>
      `SuperSpineViewer` 실행 명령어: <BR>
      java -XX:MaxRAMPercentage=75.0 --enable-preview -jar 'SuperSpineViewer 파일 이름' <BR>
      
      - **예시**:  
        SuperSpineViewer 파일 이름: <BR>
        `SuperSpineViewer-2.1.0-Win64.jar` <BR>
        
        cmd에 입력해야 할 명령어: <BR>
        `java -XX:MaxRAMPercentage=75.0 --enable-preview -jar SuperSpineViewer-2.1.0-Win64.jar`

    - **파일 준비**  
      `.atlas`, `.png`, `.skel` 파일을 모두 하나의 폴더에 두고, `.skel` 파일 이름을 `.atlas`와 `.png` 파일 이름과 동일하게 수정합니다.

    - **Skeleton 파일 열기**  
      화면 좌 상단에 있는 **가로 줄 3개 아이콘**을 클릭한 후, **Open Skeleton**을 클릭합니다.

    - **`.skel` 파일 지정**  
      생성한 `.skel` 파일을 지정하고 **열기(O)** 버튼을 클릭하여 파일을 불러옵니다.

    - **🎞 참고 자료:** <BR>
      ![_2024_11_11_01_30_09_702-ezgif com-optimize](https://github.com/user-attachments/assets/126cdf66-32a3-4c16-bbb2-e40c3bf75366) <BR>
      (📌 보스(ラットン) 애니메이션 확인) <BR>
<BR>

## ❔ Q&A

### 01. 캐릭터 애니메이션을 다른 캐릭터 애니메이션으로 교체하고 싶다면?
- `.skel` 파일만 대체해서 사용하면 됩니다.

- 예시: 콧코로(여름)(ID: `107601`) 에 스즈나(ID: `101601`) 애니메이션을 할당하고 싶을 때
  - 콧코로(여름)(ID: `107601`)
    - `.allas` 파일
    - `.png` 파일 <BR>
    
  - 스즈나(ID: `101601`)
    - `.skel` 파일 사용 <BR> <BR>

### 02. 전투(배틀) 애니메이션과 기타 애니메이션에 사용하는 리소스 구분 방법?
- 전투(배틀): spine_sdnormal_'캐릭터 ID 또는 보스 ID'
- 길드 하우스 및 기타: room_spineunit_'캐릭터 ID' <BR>
- **❗ 중요:**
  - 캐릭터 ID의 오른쪽 2번째는 캐릭터의 별의 수 이므로 콧코로(여름)(ID: `107601`)의 6성 리소스를 원하면 `107661`, 3성 리소스를 원하면 `107631` 이 할당 된 폴더 명을 찾아서 사용하십시오. <BR> <BR>
 
### 03. SD 애니메이션에 사용되는 `.skel` 파일이 아닌 스토리에 사용되는 `.skel` 파일은?
- 추가 작업 없이 'spine_full_캐릭터 ID 또는 보스 ID' 폴더 내 파일을 확인하면 됩니다. <BR>
- **❗ 중요:**
  - 캐릭터 ID의 오른쪽 2번째는 캐릭터의 별의 수 이므로 콧코로(여름)(ID: `107601`)의 6성 리소스를 원하면 `107661`, 3성 리소스를 원하면 `107631` 이 할당 된 폴더 명을 찾아서 사용하십시오. <BR> <BR>
 
### 04. ネビア(Nebbia) 캐릭터에 사용되는 `.skel` 파일 생성 시 파일 이름이 `Character ID'_'Room Spineunit ID'_'Character Name'`로 할당하는 이유?
- Character ID와 실제로 사용하는 리소스의 ID가 서로 다르기 때문 <BR>
- **❗ 중요:**
  - 캐릭터 ID : `118601`
  - 리소스 ID : `room_spineunit_190911`

<BR>

### 제공된 코드 관리 및 수정과 관련 된 내용은 아래 링크를 클릭하여 참고하십시오. <BR>
- 🔗 URL: [Priconne cysp To skel QNA](https://github.com/IZH318/Priconne_cysp_To_skel/blob/main/Priconne%20cysp%20To%20skel%20QNA.md)

<BR>

## ✨ Special Thanks to

이 도구를 만들 수 있도록 도움을 준 분들께 감사의 마음을 전합니다.

- **Princess Connect! Re:Dive**  
  🔗 URL: https://priconne-redive.jp/

- **如何提取公主连结游戏动画素材**  
  🔗 URL: https://www.bilibili.com/opus/801111052800491733

- **[游戏攻略] [教程]如何提取公主连结游戏动画素材**  
  🔗 URL: https://ngabbs.com/read.php?tid=34235326

- **AssetStudio**  
  🔗 URL: https://github.com/Perfare/AssetStudio

- **SpineViewerWPF**  
  🔗 URL: https://github.com/kiletw/SpineViewerWPF

- **cysp**  
  🔗 URL: https://github.com/casuak/cysp

- **公主连结的精灵播放器**  
  🔗 URL: https://github.com/LinXueyuanStdio/AnimPlayer

- **模型预览**  
  🔗 URL: https://wthee.xyz/spine/index.html

<BR>

## ⚖️ 라이센스
이 프로젝트는 [GNU Lesser General Public License v2.1](LICENSE)에 따라 라이선스가 부여됩니다.
