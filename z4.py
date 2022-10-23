from random import Random, randint

N = int(input('Введите число '))
num = []
for i in range(N):
    num.append(randint(-N,N+1))
print(num)

def mix(num):
    list = num[:]
    num_length = len(list)
    for i in range(num_length):
        index = randint(0, num_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(mix(num))