#writing to  files
#whoops I kind of did this
#Aiden Krahn
import random
#list
onenames = ['James', 'Robert', 'Julia', 'Ashton', 'Evan', 'Joey', 'Kingsley', 'Peter', 'Jake', 'Eva', 'Nchuleft', 'Shawn', 'Sean']
twonames = ['Mohammed', 'Bruce', 'Lee', 'Branden', 'Dougald', 'The']
threenames = ['Cornwallis', 'Whyte', 'Friesen', 'Wiebe', 'Hitler', 'Plum', 'Bateman', 'Wayne', 'Joestar']

first = onenames[random.randint(0, len(onenames)-1)] + ' '
middle = twonames[random.randint(0, len(twonames)-1)] + ' '
last = threenames[random.randint(0, len(threenames)-1)]

newfile = open('coolcoolcool.txt', 'w')

newfile.write(first)
newfile.write(middle)
newfile.write(last)

newfile.close()

newerfile = open('coolcoolcool.txt', 'r')
print('Your new name is...')
print(newerfile.read())
newerfile.close()