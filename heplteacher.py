for _ in range(int(input())):
    q=int(input())
    marks=[]
    s_new=[]
    for i in range(q):
        s=input()
        s_new.append(s)
        if s[len(s)-3:]=="100":
            marks.append(int(s[len(s)-3:]))
        else:


            marks.append(int(s[len(s)-2:]))
    avg=sum(marks)/q
    #print(avg)
    marks2=marks[:]
    marks2.sort()
    stry=set()
    #print(marks2)
    #print(marks)
    j=0
    marks2.append(1000000000)
    for i in range(q):
        if marks2[i]<avg:
            #print(marks.index(marks2[i]))
            
                print(s_new[marks.index(marks2[i])])
                #marks.pop(marks.index(marks2[i]))
                marks[marks.index(marks2[i])]=-1

                #print(s_new[marks.index(marks2[i])])
                
                #print(s_new)
    
            
    
        