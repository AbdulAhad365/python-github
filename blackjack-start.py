import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user=0
dealer=0
# for the dealer
for x in range(0,2):
    sum=int(random.choice(cards))
    dealer=dealer+sum
for x in range(0,2):
    sum=int(random.choice(cards))
    user=user+sum
print("=> RULES ARE SIMPLE IF VALUE OFN DEALER OR THE USER GETS >21 THEN HE WILL CHOOSE SO CHOOSE YOUR DECISION CAREFULLY")
print("dealer: "+str(dealer))
print("User: "+str(user))
#now the main logic
choice=True
while(choice):
    #choice
    if user==21:
        choice=False
    choice=input("Do you want to make a bid 'T' for True 'F' for False: ").lower()
    if(choice=='t'):
        sum=int(random.choice(cards))
        user=user+sum
        print("user = "+str(user))

        if user>21:
            print("You have lost the game user your net score is "+str(user))
            choice=False
        else:
            continue
    else:
        print("Your net score is "+str(user))
        break
#Now the dealer turn
choice=True
go=False
ch=["go","stop"]
while(choice):
    if dealer==21 and dealer==20:
        choice=False
    else:
        if dealer<=15:
            go=True

        elif dealer>15:
            my_wish=random.choice(ch)
            if my_wish=='go':
                choice=True
            else:
                choice=False


        if go:
            sum=int(random.choice(cards))
            dealer=dealer+sum
if dealer<=21 and dealer>user:
    print("Dealer has won")
elif dealer==user:
    print("its a tie")
else:
    print("User has won")
print("dealer: "+str(dealer))
