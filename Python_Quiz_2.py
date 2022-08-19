'''Complete the Script by filling in the missing parts. the function receives a name, then returns a greeting
based on whether or not that name is "Taylor". '''

def greeting(name):
    if name == "Taylor":
        return "Welcome Back Taylor!"
    else:
        return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("Sagar"))
