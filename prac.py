from cmath import tan
from math import sqrt
from math import atan2
import math


hole = [260, 130]
target = [250, 120]
white = [65, 65]

distance_target_hole = sqrt((abs(hole[0] - target[0]) ** 2 + abs(hole[1] - target[1]) ** 2))
ball_size = 5.73

ratio_dis = ball_size / distance_target_hole # 목적지와 목적구-홀의 비율

x_stick = target[0] * ratio_dis
y_stick = target[1] * ratio_dis
place = []
if target[0] - white[0] > 0 and target[1] - white[1] > 0: # 1사분면
    place = [target[0] - x_stick, target[1]-y_stick]
    degree = atan2(target[1]-y_stick, target[0] - x_stick) * 180 / math.pi
    angle = 90 - degree

elif target[0] - white[0] < 0 and target[1] - white[1] > 0: # 2사분면
    place = [target[0] + x_stick, target[1]-y_stick]
    degree = atan2(target[1]-y_stick - white[1], target[0] + x_stick - white[0]) * 180 / math.pi
    angle = 450 - degree

elif target[0] - white[0] < 0 and target[1] - white[1] < 0: # 3사분면
    place = [target[0] + x_stick, target[1] + y_stick]
    degree = atan2(target[1] + y_stick - white[1], target[0] + x_stick - white[0]) * 180 / math.pi
    angle = -(degree) + 90
    
elif target[0] - white[0] > 0 and target[1] - white[1] < 0: # 4사분면
    place = [target[0] - x_stick, target[1]+y_stick]
    degree = atan2(target[1] + y_stick - white[1], target[0] - x_stick - white[0]) * 180 / math.pi
    angle = -degree + 90
print(place)
print(angle)


# if 목적구x - 흰공x > 0 and 목적구y - 흰공y >0 :
#        angle = 아크탄젠트
# elif 목적구x - 흰공x > 0 and 목적구y - 흰공y <0 :
#        angle = 탄젠트 + 90
# elif 목적구x - 흰공x < 0 and 목적구y - 흰공y <0 :
#        angle = 아크탄젠트 + 180
# else:
#        angle = 탄젠트 + 270



# def getAngle(white, target): # target은 1번공
#     angle = 0
    

x_stick = 2.39374
y_stick = 2.39374
if target[0] - white[0] > 0 and target[1] - white[1] > 0: # 1사분면
    degree = math.atan2(target[1]-y_stick-white[1], target[0] - x_stick - white[0]) * 180 / math.pi
    angle = 90 - degree + 1

elif target[0] - white[0] < 0 and target[1] - white[1] > 0: # 2사분면
    degree = math.atan2(target[1]-y_stick - white[1], target[0] + x_stick - white[0]) * 180 / math.pi
    angle = 450 - degree + 1

elif target[0] - white[0] < 0 and target[1] - white[1] < 0: # 3사분면
    degree = math.atan2(target[1] + y_stick - white[1], target[0] + x_stick - white[0]) * 180 / math.pi
    angle = -(degree) + 90 + 2
    
elif target[0] - white[0] > 0 and target[1] - white[1] < 0: # 4사분면
    degree = math.atan2(target[1] + y_stick - white[1], target[0] - x_stick - white[0]) * 180 / math.pi
    angle = -degree + 90 + 2


print(math.atan2(27, 54) * 180 / math.pi)
print(math.sin((90-math.atan2(27, 54)))*5.74)