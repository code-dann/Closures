def decorator(function):
    def nestedfunction():
        
        print('This is a new instruction')
        function()
        
    return nestedfunction

@decorator
def greetings():
    print('Hello!')


greetings()


