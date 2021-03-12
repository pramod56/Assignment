def print_pattern(n):
    k=2*n-2
    for i in range(1,n+1):
        for j in range(0,k):
            print(" ",end="")
        k=k-2
        for ele in range(1,i+1):
            print("*",end=" ")
        print()
        
def alphabet(n):
    print()
    num=65
    for i in range(1,n+1):
        for j in range(1,i+1):
            char=chr(num)
            print(char,end=" ")
            num=num+1
        print()
            
            
    
if __name__=="__main__":
    n=int(input("enter the number of rows: "))
    print_pattern(n)
    alphabet(n)
