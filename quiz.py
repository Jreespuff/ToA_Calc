score = 0

print('Welcome to my Book of Mormon Quiz!')
username = input('What is your name? ')
print("Welcome " + username + '!')

answer = input('Who translated the Book of Mormon?').lower()
if answer == 'joseph smith':
    print('Correct!')
    score +=1
    print('You have ' + str(score) + ' points')