#As a developer, I want to use Python’s proper snake_case for variable names.
#As a developer, I want to create a selfClock class.
#As a developer, I want the selfClock class to have class instance variables to keep track of the selfClock’s current time, whether the self is on or off, and the time the self is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).
#As a developer, I want the selfClock class to have a method to set (or change) the current time and print to the console the current time.
#As a developer, I want the selfClock class to have a method to toggle the self on or off.
#As a developer, I want the selfClock class to have a method to set the current self time and print to the console the current self time.
#As a developer, I want to import the selfClock class into main.py so I can instantiate it as a new selfClock object and call methods on it.

from main1 import self


class self:
    def __init__(self):
        self.name = 'Scheduled self'
        self.enter_time = ''
        self.alarm_set = ''
        self.go_off = ''
    
    def set_time(self):
        set_time = self.enter_time
        self.enter_time = input(f'Please enter time (0001 - 2359).    ')
        print(f'The time is {self.enter_time}.')

    def set_up_self(self):
        self.go_off  = input(f"Please, set the time you want {self.name} to go off. (0001 - 2359) ")
        print(f'{self.name} is set for {self.go_off}.')

    def set_alarm (self):
        self.alarm_set = input(f'Is {self.alarm_set}? Y or N')

    if self.alarm_set == 'Y':
            print(f'{self} is on, and set to wake you up at {self.go_off}.')
    else:
            self.alarm_set == False
            print(f'{self.name} is not turned on!')
