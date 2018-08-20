#You are the manager of a supermarket.
#You have a list of  items together with their prices that consumers bought on a particular day.
#Your task is to print each item_name and net_price in order of its first occurrence.

#item_name = Name of the item.
#net_price = Quantity of the item sold multiplied by the price of each item.

#Input Format
#The first line contains the number of items, .
#The next  lines contains the item's name and price, separated by a space.

#Output Format
#Print the item_name and net_price in order of its first occurrence.

#Sample Input
#9
#BANANA FRIES 12
#POTATO CHIPS 30
#APPLE JUICE 10
#CANDY 5
#APPLE JUICE 10
#CANDY 5
#CANDY 5
#CANDY 5
#POTATO CHIPS 30

#Sample Output
#BANANA FRIES 12
#POTATO CHIPS 60
#APPLE JUICE 20
#CANDY 20

from collections import OrderedDict
ordered_dictionary = OrderedDict()
for goods in range(int(input())):
    fullname = input().split()
    price = int(fullname[-1])
    name = " ".join(fullname[:-1])
    try:
        ordered_dictionary[name] += int(price)
    except:
        ordered_dictionary[name] = int(price)
for ements,costs in ordered_dictionary.items():
    print(ements, costs)
