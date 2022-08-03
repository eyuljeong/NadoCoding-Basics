python = "Python is Amazing"
print(python.lower()) # 소문자로 변환
print(python.upper()) # 대문자로 변환
print(python[0].isupper()) # 0 번째 문자가 대문자인가?
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 교체

where = python.index("n") # 위치 찾기
print(where)
where = python.index("n", where + 1) # 첫 문자의 위치 이후부터의 문자의 위치
print(where)

print(python.find("Java")) # 원하는 값이 없으면 -1 출력
# print(python.index("Java")) # 원하는 값이 없으면 오류

print(python.count("n")) # 개수