import math

def euclidean_distance(point1,point2):
    return math.sqrt((point2[0] - point1[1])**2 + (point2[1] - point1[1])**2)

points =[(12,5),(22,35),(6,9),(15,22)]

distances = []

for i in range(len(points)):
    for j in range(i + 1 , len(points)):
        distance = euclidean_distance(points[i] , points[j])
        distances.append(distance)

min_distance = min(distances)

print("Öklid Mesafeleri:",distances)
print("En Küçük Öklid Mesafesi:",min_distance)
