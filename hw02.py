"""
Ruby Tricca

"""

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
        
    #asks users to input values for variables x and y and returns the values
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    return x,y

# Task 2.1:
"""
        The function below uses the multiplication and addition
        operators to compute the numerator and denominator of the fraction.
        It takes in the values of x and y defined by the user input in the
        previous function.
        
"""
  
def compute_multadd(x,y):
     
    # calculates the numerator and denominator of a fraction, and returns the quotient
    numerator = (x*y)
    print(f"mult result: {numerator}")
    denominator = (x+y)
    print(f"add result: {denominator}")
    return numerator/denominator
    
# Task 3.1:

"""
        The function below prints the variable and return values from the functions
        above. It then uses the multiplication operator to create a line of * above and
        a line of = below the printed statements. 
"""
    
def print_fancy(x, y, xy_multadd):
    
    # prints the variables x and y and the  results of the operations above
    print("*"*16)
    print("RESULTS:")
    print(f"first number: {x}")
    print(f"second number: {y} ")
    print(f"multadd result: {xy_multadd}")
    print("="*16)
    
"""
        The main function below calls each of the functions
        defined above, including arguments where applicable.
        
"""
def main ():
    # calls the functions defined above 
    # Task 1.2:
    x, y = read_two_ints()
             
    # Task 2.2:
    xy_multadd=compute_multadd(x,y)

    # Task 3.2:
    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
