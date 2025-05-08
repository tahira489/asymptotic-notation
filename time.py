def printnumber(n):
    literation = 0
    print("the total number entered by the user is",n)
    literation+=1
    print("total literation will be",literation)

printnumber(20)
printnumber(50)

print("the time taken will not change for every n")
#best case scenario
#time complexity = O(1)

def display(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("the total iteration will be", iteration)

display(10)
display(20)
print("the time taken will increase linearly")
#average case scenario
#time complexity = O(n)

def test(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1
        print("")
    print("the total iteration will be",iteration)

test(4)
test(2)
print("time taken will increase quadritely")
