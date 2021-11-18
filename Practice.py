def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, 'Please enter a text'
        return string *n
    
    return repeater



def run():
    test= make_repeater_of(3)
    print(test('hello'))



if __name__ == '__main__':
    run()