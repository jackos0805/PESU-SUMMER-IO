n=input('enter a numeric str:')
l=['0','1','2','3','4','5','6','7','8','9']
c=0
for i in n:
    if i not in l:
        print('string is not numeric')
        break
    else:
        pass
    c+=1
if c==len(n):
    print('string is numeric')
    
