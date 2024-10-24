import random
while True:
    rps=input("choice: r(rock) p(paper) s(sissor)")
    print("computer choose: ")
    choice = random.choice(['r','p','s'])
    print(choice)
    if rps==choice:
        print("both choose same tie!")

    elif (rps=='r' and choice =='s') or (rps=='s' and choice=='r')or (rps=='p' and choice=='r'):
        print("you won!! :)")
    else:
        print("you lose :(")
    print("do you wanna continue?")
    yn=input("yes/no" )
    if yn=='no':
        break
         
