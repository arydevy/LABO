

import random,datetime
from adons import *
from stats import *
from sys import exit



input_output = {"hi": greeting,
                'hello': greeting,
                "what is your name": myname,
                "my name": user,
                "about": about,
                "where are you from": home,
                "how old are you":brithCalc(day,mon),
                "what is the date": today,
                "what is the time": timeNow,
                "bye" : exit()
                }

