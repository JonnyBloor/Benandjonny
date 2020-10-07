#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


secret = 'swordfish'
pw = ' '

auth = False
count = 0
max_attempt = 7

while pw != secret:
    count += 1
    if count > max_attempt:
        print("X Incorrect answer, you lose, try playing again later when you have some better ideas")
        break

    elif count > 1:
        print( "X Incorrect answer, plese try again")

    pw = input(f"{count}: What's the secret word? ")

if pw == secret:
    print ("O Congratulations, you guessed the right answer")    


 
