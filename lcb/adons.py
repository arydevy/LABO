from stats import *

def brithCalc(day,mon):
    days= day-int(theBrith_List[0])
    months = mon-int(theBrith_List[1])
    return f"i have {days} days and {months} months now "

def speach(input, output):
    if input == inputFromUser:
        print(output)
    else:
        print("i don't have this implemented if you want to help go to my github repository")
        
