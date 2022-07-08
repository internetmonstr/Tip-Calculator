#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total=(float(input("What was the total bill? ")))
split=(float(input("How many people split the bill? ₹")))
perce=(float(input("What percentage tip would you like to give? 10, 12 or 15? ₹")))

tip=(total/split) * (perce/100)
amount=(total/split)+tip
amount="{:.2f}".format(amount)
print(f"Each person should pay: ₹{amount}")