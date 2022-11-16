class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # equal to
    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    # 두 점 사이의 거리
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)


# pointA, pointB 인스턴스화
pointA = Point(2, 6)
pointB = Point(5, 8)

# pointA, pointB 일치 비교
if (pointA == pointB):
    print('Point are equals')
else:
    print('Point are not equals')

# pointA, pointB 거리 출력
print(f'Distance between points are {pointA.distance(pointB)}')
