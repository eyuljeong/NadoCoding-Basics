gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용. 코드 관리 어려워짐 -> 비추
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers): # 추천 코드
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2)