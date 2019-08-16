#Write a Python program to detect the number of local variables declared in a function
def check():
    x = 1
    y = 2
    st= "Krunal"
    print("Python Exercises")
print(check.__code__.co_nlocals)