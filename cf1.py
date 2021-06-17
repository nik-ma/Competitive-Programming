
for _ in range(int(input())):
    s=input()
    s=s.lower()
    c=0
    if 'berhampore' in s:
        c+=1
        #print('GCETTB')
    if 'serampore' in s:
        c+=1
        #print('GCETTS')
    if c==2:
        print('both')
    if c==0:
        print('others')
    if c==1:
        if 'berhampore' in s:
        
            print('GCETTB')
        if 'serampore' in s:
        
            print('GCETTS')

    
    