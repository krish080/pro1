n1=''
n2=''
def Swap(n1,n2):
    d1=''
    d2=''
    with open(f'{n1}.txt','r')as f:
        d1=f.read()
    with open(f'{n2}.txt','r')as f:
        d2=f.read()    
    with open(f'{n1}.txt','w')as f:
        f.write(d2)
    with open(f'{n2}.txt','w')as f:
        f.write(d1)

print('hello')
             
n1=input("enter the name of file 1 : ")
n2=input("enter the name of file 2 : ")
Swap(n1,n2)