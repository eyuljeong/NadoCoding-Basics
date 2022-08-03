# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random)) # random 함수 상세 정보

lst = [1,2,3]
print(dir(lst)) # 리스트에서 쓸 수 있는 것

name = "Jim"
print(dir(name)) # 문자열에서 쓸 수 있는 것

# Built-in Functions 참고