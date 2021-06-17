array = [int(i) for i in input().split()]

ptr1 = ptr2 = array[len(array)//2]

sum1 = sum(array[:ptr1])
sum2 = sum(array[ptr2:])
sum3 = array[len(array)//2]
while 1:
    if sum1 > sum2:
        if sum1 > sum3:
            ptr1 -= 1
            sum1 -= array[ptr1]
        else:
            sum



    