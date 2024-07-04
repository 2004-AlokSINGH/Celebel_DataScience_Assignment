# Create lower triangular, upper triangular and pyramid containing the "*" character.

def pattern(n):
  
    print("Lower triangular pattern")
  
    for i in range(1,n+1):
        print("*"*(i))
        
    print("Upper triangular pattern")
  
    for i in range(n,0,-1):
        print(" "*(n-i)+"*"*(i))
        
    print("pyramid")
  
    for i in range(1,n+1,2):
        print(" "*((n-i)//2)+"*"*i)

pattern(6)
