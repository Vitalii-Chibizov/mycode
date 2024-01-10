#!/usr/bin/env python3

#create vars
name = input("What is your name?\n")
age = input("What is your age?\n")
favourite_movie = input("What is your favourite movie?\n")
my_list = [name, age, favourite_movie]
print("Hello, " + my_list[0][0].upper + my_list[0][1:].lower + ", you are " + my_list[1] + " years old and your favourite movie is " + my_list[2][0].upper + my_list[2][1:].lower + ".")
