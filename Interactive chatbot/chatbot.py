# Chatbot with personality
# Mike Kim
# Jan.13 2022

'''
This chatbot will help customers order their food at the restaurant.
'''
# Total price 
total_price = 0

# Greet User + Get their name
customer_name = input("Welcome to Burger Cuisine! What is your name?")
print("Nice to meet you, " + customer_name + "!")

# Show them the menu
combos = input("Here are the list of menus: \n \
Please reply with a number. \n \
1: Cheeseburger combo ($10)\n \
2: Fish burger combo ($9) \n \
3: Double cheeseburger combo ($12) \n \
4: Spicy chicken sandwich combo ($10) \n ") 

# Response based on their choice of combos
if combos == "1" or combos == "one":
  total_price += 10
  print("Cheeseburger combo! That's what we're known for!")
elif combos == "2" or combos == "two":
  total_price += 9
  print("Fish burger combo! That's a solid choice!")
elif combos == "3" or combos == "three":
  total_price += 12
  print("Double cheeseburger combo! \n \
  This is perfect when you are extremely hungry!")
elif combos == "4" or combos == "four":
  total_price += 10
  print("Spicy chicken sandwich combo is perfect \n \
   when you are craving something spicy!")
else:
  print("Sorry, the combo that you have requested is not in our menu.")

# Sides (french fries)
french_fries = input("Which size of french fries would you like? \
 We have medium and large.\
 Medium comes with the menu by default and \
 large would cost you a dollar extra.")

# Response 
if french_fries == "medium" or french_fries == "Medium":
  print("Medium it is!")
elif french_fries == "large" or french_fries == "Large":
  total_price += 1
  print("One large fries! I'll keep that in mind.")
else:
  print("Sorry, you have entered an invalid size for french fries.")

# Beverages (fountain drink or milkshake)
beverages = input("What would you like to drink?\
 We have milkshake(1 dollar extra) \n \
 and fountain drinks.")

#Response
if beverages == "milkshake" or beverages == "Milkshake":
  total_price += 1
  print("I'll swap out the fountain drink with milkshake.")
else:
  print("Fountain drink it is!")

# Paying
payment = input("Alright, " + customer_name + "! Are you ready to pay? (type 'yes' when you are ready.)")
if payment == "yes" or payment == "Yes":
  print("Your total is:" , (total_price*1.14) , \
  "! Again, thank you for choosing Burger Cuisine! Enjoy your meal :)")