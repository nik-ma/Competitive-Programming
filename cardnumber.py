tc = int(input())
while tc:
    n=[int(i) for i in input()]
    j=0
    for i in n :
        
        if i.isdigit()==0 or (i=='-' and i%4==0):
            print('Valid')
    
        j+=1   