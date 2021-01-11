import math

ab = float(input())
bc = float(input())
answer = int(round(math.degrees(math.atan2(ab, bc))))
print(str(answer)+"°")
