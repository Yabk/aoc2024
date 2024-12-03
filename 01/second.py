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

similarity = 0

for num in list1:
    similarity += num * list2.count(num)



print(similarity)
