# Write your code here
class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, till):
        self.buy_ = 0
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.till = till
        self.state = 'main'
        self.fill_state = None

    def menu_(self, selection):
        if self.state == 'main':
            if selection == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, or type "back":')
                self.state = 'buy'
            elif selection == 'fill':
                print('Write how many ml of water do you want to add:')
                self.state = 'fill'
                self.fill_state = 'water'
            elif selection == 'take':
                cm1.take()
            elif selection == 'remaining':
                cm1.machine_status()
            elif selection == 'exit':
                self.state = 'exit'
            else:
                print('Invalid input')
        elif self.state == 'buy':
            self.buy(selection)
        elif self.state == 'fill':
            self.fill(selection)

    def machine_status(self):
        """Returns current inventory and till levels, no input"""
        print('''The coffee machine has:
{0} of water
{1} of milk
{2} of coffee beans
{3} of disposable cups
${4} of money'''.format(self.water, self.milk, self.beans, self.cups, self.till))

    def check_lvl(self, water, milk, beans, cups, till):
        """This function checks inventory levels against the passed in values, then adjust levels"""
        if self.water >= water:
            pass
        else:
            return 'Sorry, not enough water!'
        if self.milk >= milk:
            pass
        else:
            return 'Sorry, not enough milk!'
        if self.beans >= beans:
            pass
        else:
            return 'Sorry, not enough coffee beans!'
        if self.cups >= cups:
            pass
        else:
            return 'Sorry, not enough cups!'
        # modify the inventory quantities if there are sufficient quantities to make the coffee
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.till += till
        self.state = 'main'
        return 'I have enough resources, making you a coffee!'

    def buy(self, selection):
        """takes user input for coffee type selection, calls check level to adjust inventory if sufficient quantities"""
        result_ = ''
        self.buy_ = selection
        if self.buy_ == "1":  # espresso
            result_ = self.check_lvl(250, 0, 16, 1, 4)
        elif self.buy_ == "2":  # latte
            result_ = self.check_lvl(350, 75, 20, 1, 7)
        elif self.buy_ == "3":  # cappuccino
            result_ = self.check_lvl(200, 100, 12, 1, 6)
        elif self.buy == "back":
            self.state = 'main'
        else:
            print("This is not a valid option")
        print(result_)
        self.state = 'main'


    def fill(self, selection):
        """Add quantities to inventories with user inputs"""
        if self.fill_state == 'water':
            self.water += int(selection)
            self.fill_state = 'milk'
        elif self.fill_state == 'milk':
            self.milk += int(selection)
            self.fill_state = 'beans'
        elif self.fill_state == 'beans':
            self.beans += int(selection)
            self.fill_state = 'cups'
        elif self.fill_state == 'cups':
            self.cups += int(selection)
            self.fill_state = None
            self.state = 'main'

    def take(self):
        """Prints till amount an then reduces till to zero"""
        print('I gave you ${0}'.format(self.till))
        self.till = 0


# start of the program
# cm1 = CoffeeMachine(1200,540,120,9,550)
cm1 = CoffeeMachine(400, 540, 120, 9, 550)
while cm1.state != 'exit':
    cm1.menu_(input())

