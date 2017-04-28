spam = ['apples', 'bananas', 'tofu', 'cats']
spam_message = ''

for x in range(0, len(spam)):
    if x == len(spam)-1:
        spam_message += "and " + spam[x]
    else:
        spam_message += spam[x] + ", "

print (spam_message)
