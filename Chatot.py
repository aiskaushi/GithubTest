name = input("Hii I am Anant,may i know youe name please:")
print("Nice to meet you "+name)
place=input("Which school are you from? ")
print(place+ " is a nice school. I have a friend there")
Class =input("In which class do you read?")
print("I steady in class "+Class)
sports=input(name+" Do you play cricket? ")
# if sports=="yes":
#     print("We play cricket in the school play ground every evening. you can join us")
# else:
#     print("What is your favourite sport")
sport=input("What is your favourite sport? ")
if sport=="football":
    print("I like football too")
    play=input("We have a match today at 5.30pm. Would you like to play?")
    if play=="yes":
        print("Let's meet in the school play ground in the evening")
    else:
        print("Not an isuue. We can meet some other time")
   
elif sport == "Hockey":
    print("I dont like Hockey,I like football. I have  a friend who plays hockey")
    play=input(" Would you like to play in their team?")
    if play=="yes":
        print("I will introduce him in the school play ground in the evening")
    else:
        print("Not an isuue. We can meet some other time")
elif sport == "Badminton":
    print("Its a nice game but i lie only football") 
elif sport == "Cricket":
    print("I dont like Cricket,I like football")
elif sport == "Basketball":
    print("I hate Basketball but i like footballo")
else:
    print("")
