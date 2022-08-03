absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡함

for student in range(1, 11): # 1 부터 10
    if student in absent: # student 가 absent 안(in)에 있다면...
        continue
    elif student in no_book: # student 가 no_book 안(in)에 있다면...
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 남은 반복문과 관계없이 종료
    print("{0}, 책을 읽어봐".format(student))