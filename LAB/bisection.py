def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Function values at 'a' and 'b' should have opposite signs.")
        return None
    
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    
    return (a + b) / 2

# Get user input for the function as a string
func_str = input("Enter the function in terms of 'x': ")

# Create a function object from the user-provided function string
def user_function(x):
    return eval(func_str)

# Get user input for the interval [a, b]
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

root = bisection_method(user_function, a, b)

if root is not None:
    print(f"Root found at x = {root:.6f}")
else:
    print("Bisection method did not converge within the specified tolerance or maximum iterations.")
