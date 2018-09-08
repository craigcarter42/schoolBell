import os,time,datetime,pygame
globalcurrentTime = 0
currentDate = ""

def chime():
    pygame.mixer.init()
    pygame.mixer.music.load("tone.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def dateCheck():
    bellDate = True
    while bellDate == True:
        datetime.datetime.today()
        currentDate = datetime.datetime.today().weekday()
        currentTime = int(time.strftime("%H%M"))
        time.sleep(5)
        #(0)Monday (1)Tuesday (2)Wednesday (3)Thursday (4)Friday (5)Saturday (6)Sunday
        if currentDate == 0 or currentDate == 1 or currentDate == 2:
            print(">",currentDate, "is a school day") #: go from 0 - 6.
            if currentTime == 1630:
                print("> Bell chime!")
                chime()
                logger(1)
                time.sleep(60)
            if currentTime == 1840:
                print("> Bell chime!")
                chime()
                logger(1)
                time.sleep(60)
            if currentTime == 2005:
                print("> Bell chime!")
                chime()
                logger(1)
                time.sleep(60)
            if currentTime == 2025:
                print("> Bell chime!")
                chime()
                logger(1)
                time.sleep(60)
            if currentTime == 2200:
                print("> Bell chime!")
                chime()
                logger(1)
                time.sleep(60)
        else:
            print(">",currentDate, "not a school day.")

def logger(message):
    datetime.datetime.today()
    currentDate = datetime.datetime.today().weekday()
    currentTime = int(time.strftime("%H%M"))
    if message == 0:
        output = "echo :: school bell started date:" + str(currentDate) + " time:" + str(currentTime) + " >> bell_log.txt"
        os.system(output)
    elif message == 1:
        output = "echo :: school bell chimed date:" + str(currentDate) + " time:" + str(currentTime) + " >> bell_log.txt"
        os.system(output)

print(":: start")
logger(0)
dateCheck()
