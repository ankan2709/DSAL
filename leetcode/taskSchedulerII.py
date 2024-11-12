def taskschedulerII(tasks, space):

    days = 0
    last_completed = {}

    for task in tasks:
        if task in last_completed and days - last_completed[task] <= space:
            days = last_completed[task] + space + 1

        else:
            days += 1
        last_completed[task] = days


    return days

tasks = [1,2,1,2,3,1]
space = 3
print(taskschedulerII(tasks, space))

tasks = [5,8,8,5]
space = 2
print(taskschedulerII(tasks, space))