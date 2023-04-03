import math as m


def func(x):
    return x*m.sin(x)



def simpson_one_third(ll, up, n):
    h = (ul-ll)/n
    ans = func(ll) + func(ul)

    for i in range(1, n):
        xi = ll + i * h
        tmp = func(xi)
        if i % 2 != 0:
            ans += tmp * 4
        else:
            ans += tmp * 2

    new_ans = (h/3) * ans
    return new_ans


if __name__ == '__main__':

    ll = float(input("Enter Lower limit : "))
    ul = float(input("Enter upper limit : "))
    n = int(input("Enter interval : "))

    ans = simpson_one_third(ll, ul, n)

    print(ans)
