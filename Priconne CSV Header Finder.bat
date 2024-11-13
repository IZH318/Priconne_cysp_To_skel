@echo off
TITLE Priconne CSV Header Finder
echo.
echo. ===== Welcome to Priconne CSV Header Finder =====
echo. A tool to search and copy CSV files for Princess Connect! Re: Dive based on specific headers.
echo.
echo. [ WARNING ]
echo. Please ensure that the path does not contain spaces when running the batch file.
echo. Unexpected errors may occur if there are spaces in the path.
echo.
echo.
echo.

REM Directory to search in
set DIRECTORY=.
setlocal enabledelayedexpansion

REM Define search strings for each category
set "Search_Character_Header=63b62d72f43f1ee9d3ffa6528fd788c4c05ab9bf3be4046fa0c670308ffda877 758a833b38682617eb99c0e50e138a1e08008740c69a2a1e1fe3eaa6e913f894 556944d17c3dccfdac0aa708e6e713008a0ed10956c307cca8a49dffa26d09a8"
set "Search_Boss_Header=5f6902a3cabd407a699ecbadbce41011b4703d685e80a48d3a51f5c3d44f3b7b 52c55fdb9c4384a8ba7151004585a3dfc2a464c71a3dc3d229fd33d6947331cd 42409c8a6a41c132c614b19c7171cc886b6bb65c172e9aec0406d143d4f27672"
set "Search_Nebbia_ID_Header=9e7e08f2eb6ecb3955d4e5488835e791a3d55869d1a7ca49c35f0a079be4771d 2ade35e1ce2dd7a2d3fd37d4adc92149b8054b798f5adc813257047567894f9f"

REM Find files matching 'v1_' prefix and '.csv' extension
echo. [Info] Searching for files that start with "v1_" and end with ".csv"...

REM Create temporary list of matching files
for /r %DIRECTORY% %%F in (v1_*.csv) do (
    set file=%%F
    set found=false
    REM Check for Character Header in the file
    for %%s in (%Search_Character_Header%) do (
        findstr /i /c:"%%s" "!file!" >nul && set found=true
    )
    if !found!==true (
        echo.
        echo.
        echo.
        echo. [Info] File found with Character Header: !file!
        set Character_Header_Include=!file!
    )
)

REM Repeat above block for Boss Header and Nebbia ID Header
REM For Boss Header
for /r %DIRECTORY% %%F in (v1_*.csv) do (
    set file=%%F
    set found=false
    for %%s in (%Search_Boss_Header%) do (
        findstr /i /c:"%%s" "!file!" >nul && set found=true
    )
    if !found!==true (
        echo.
        echo. [Info] File found with Boss Header: !file!
        set Boss_Header_Include=!file!
    )
)

REM For Nebbia ID Header
for /r %DIRECTORY% %%F in (v1_*.csv) do (
    set file=%%F
    set found=false
    for %%s in (%Search_Nebbia_ID_Header%) do (
        findstr /i /c:"%%s" "!file!" >nul && set found=true
    )
    if !found!==true (
        echo.
        echo. [Info] File found with Nebbia ID Header: !file!
        set Nebbia_ID_Header_Include=!file!
        echo.
        echo.
        echo.
    )
)

REM Ask user whether they want to copy the files
echo. [Info] Do you want to create copies of all the files? ([Y]: Yes, [N]: No)
set /p user_input=" >>> "
echo.
echo.
echo.
if /i "%user_input%"=="Y" (
    REM Copy Character Header files
    if defined Character_Header_Include (
        call :copy_files "!Character_Header_Include!" "Character.csv"
    )
    
    REM Copy Boss Header files
    if defined Boss_Header_Include (
        call :copy_files "!Boss_Header_Include!" "Boss.csv"
    )

    REM Copy Nebbia ID Header files
    if defined Nebbia_ID_Header_Include (
        call :copy_files "!Nebbia_ID_Header_Include!" "Nebbia_ID.csv"
    )

    echo.
    echo.
    echo. [Info] All tasks have been completed.
    echo.
)

pause
exit /b

REM :copy_files function - Handles file copying and renaming (no overwrite)
:copy_files
set file=%1
set target=%2

REM Check if file exists
if exist "%target%" (
    REM If the file already exists, rename it by adding _number to the filename
    call :get_new_file_name %target%
) else (
    REM If the file does not exist, copy it normally
    copy "%file%" "%target%" >nul
    echo. [Info] Copying %file% to %target%
    echo.
)
goto :eof

REM :get_new_file_name function - Handles renaming files if they already exist
:get_new_file_name
set target=%1
set base=%~dp1
set filename=%~n1
set ext=%~x1
set counter=1

:rename_loop
REM Here, we append _counter to the filename, so it will be like filename_1.csv, filename_2.csv, filename_3.csv
set new_target=%base%%filename%_%counter%%ext%
if exist "%new_target%" (
    set /a counter+=1
    goto :rename_loop
)

copy "%file%" "%new_target%" >nul
echo. [Info] Renaming file to "%new_target%"
echo.
goto :eof
