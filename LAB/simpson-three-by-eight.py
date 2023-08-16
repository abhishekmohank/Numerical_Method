#Simpson
def simpson_3_by_8(f,a,b,step):
    h = (b - a) / step
    # Array to store x_i and y_i values
    x = [i*h + a for i in range(0,step)]
    y = [f(j) for j in x]

    #print(x)
    #print(y)
    # Applying simpsons formuls
    I = y[0] + y[-1]

    # iterating through 1 to n-1
    for i,f_i in enumerate(y[1:-1]):
        if i%3 == 0:
            I += f_i * 2
        else:
            I += f_i * 3

    I = I*((3/8)*h)

    return I

def main():
    f = lambda x: 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)

    #f = lambda x: 2 / (1 + x**3)
    a = 0
    b = 1

    step = 2

    for step in range(100,102):

        print("Step size", step)
        I1 = simpson_3_by_8(f,a,b,step)
        print("Simpson 3/8", I1)

if __name__ == "__main__":
    main()
