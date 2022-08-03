class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
    

class FlyableUnit(Flyable, Unit): 
    def __init__(self):
        super().__init__() # super 는 첫 메소드만 호출, self 쓸 필요 없음
        Unit.__init__(self) # 따라서 뒤에 나오는 Unit.__init__ 을 호출해줘야함

# 드랍쉽
dropship = FlyableUnit()