# 빈 자리는 빈공간, 오른쪽 정렬, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸 _로 채우기
print("{0:_<+10}".format(500))

# 3자리 마다 쉼표 찍기
print("{0:,}".format(100000000000))

# 3자리 마다 쉼표 찍기, +- 부호 붙이기
print("{0:+,}".format(-100000000000))

# 3자리 마다 쉼표 찍기, +- 부호 붙이기, 자릿수 확보, 빈 자리는 ^
print("{0:^<+30,}".format(-100000000000)) # 순서 주의

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (소수점 2째 자리까지)
print("{0:.2f}".format(5/3))