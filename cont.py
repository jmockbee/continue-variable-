# Prompt the user to enter a word
# and assign it to the user_word variable.

#for letter in user_word:
    # Complete the body of the for loop.

user_word = input('Type a word: ')
user_word = user_word.upper()
for i in user_word:
    if (i == 'A' or i=='E' or i=='O' or i=='U' or i=='I'):
        continue
    print (i)



