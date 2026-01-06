# for is widely used for iterating over sequence(list,tuple,dictionary,set or string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# loop through string
for x in "banana":
    print(x)

    # can use break, continue statements 
    
    # The range() function 
    for x in range(6):
        print(x)
        # range() returns sequence of numbers starting from 0 and increments by 1 and ends at a specifiend number
        
# nested loops
adj=["red","big","tasty"]
# fruits is already there 
for x in adj:
    for y in fruits:
        print(x,y)