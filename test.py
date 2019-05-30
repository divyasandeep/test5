# WHILe LOOP


guess_count =1
while guess_count <=5:
    print(guess_count)
    guess_count = guess_count + 1
print("done")


#Guess Game

secreat_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int (input('guess: '))
    guess_count += 1
    if guess == secreat_number:
        print('you won! ')
        break
else:
    print('sorry,you failed')