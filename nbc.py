import os
import time
from selenium import webdriver
from selenium .webdriver.common.by import By
from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path


cal = Calendar()

#url
nbc_url = "https://simbasc.co.tz/team/fixtures/"


#opening browser
driver = webdriver.Firefox(executable_path=r"C:/seleniumDriver/geckodriver.exe")


driver.get(nbc_url)


timedate = driver.find_elements(By.TAG_NAME,"time")
match_time = driver.find_elements(By.CSS_SELECTOR,".sp-result.ok")
links = driver.find_elements(By.CSS_SELECTOR,".sp-events-results")

a = 0
b = 0
tarehe = []
muda = []


for x in timedate:

    present = x.text.find("October ") 
    
    if present >= 0:
        
      print(x.text)
      tarehe.append(x.text)

        
        
for value in match_time:

    present2 = value.text.find("pm") 
    
    if present2 >= 0:
        
      print(value.text)
      muda.append(value.text)

    
    #print(x.text)
event = Event()
n = 0
while (n <= 4 ):
    siku = tarehe[n][tarehe[n].find(" "): tarehe[n].find(",")]
    print(siku)
    

    saa = muda[n][0:1]
    print(saa)

    saa = int(saa) + 12

    siku = int(siku)


    event.add('summary', 'Simba - MatchDay')
    event.add('dtstart', datetime(2022, 10, siku, saa, 0, 0, tzinfo=pytz.utc))
    event.add('dtend', datetime(2022, 10, 24, siku, saa+2, 0, tzinfo=pytz.utc))
    event.add('dtstamp', datetime(2022, 10, siku, saa, 10, 0, tzinfo=pytz.utc))


    # Adding events to calendar
    cal.add_component(event)

    directory = str(Path(__file__).parent.parent) + "/"
    simba_match_day = "october_"+ str(siku) + ".ics"
    print("ics file will be generated at ", directory)
    f = open(os.path.join(directory, simba_match_day), 'wb')
    f.write(cal.to_ical())
    f.close()


    n = n + 1

