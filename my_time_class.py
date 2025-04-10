from typing import Optional

IS_DEBUG = False

HOURS_THRESHOLD = 12
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
WEEK_DAYS =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]

def debug_print(*args,**kvargs):
  if IS_DEBUG:
    print(*args,**kvargs)



def from_day_to_index(day_name:str|None):
  #for calulate the index of the day in the week
  if(day_name is None):
    return None
  try:
    index_number= WEEK_DAYS.index(day_name.lower().strip())
    debug_print("[Function: from day to index]:",  index_number)
    return index_number
  except ValueError:
    
    raise Exception("Invalid day name")
pass

def result_day_name(input_day_index:int|None, residual_days):
  if input_day_index is None:
    raise Exception("[Function: result_day_name] Invalid day index")
  
  residual_days = int(residual_days)

  output_index=(input_day_index+residual_days)% len(WEEK_DAYS)
  debug_print("[Function: result_day_name]:",  output_index)
  day_name_result=WEEK_DAYS[output_index]  
  debug_print("[Function: result_day_name]:",  day_name_result)
  return day_name_result

pass




class MyTime:
  def __init__(self, hour, minute, period,duration_hours,duration_minutes,day: Optional[str]=None):
    debug_print(
        f"\n\thour={hour}, \n\tminute={minute}, \n\tperiod={period},"
        f"\n\tduration_hours={duration_hours}, \n\tduration_minutes={duration_minutes}, \n\tday={day}"
    )
    #------------------------  valori iniziali ------------------------------
    self.hour = int(hour)
    self.minute = int(minute)
    self.period = str(period)  # AM or PM
    if day is not None:
      self.day = str(day).strip().lower()
    else:
      self.day = None  
    self.duration_hours = int(duration_hours)
    self.duration_minutes = int(duration_minutes)
    #------------------------  valori temporanei ------------------------------
    self.residual_hours = 0
    self.residual_number_of_peroids=0
    self.resisual_days = 0
    self.input_day_index:Optional[int|None]=from_day_to_index(self.day)
    self.output_day_index:Optional[int|None]=None
    #--------------------  valori con la soluzione ------------------------------
    self.result_hour = None
    self.result_period = None
    self.result_minute:Optional[str|int] = 0
    self.result_day_name = None 
    self.result_days_later = None
    self.outputstring = None
    #----------------------------------------------------------------------------
    self.compute_time()

  
  def compute_time(self):
    self.compute_residual()
    self.make_output()

  

  def compute_residual(self):
    #calcolo dei minuti Totali 
    total_minutes= (self.minute+self.duration_minutes) 
    self.result_minute = total_minutes % MINUTES_IN_HOUR
    debug_print("minutes",self.result_minute)

    #calcolo delle ore Residue
    partial_residual_hours = int(total_minutes / MINUTES_IN_HOUR)
    self.residual_hours = partial_residual_hours + self.duration_hours + self.hour
    self.result_hour = (int(self.residual_hours)% HOURS_THRESHOLD)
    if self.result_hour == 0:
      self.result_hour = HOURS_THRESHOLD
    debug_print("hours",self.result_hour)
    debug_print("residual hours",self.residual_hours)
    

    #calcolo dei giorni residui
    self.resisual_days = int(self.residual_hours / HOURS_IN_DAY)
    debug_print("residual days",self.resisual_days)
    
    self.residual_number_of_peroids = int(self.residual_hours/HOURS_THRESHOLD)+2*self.resisual_days
    debug_print("residual number of peroids",self.residual_number_of_peroids)
    if self.residual_number_of_peroids % 2 == 0:
      self.result_period = self.period
    else:
      if self.period == "AM":
        self.result_period = "PM"
      else:
        self.result_period = "AM"

    debug_print("result period",  self.result_period)

      
  def make_output(self):
    # print(self)
    #------------------------------------------  properly format Minutes
    if int(self.result_minute) < 10:
      self.result_minute = f"0{self.result_minute}"
    self.my_out_string = f"{self.result_hour}:{self.result_minute} {self.result_period}"


    #------------------------------------------  discriminate and format days
    if self.day is None: 
      #NO day name, only passed
      if self.resisual_days == 1:
        self.my_out_string = self.my_out_string + " (next day)"
      else:
        if self.resisual_days > 1:
          self.my_out_string = self.my_out_string + f" ({self.resisual_days} days later)"
      pass
    else:
      # With day name
      self.result_day_name=result_day_name(self.input_day_index,self.resisual_days)
      self.my_out_string = self.my_out_string + f", {self.result_day_name}"+ f" ({self.resisual_days} days later)"
    
    
    debug_print("result String",self.my_out_string)
    
    
  
  
  
  def get_output(self):
    #print(self.my_out_string)
    return self.my_out_string
  

  def __str__(self):
    attributi = [f"-> {chiave}=f{valore!r}" for chiave, valore in self.__dict__.items()]