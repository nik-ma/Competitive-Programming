n=int(input())
k=300
#print(n)
def checkn(start,end):
    print((start+end)//2)
    char=input()
    return char
start=1
end=n
for i in range(k):
    char = checkn(start,end)
    if char=='G' and i%2==0:
       start = (start+end)//2
       end=end
    elif char=='G' and i%2!=0: 
        start=start
        end=end
    elif char=='L' and i%2==0:
        start=start
        end=(start+end)//2
    elif char=='L' and i%2!=0: 
        start=start
        end=end
    elif char=="E":
        #print('EQUAL')
        break
if char!='E':
    start=1
    end=n
    for i in range(k):
        char = checkn(start,end)
        if char=='G' and i%2!=0:
            start = (start+end)//2
            end=end
        elif char=='G' and i%2==0: 
            start=start
            end=end
        elif char=='L' and i%2!=0:
            start=start
            end=(start+end)//2
        elif char=='L' and i%2==0: 
            start=start
            end=end
        elif char=="E":
            #print('EQUAL')
            break

    




