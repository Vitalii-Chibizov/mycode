#!/usr/bin/env python3

def main():

    #first number would be 0 and second 1 (as it should be)
    a = int(0)
    b = int(1)

    print(a)
    fibonacci(a,b)

def fibonacci(a,b):
       
   old_a = int(a)
   a = b
   b = old_a + a
       
   print(b)
   return fibonacci(a,b)
    
main()
    #fibonacci()
