def decorator(function):
    def nestedfunction():
        
        print('This is a new instruction')
        function()
        
    return nestedfunction


def greetings():
    print('Hello!')


greetings()

sayHi= decorator(greetings)
sayHi()