def make_multiplier(number):
    def multiplier(n):
        return number*n

    return multiplier

times10 = make_multiplier(10)
times5= make_multiplier(5)



print(times10(3))
print(times5(4))