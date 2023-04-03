import math as m


def func(x):
    return x*m.sin(x)


def trapezoidal(ll, ul, n):

    h = (ul-ll)/n
    ans = func(ll) + func(ul)/2

    for i in range(1, n):
        xi = ll + i*h
        ans += func(xi)

    ans *= h
    return ans


if __name__ == '__main__':

    ll = float(input("Enter Lower limit : "))
    ul = float(input("Enter upper limit : "))
    n = int(input("Enter interval : "))

    ans = trapezoidal(ll,ul, n)

    print(ans)
