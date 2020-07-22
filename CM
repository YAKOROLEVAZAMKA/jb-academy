class Coffee_Machine:
    
    def __init__(self, bucks, water, milk, beans, cups):
        self.bucks = bucks
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        
        self.ans = None
        self.a = None
        self.action()
        
        #self.state = 'action'
        
    
    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.bucks} of money')
        
        self.action()
        
    
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        
        self.action()
        
    def take(self):
        print(f'I gave you ${self.bucks}')
        self.bucks = 0
        
        self.action()
        
        
    def check(self, wa, mi, be, bu, cu):
        if self.water - wa >= 0 and self.beans - be >= 0 and self.cups - cu >= 0 and self.milk - mi >=0:
            print('I have enough resources, making you a coffee!')
            self.water -= wa
            self.milk -= mi
            self.beans -= be
            self.bucks += bu
            self.cups -= cu

        else:
            if self.water - wa < 0:
                self.ans = 'water'
            elif self.beans - be < 0:
                self.ans = 'beans'
            elif self.milk - mi < 0:
                self.ans = 'milk'
            else:
                self.ans = 'cups'
            print(f'Sorry, not enough {self.ans}!')
        self.action()
        
    
    def buy(self):
        self.a = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

        if self.a == '1':
            self.check(250, 0, 16, 4, 1)

        elif self.a == '2':
            self.check(350, 75, 20, 7, 1)

        elif self.a == '3':
            self.check(200, 100, 12, 6, 1)

        else:
            
            self.action()
            #self.state = 'action'

    
    def action(self):
        self.a = input('Write action (buy, fill, take, remaining, exit):')
    
        if self.a == 'buy':
            self.buy()
        elif self.a == 'fill':
            self.fill()
        elif self.a == 'take':
            self.take()
        elif self.a == 'remaining':
            self.remaining()
        elif self.a == 'exit':
            pass
            
c = Coffee_Machine(550, 400, 540, 120, 9)            
