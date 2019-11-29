def formalGreeting():
    print("How are you?")

def casualGreeting():
    print("What's up?")

def greet(self, type, greetFormal, greetCasual):
    if type == 'formal':
        self.greetFormal()
    elif type == 'casual':
        self.greetCasual

print("Formal greeting is ", formalGreeting())
print("Casual greeting is ", casualGreeting())