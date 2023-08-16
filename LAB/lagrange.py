#Lagrange
def lagrange_interpolation(X,Y,k):
    x_k = 0
    for i in range(len(X)):
        T_i = Y[i]
        for j in range(len(X)):
            if i != j:
                # numerator term
                T_i *= (k - X[j])
                # denominator term
                T_i *= (1/(X[i] - X[j]))
        x_k+=T_i
    return x_k



def main():
    x = [45, 50, 55, 60, 65]
    f_x = [114.84, 96.16, 83.22, 74.48, 68.48]
    for k in range(46,64):
        f_k = lagrange_interpolation(x,f_x,k)
        print("f({0}) = {1}".format(k,f_k))


main()
