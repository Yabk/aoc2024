import fileinput

def is_safe(report) -> bool:
    if sorted(report) == report or sorted(report, reverse=True) == report:
        safe_flag = True
        for i in range(len(report)-1):
            diff = abs(report[i]-report[i+1])
            if diff < 1 or diff > 3:
                safe_flag = False
                break
        if safe_flag:
            return True
    return False


def with_dampener(report) -> bool:
    reports = []
    for i in range(len(report)):
        reports.append(report[:i]+report[i+1:])
    for r in reports:
        if is_safe(r):
            return True
    return False




lines = [line.rstrip() for line in fileinput.input()]
parsed = [[int(c) for c in line.split()] for line in lines]

safe = 0

for line in parsed:

    if with_dampener(line):
        safe += 1



print(safe)

