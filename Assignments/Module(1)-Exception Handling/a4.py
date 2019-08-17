#Write program that except Clause with No Exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# user guesses a number until he/she gets it right
number = 10

while True:
   try:
       inum = int(input("Enter a number: "))
       if inum < number:
           raise ValueTooSmallError
       elif inum > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
   except ValueTooLargeError:
       print("This value is too large, try again!")
 
print("Congratulations! You guessed it correctly.")