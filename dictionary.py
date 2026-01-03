thisdict={
    "brand": "Ford",  #dictionary is a collection of prdered*, changeable and do not allow duplicates
    "model":"Muatang", #key:value 
    "year":1964
} 
# accessing items
print(thisdict["brand"])  #output: Ford")
print(thisdict.get("model"))  #output: Muatang
# change values
thisdict["year"]=2020
print(thisdict["year"])  #output: 2020
# loop through dictionary
for x in thisdict:
    print(x)  #output: brand, model, year (keys)
    for c in thisdict:
        print(thisdict[c])  #output: Ford, Muatang, 2020 (values)
        # adding items
        thisdict["color"]="red"
        print(thisdict)  #output: {'brand': 'Ford', 'model': 'Muatang', 'year': 2020, 'color': 'red'}
        # removing items
        thisdict.pop("model")
        print(thisdict)  #output: {'brand': 'Ford', 'year': 2020, 'color': 'red'}
        del thisdict["year"]
        print(thisdict)  #output: {'brand': 'Ford', 'color': 'red'}

        # loop dictionary items
        for key,value in thisdict.items():
            print(key,value)  #output: brand Ford, color red    

            # copy dictionary
            newdict=thisdict.copy()
            print(newdict)  #output: {'brand': 'Ford', 'color': 'red'}

            # nested dictionary
            # type 1 
            myfamily={
                "child1":{
                    "name":"Emil",
                    "year":2004
                },
                "child2":{
                    "name":"Tobias",
                    "year":2007
                },
                "child3":{
                    "name":"Linus",
                    "year":2011
                }
            }
        #   type 2
        child1={
            "name":"Emil",
            "year":2004
        }
        child2={
            "name":'Tobias',
            "year":2007
        }
        child3={
            "name":"linus",
            "year":2011
        }
        myfamily={
            "child1":child1,
            "chilld2":child2,
            "child3":child3
        }
        #accessing nested dictionary
        print(myfamily["child1"]["name"])
        print(myfamily)
        #loop through nested dictionary 
        for x,obj in myfamily.items():
            print(x)

            for y in obj:
                print(y+":",obj[y])


                 # dictionary methods
        print(thisdict.keys())  #output: dict_keys(['brand', 'color'])
        print(thisdict.values())  #output: dict_values(['Ford', 'red'])
        print(thisdict.items())  #output: dict_items([('brand', 'Ford'), ('color', 'red')])
        print(thisdict.clear())#removes all the elements from the dictionary 
