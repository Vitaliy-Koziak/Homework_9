"""У змінній записаний текст. Словом вважається послідовність непорожніх символів, які йдуть
підряд, слова розділені одним або більше пробілом.

Програмно створіть словник, в якому ключами є слова з речення, а значеннями – кількість
входження в речення."""

str = input("Enter string:  ")

symbols = ['.',',','!','?',';',':',')','(']
for symbol in symbols:
    if symbol in str:
        str = str.replace(symbol,'')

str = str.lower()
str_list = str.split()

dictionary = {}

for item in str_list:
    dictionary[item] = str_list.count(item)

for key,value in dictionary.items():
    print(key," : ",value)










