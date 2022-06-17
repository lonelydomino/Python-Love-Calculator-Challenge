# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score = 0
score += name1.lower().count('t')
score += name2.lower().count('t')
score += name1.lower().count('r')
score += name2.lower().count('r')
score += name1.lower().count('u')
score += name2.lower().count('u')
score += name1.lower().count('e')
score += name2.lower().count('e')

score2 = 0
score2 += name1.lower().count('l')
score2 += name2.lower().count('l')
score2 += name1.lower().count('o')
score2 += name2.lower().count('o')
score2 += name1.lower().count('v')
score2 += name2.lower().count('v')
score2 += name1.lower().count('e')
score2 += name2.lower().count('e')

finalString = str(score) + str(score2)

if int(finalString) < 90 or int(finalString) < 10:
  print(f"Your score is {finalString}, you go together like coke and mentos.")
elif int(finalString) < 40 and int(finalString) < 50:
  print(f"Youre score is {finalString}, you are alright together.")
else:
  print(f"Your score is {finalString}.")

