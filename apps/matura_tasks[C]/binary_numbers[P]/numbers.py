""" File with all of the solutions to the task matura_tasks[C]/binary_numbers[P] """

# TASK 1
def task_1():
    """ Returns number of lines in file 'numbers.txt' that have more zeros than ones. """

    f = open("numbers.txt", "r")
    z = 0
    for x in f:
        i = [0, 0]
        for y in x:
            if (y.isnumeric()):
                i[int(y)]+=1
        if (i[0]>i[1]):
            z+=1
    return z

# TASK 2
def task_2():
    """ Returns number of lines in file 'numbers.txt' that are divisible by 2 and 8. """

    f = open("numbers.txt", "r")
    z = 0 #liczby podzielne przez 2
    k = 0 #liczby podzielne przez 8
    for x in f:
        if (int(x,2)%2==0):
            z+=1
        if (int(x,2)%8==0):
            k+=1
    return [z,k]

# TASK 3
def task_3():
    """ Returns the lines in file 'numbers.txt' that have the smallest and the biggest number. """

    f = open("numbers.txt", "r")
    z = []
    for x in f:
        z.append(int(x,2))
    return [z.index(min(z))+1, z.index(max(z))+1]

odp1 = task_1()
odp2 = task_2()
odp3 = task_3()

print(str(odp1)+" numbers have more zeros than ones in the binary notation")
print(str(odp2[0])+" numbers divisible by 2")
print(str(odp2[1])+" numbers divisible by 8")
print("in the "+str(odp3[0])+" line is the smallest number")
print("in the "+str(odp3[1])+" line is the largest number")
