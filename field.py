class Field(object):
    # def _init_(self):
    #     self.matrix =
    def generate_matrix(self):
        matrix1 = [0 for i in range(11)]
        matrix2 = [matrix1 for i in range(11)]
        x = [i for i in range(0,11)] ## ось x
        matrix2.append(x)
        a = 10
        for i in matrix2[:-2]:
            i[0] =  a
            print(i)
            a -= 1
        print(matrix2[11])
Field1 = Field()
Field1.generate_matrix()


"""
******** Попытка расположить корабли на карте ******
import random

points = [[x, y] for x in range(1,11)
                for y in range(1,11)]
# print(point)

point = random.choice(points)
used_points = []
#used_points.append(point)
#print(point)
#print(used_points)
print("+"*30)
#points.remove(point)
#print(points)

# direction = random.choice([0,1])
point = [1,2]
direction = 1
if direction == 1: # RIGHT
    for i in range(3):
        print(point)
        used_points.append(point)
        print(used_points)
        print("         ////////////////       ")
        points.remove(point)
        print(points)
        new_point = point[:]
        new_point[0] = new_point[0] + 1
# print(used_points)
# print("@"*50)
# print(points)

"""
