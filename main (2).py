def user_input(lowest_bid, user_bid, tax_total=0):

  while (user_bid < lowest_bid):
    answer = input("Would you like to bid? y or n?\n")
    if answer == "n":
      print('Goodbye.')
      break
    else:
      user_bid = int(input('What will you bid?\n'))

      if user_bid >= lowest_bid:
        print('You win! you have 24 hrs to pay.\n')
        if user_bid >= 100:
          tax_total = user_bid * 0.05
          tax_total = tax_total + user_bid
          print(
              f'You spent $100 you get free shipping!\nTotal is ${tax_total:.2f}'
          )

        if user_bid < 100:
          tax_total = user_bid * 0.05
          tax_total = tax_total + user_bid + 10
          print(f'Your total after shipping and tax is ${tax_total:.2f}\n')

    if user_bid < lowest_bid:
      print('Sorry your bid is to low. You lose.\n')

  return 0


user_bid = 0
item = input("Please list the Item you would like to put up for auction.\n")
print(f'You are selling an {item}.\n')

lowest_bid = int(
    input(f'What is the lowest amount you will accept for your {item}.\n'))
print(f'Lowest bid is set to ${lowest_bid}.')
user_input(lowest_bid, user_bid, tax_total=0)
