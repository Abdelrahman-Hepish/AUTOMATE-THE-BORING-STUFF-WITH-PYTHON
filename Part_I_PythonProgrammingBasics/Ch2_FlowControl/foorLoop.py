# import random , sys 
# 
# while True : 
#     i = random.randint(0 , 10 ) 
#     print(i) 
#     if i == 5 : 
#         sys.exit()
############################################
#def spam():
#    global var
#    var = "l" 
#    print("Spam : ",var) 
#
#var = "g"
#spam() 
#print("global ",var)

# def div(divi):
#     try :
#         return 42/ divi 
#     except ZeroDivisionError : 
#         print("Zero Division ")
# 
# print(div(7))
# print(div(42))
# print(div(0))

import random 

target = random.randint(1,20) 
print("I am thinking in a number between 1 and 20 ") 

# Ask the player to guess 6 times 
for try_ in range(1 , 7 ) : 
    print("Guess the number ") 
    guess = int(input()) 
    if guess < target : 
        print('Your guess is too low.')
    elif guess > target : 
        print('Your guess is too high.')
    else : 
        break 
if guess == target : 
    print('Good job! You guessed my number in ' + str(try_) + ' guesses!')
else : 
    print('Nope. The number I was thinking of was ' + str(target))