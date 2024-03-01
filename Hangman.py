import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
position = 0

arr = ["ahad", "welcome", "sohail"]
i = random.choice(arr)
# num of the messege displaced in the input bar
num = random.randint(2, (int(len(i) / 2)))
iii = 0

# now between them

l = []
for x in i:
    l.append("_")
while iii < num:
    a = random.randint(0, len(i) - 1)
    l[a] = i[a]

    iii = iii + 1
print(l)

# for x in i:
#     if name==x:
#         # print(name,end=" ")
#         l[it]=name
#
#     it=it+1

boo=True
while (boo) :
    for x in l:
        if(x=="_"):
            boo = True
            break

        else:
            boo=False

    if boo==False:
        break
    name = input("Guess the letter")
    it = 0
    checker=False
    for x in i:
        if name==x:
            # print(name,end=" ")
            l[it]=name
            checker=True

        it=it+1
    if not checker:
        lives=lives-1
        position=position+1
        print("Your life is "+str(lives))
        print(stages[position])
    if(lives==0):
        break
    print(l)
