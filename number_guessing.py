import random
random_number=random.randint(1,100)
print("welcome to number guessing game!!")
count=0
while True:
    user_num=int(input("guess the number: "))
    if (user_num>100) or (user_num<=0):
        print("invalid!!")
    if random_number>user_num:
        print("enter greater!")
        count+=1
    elif random_number<user_num:
        print("enter smaller!")
        count+=1
    else:
        print("guessed right!!!!!")
        break
       
print("your score:",count)




