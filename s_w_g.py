import random
import time

def game(a,b):
    if a == b:
        return None
    elif a=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif a=='w':
        if b=='s':
            return True
        elif b=='g':
            return False
    elif a=='g':
        if b=='w':
            return True
        elif b=='s':
            return False
     
# print("computer turn:\n")
# b=input("players turn: Snake(s),Water(w),Gun(g)?\n")
# randomno= random.randint(1,3)
# if randomno == 1:
#      a='s'
# elif randomno == 2:
#     a='w'
# else:
#     a='g'

# c=game(a,b)
# print(f"Bot ne {a} select kelay\n")
# if c== None:
#     print("Draw zala na\n")
# elif c:
#     print("Jeet Gaye!!!!!!!")
# else:
#     print("Harla na rao ):")

r=int(input("kiti round cha game zala pahije 3,5,7\n"))
Bot=0
You=0
Round=1
for i in range (r):
    print(f"Round = {Round}")
    randomno= random.randint(1,3)
    #print(randomno)
#options = ['s', 'w', 'g']
#randomno=random.choice(options)
    if randomno == 1:
        a='s'
    elif randomno == 2:
        a='w'
    else:
        a='g'
    print("computer turn:\n")
    time.sleep(1)
    b=input("players turn: Snake(s),Water(w),Gun(g)?\n")
    c=game(a,b)
    print(f"Bot ne {a} select kelay\n")
    if c== None:
        time.sleep(1)
        print("Draw zala na\n")
        You=You
        Bot=Bot
    elif c:
        time.sleep(1)
        print("Jeet Gaye!!!!!!!\n")
        You=You+1
    else:
        time.sleep(1)
        print("Bot jinklay\n")
        Bot=Bot+1
    #print(f"{You},{Bot}")
    Round = Round+1
    time.sleep(1)
    

print("Final result Yetayet........Wait\n\n")
if(You>Bot):
    time.sleep(2)
    print("Saglya rounds Nantar antim vijete apan ahat\n")
elif(You==Bot):
    time.sleep(2)
    print("It's Tie\n")
else:
    time.sleep(2)
    print("Evdya saglya Dhadpadinantarsuddha Bot jinkla\n")


    