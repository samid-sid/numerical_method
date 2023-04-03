import math as m


def func(x):
    return x*m.sin(x)


def simpson_three_eight(ll, ul, n):
    h = (ul-ll)/n
    ans = func(ll) + func(ul)

    for i in range(1, n):
        xi = ll + i * h
        tmp = func(xi)
        if i % 3 != 0:
            ans += tmp * 3
        else:
            ans += tmp * 2

        # ans *= h/3
    new_ans = (3*h/8) * ans
    return new_ans


if __name__ == '__main__':

    ll = float(input("Enter Lower limit : "))
    ul = float(input("Enter upper limit : "))
    n = int(input("Enter interval : "))

    ans = simpson_three_eight(ll,ul,n)

    print(ans)
