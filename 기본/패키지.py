# 패키지에서 모듈 호출
import travel.thailand # 모듈이나 패키지만 import 할 수 있음
# import travel.thailand.ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 클래스나 함수 호출
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

# 공개 범위 설정 : __init__.py
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 패키지, 모듈 위치 확인
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))