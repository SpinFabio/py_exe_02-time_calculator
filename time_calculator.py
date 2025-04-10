from my_time_class import MyTime
from typing import Optional
import re

MY_PATTERN_START = r"(\d+):(\d+) (AM|PM)"
MY_PATTERN_DURATION = r"(\d+):(\d+)"
HOURS_THRESHOLD = 12
MINUTES_THRESHOLD = 59


def add_time(start, duration, day:Optional[str]=None):
    #print(f"INPUT: {start} {duration} {day}")
    #----------------------------------------------------------------
    matches : re.Match[str]|None = re.search(MY_PATTERN_START,start)   
    if matches is None:
        raise Exception("Invalid start time format")

    start_hour = int(matches.group(1))
    if start_hour > HOURS_THRESHOLD | start_hour <=0:
        raise Exception("Invalid start hour")
    start_minute = int(matches.group(2))
    if start_minute > MINUTES_THRESHOLD| start_minute <0:
        raise Exception("Invalid start minute")        
    start_period = matches.group(3)    

    #----------------------------------------------------------------
    
    matches : re.Match[str]|None = re.search(MY_PATTERN_DURATION,duration)
    if matches is None:
        raise Exception("Invalid duration fromat")    
    #qui ci possono stare un umero arbitrario di ore 
    #ma i minuti sempre meno di 59 devono essere
    duration_hour = int(matches.group(1))
    duration_minute = int(matches.group(2))
    if duration_minute > MINUTES_THRESHOLD| duration_minute <0:
        raise Exception("Invalid duration minute")
        
    #----------------------------------------------------------------
    
    
    my_time = MyTime(start_hour,start_minute,start_period,duration_hour,duration_minute,day)
    #print(my_time)
    
    
    


    return my_time.get_output()