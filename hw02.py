# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
        
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    return x,y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(x,y):
     
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    numerator = (x*y)
    print(f"mult result: {numerator}")
    denominator = (x+y)
    print(f"add result: {denominator}")
    return numerator/denominator
    
# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(x, y, xy_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("*"*16)
    print("RESULTS:")
    print(f"first number: {x}")
    print(f"second number: {y} ")
    print(f"multadd result: {xy_multadd}")
    print("="*16)
def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x, y = read_two_ints()
             
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
        #compute_multadd(x,y):
    xy_multadd=compute_multadd(x,y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    #def print_fancy(a, b, ab_multadd):
       # result = print_fancy(a,b,ab_multadd)
    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
