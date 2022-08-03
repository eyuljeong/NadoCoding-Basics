# sep
print("Python" + "Java")
print("Python", "Java", "JavaScript", sep = " vs ")

# end
print("Python", "Java", sep = ",", end = "? ")
print("무엇이 더 재밌을까요?")

# sys
import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

# 좌우로 정렬 좌우로 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# input
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # input 은 항상 str 로 출력
print("입력하신 값은 {0} 입니다.".format(answer))