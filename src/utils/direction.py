from math import atan2, pi


class DIRECTION:
    FORWARD = "FORWARD"
    FORWARD_RIGHT = "FORWARD_RIGHT"
    FORWARD_LEFT = "FORWARD_LEFT"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    BEHIND = "BEHIND"
    BEHIND_RIGHT = "BEHIND_RIGHT"
    BEHIND_LEFT = "BEHIND_LEFT"


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def angle(self, x, y):
        dx = x - self.x
        dy = y - self.y

        return atan2(dy, dx) * (180 / pi)

    def direction(self, directionX, directionY, x, y):
        myAngle = self.angle(directionX, directionY)
        print("MyAngle: ", myAngle)

        newCoordinate = Coordinate(directionX, directionY)
        angle = newCoordinate.angle(x, y)
        print("Angle: ", angle)

        directionAngle = angle - myAngle
        print("Direction Angle: ", directionAngle)

        while directionAngle < 0:
            directionAngle = directionAngle + 360
        print("Direction Angle: ", directionAngle)

        pie = 360 / 8
        pie2 = pie / 2

        print("Pie: {}, Pie2: {}".format(pie, pie2))

        direction_map = [
            DIRECTION.FORWARD,
            DIRECTION.FORWARD_LEFT,
            DIRECTION.LEFT,
            DIRECTION.BEHIND_LEFT,
            DIRECTION.BEHIND,
            DIRECTION.BEHIND_RIGHT,
            DIRECTION.RIGHT,
            DIRECTION.FORWARD_RIGHT,
            DIRECTION.FORWARD
        ]

        for x in range(8):
            if directionAngle < pie2 + pie * x:
                return direction_map[x]

        return direction_map[-1]

#k1 = Coordinate(0, 0)
#d = k1.direction(0, 5, 0.1, 0)
#print(d)
