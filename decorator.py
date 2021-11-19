def decorator(function):
    def nestedfunction():
        
        print('This is a new instruction')
        function()
        
    return nestedfunction

@decorator
def greetings():
    print('Hello!')


greetings()


def Uppercase(function):
    def nested(text):
       return function(text).upper()
    return nested

@Uppercase
def message(name):
    return f'{name}, you have a message'

print(message('Daniel'))
