for row in range(3,0-1,-1):
    for col in range(4):
        if row <= col:
            print(row + col,end=" ")
        else:
            print(" ",end=" ")    
    print()        