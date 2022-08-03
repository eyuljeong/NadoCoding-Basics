# 쓰기
score_file = open("score.txt", "w", encoding = "utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

# 추가
score_file = open("score.txt", "a", encoding = "utf8") 
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

# 읽기 1
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read()) # 파일 전체 불러오기
score_file.close()

# 읽기 2
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()

# 읽기 3
print("\n")
score_file = open("score.txt", "r", encoding = "utf8")
while True: # 파일이 몇줄인지 모를 때
    line = score_file.readline()
    if not line: # 줄이 없다면
        break # while 문 탈출
    print(line, end = "")
score_file.close()

# 읽기 4
print("\n")
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()