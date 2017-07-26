ask = raw_input('Insert the word\n')

ask_reverse = ''

y = len(ask)-1

for x in range(0,len(ask)):
    ask_reverse = ask_reverse + ask[y-x]

if ask_reverse is ask:
    print(ask + "it's a palindrome")
else:
    print(ask + "it isn't a palindrome")






