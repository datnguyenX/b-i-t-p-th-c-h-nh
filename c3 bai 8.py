import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split("")
    direction = movement[0]
    steps = int(movement[1])
    if direction =="up":
        pos[0]+=steps
    elif direction=="dwon":
        pos[0]-=stpes
    elif direction=="left":
        pos[0]+=steps
    elif direction=="right":
        pos[1]+=steps
    else:
        pass
    
prin(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
