# Python Module Index 참고

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리
print(os.listdir()) # 현재 경로 내 폴더 / 파일 목록 조회

folder = "sample_dir"

if os.path.exists(folder): # sample_dir 이란 폴더가 있다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 지우기
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")



# time : 시간 관련 함수
import time
print(time.localtime()) # 현재 시간
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-달-일 시-분-초

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days = 100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후