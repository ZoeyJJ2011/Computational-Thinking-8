fish_points = 0
dog_points = 0

answer = input("On a weekend would you rather A) play sports all day, or B) hangout and chill?\n")
if answer == "A": 
    fish_points += 1 
elif answer == "B": 
    dog_points += 1


answer = input("which place would you rather fly to A) the bahamas, or B) Japan?\n")
if answer == "A": 
    dog_points += 1 
elif answer == "B": 
    fish_points += 1

answer = input("which is better? A) hot coco, or B) eggnog?\n")
if answer == "A": 
    dog_points += -1 
elif answer == "B": 
    fish_points += 1

answer = input("would you rather? A)talk to yoda , or B)talk to daffy duck ?\n")
if answer == "A": 
    dog_points += 1 
elif answer == "B": 
    fish_points += 1


answer = input("you have a bully at school? A)are you going to fight them, or B)be a snitch and tell on them ?\n")
if answer == "A": 
    fish_points += 1 
elif answer == "B": 
    dog_points += -1

if fish_points > dog_points:
    print("you are a fish person")
elif dog_points > fish_points: 
    print(" you are a dog person")
elif fish_points== dog_points:
    print("you like fish and dogs the same")

