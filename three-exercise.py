from datetime import datetime,timedelta
from time import strftime

now= datetime.now()
now_less_5hours=now - timedelta(hours = 5)

current_time= now_less_5hours.strftime("%H,%M,%S")
("Current Time =",current_time)
(now_less_5hours.isoweekday())

day = now_less_5hours.isoweekday()
if(day == 2 or 4):
  print("Hay clase")

else:
   print("No hay clase")