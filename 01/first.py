import fileinput

lines = [line.rstrip() for line in fileinput.input()]

list1 = []
list2 = []

for line in lines:
    first, second = line.split()
    list1.append(int(first))
    list2.append(int(second))

list1.sort()
list2.sort()

distance = 0

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])


print(distance)
