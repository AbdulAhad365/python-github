import random
#perry> mimi ikonnl > julia >li-ci
data=[
    {
"name":"Julia Engel","Work": "Lifestyle","Age": 30,"Followers": 1.4
},
    {
"name":"Mimi Ikonnl","Work": "Entrepreneur","Age": 36,"Followers": 2.2
    },
    {
"name":"ahmad","Work": "Photography","Age": 29,"Followers": 1
    },
{
"name":"Li-Chi Pan","Work": "Photography","Age": 28,"Followers": 1.2
},
{
"name":"Michael Perry","Work": "Horticulture","Age": 43,"Followers": 13

},]
def remove_fromlist(d):
    for i in data:
        if i["name"]==d["name"]:
            print("Removed from the list: "+str(i))
            data.remove(i)


x=0
a = random.choice(data)
b = random.choice(data)
# delete_list=[b]
#correct ansert
answer=0
#make sure it will give the distinguish value

while(x<=len(data)-1):
    #choices
    if (len(data)<=1):
        break

    if a["name"] == b["name"]:
        while (a["name"] == b["name"]):
            b = random.choice(data)
    #now start competion
    #name of those will be displayed stored in the a & b
    print()
    print("a) The celebrity is "+a["name"] + " and age is "+str(a["Age"]) +", Moreover is "+a["Work"])
    print()
    print("\t\t\t\t\t\t VS")
    print()
    print("b) The celebrity is " + b["name"] + " and age is " + str(b["Age"]) + ", Moreover is " + b["Work"])
    print()


    store=(input("Guess which one has more insta followers: Type 'a' for option 1 and 'b' for option2:"))
    #a and be are given
    if store=='a':
        if a["Followers"]>b["Followers"]:
            remove_fromlist(b)
            b=random.choice(data)
        else:
            print("Wrong answer")
            break
    elif store=='b':
        if b["Followers"]>a["Followers"]:
            remove_fromlist(a)
            a=random.choice(data)
        else:
            print("Wrong answer")
            break
    #Now, verify the answer

