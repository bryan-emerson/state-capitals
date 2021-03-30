from capitals import states
import random

#print(states)

score = {"Correct": 0, "Incorrect": 0}
# print(score)

print("Greetings! How well do you know the geography of the United States? Guess the capitals of each state and test your knowledge!")

random.shuffle(states)
#print(states)

num_list = list(range(50))
#print(num_list)



def play():
  for n in num_list:
    answer = input("what is the capital of " + states[n]["name"] +": ")
    if answer == states[n]["capital"]:
      score["Correct"] = score["Correct"] + 1
    elif answer != states[n]["capital"]:
      score["Incorrect"] =  score["Incorrect"]+ 1
    print(score)

  print("Your Final Score is " + str(score["Correct"]))
  choice = input("Would you like to plat again? Yes (y) or No (n)")
  if choice == "y":
    score["Correct"] = 0
    score["Incorrect"] = 0
    play()
  else:
    print("Thanks for Playing!!!")

play()

# print("Your Final Score is " + str(score["Correct"]))

# choice = input("Would you like to plat again? Yes (y) or No (n)")
# if choice == "y":
#   score["Correct"] = 0
#   score["Incorrect"] = 0
#   play()
# else:
#   print("Thanks for Playing!!!")
