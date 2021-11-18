
def make_divisor_by(n):

    def divisor(x):
        assert type(x) == int and x >0,  'please enter a valid value'
        return x/n

    return divisor

def run():
    test=make_divisor_by(3)
    print(test(18))

    test_by_5=make_divisor_by(5)
    print(test_by_5(100))

    test_by_18=make_divisor_by(18)
    print(test_by_18(54))

if __name__ == '__main__':
    run()