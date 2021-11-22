###########################################################################################################################3
## James Burns
## CS101 Lab 
## Assignment 11
##
## PROBLEM: create a clock class that can keeptrack of hours, minutes and seconds. Contains attributes for hours, minutes, seconds, and clocktype.  Formats time as a string using either 24-hour clock or 12-hour clock. Program takes input for hour, minute, second and outputs time of day, incrementing time at each second and printing current time continuously.
##
## Algorithm:
##  1. Create Clock class, initiating "__init__()" method containing parameters hours, minutes, seconds, and clocktype(default 0)
##  2. Create clock method __str__() to print formatted time. 
##  3. Create clock method "tick()" to increment seconds by 1. If seconds is 60, changes seconds to 0, increments minutes by 1. If minutes = 60, changes minutes to 0, increments hours by 1/
## In Main:
##  4. import time module
##  5. Obtain input for hours, minutes, seconds. Set to respective variables.
##  6. create an instance of Clock called time_of_day with arguments hour, minute, second
##  7. Initiate while loop to print time_of_day then sleep one second 
##
###############################################################################################################################################

class Clock:
    def __init__(self, hours, minutes, seconds, clock_type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type

    def __str__(self):
        if self.clock_type == 0:
            return "{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds)
        elif self.clock_type == 1:
            if self.hours > 12:
                return "{:02}:{:02}:{:02} pm".format((self.hours - 12), self.minutes, self.seconds)
            elif self.hours == 0:
                return "{:02}:{:02}:{:02} am".format(12, self.minutes, self.seconds)
            else:
                if self.hours == 12:
                    return "{:02}:{:02}:{:02} pm".format(self.hours, self.minutes, self.seconds)
                else:
                    return "{:02}:{:02}:{:02} am".format(self.hours, self.minutes, self.seconds)
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0


if __name__ == "__main__":

    import time
    
    hour = int(input("What is the current hour? ==> "))
    minute = int(input("What is the current minute? ==> "))
    second = int(input("What is the current second? ==> "))

    time_of_day = Clock(hour, minute, second,1)

    while True:
        print(time_of_day)
        time_of_day.tick()
        time.sleep(1)

