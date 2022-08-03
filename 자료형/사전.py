cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# print(cabinet[5]) # Key 가 없다면 오류
print(cabinet.get(5)) # Key 가 없다면 None 출력

print(cabinet.get(5, "사용 가능")) # Key 가 없다면 뒤의 값 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) # Key 들만 출력
print(cabinet.values()) # Value 들만 출력
print(cabinet.items()) # Key, Value 쌍으로 출력

# 목욕탕 폐점
cabinet.clear()
print(cabinet)