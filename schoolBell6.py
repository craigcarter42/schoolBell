import time, datetime

##### Uncomment code below before running on Raspberry Pi
#import pygame

def chime():
##### Uncomment code below before running on Raspberry Pi
    # pygame.mixer.init()
    # pygame.mixer.music.load("tone.mp3")
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy() == True:
    #     continue

    print(" schoolBell -- chime")
    logger(2)
    time.sleep(60)
# chime: END

def date_time():
    global now, currentDate, currentTime, currentDay
    currentDate = datetime.datetime.today().weekday()
    currentTime = int(time.strftime("%H%M"))
    now = datetime.datetime.now()
    now.strftime("%Y-%m-%d %H:%M")
    currentDay = day_check(currentDate)
    print(" schoolBell -- Date / Time Check: " + str(now))
# date_time: END

def day_check(daynum):
    if   daynum == 0: return "Monday"
    elif daynum == 1: return "Tuesday"
    elif daynum == 2: return "Wednesday"
    elif daynum == 3: return "Thursday"
    elif daynum == 4: return "Friday"
    elif daynum == 5: return "Saturday"
    elif daynum == 6: return "Sunday"
    else:
        print(" schoolBell -- day_check: ERROR")
# day_check: END
def dateCheck():
    bellDate = True
    logger(1)
    while bellDate == True:
        date_time()
        time.sleep(5)
        #(0)Monday (1)Tuesday (2)Wednesday (3)Thursday (4)Friday (5)Saturday (6)Sunday
        if currentDate == 0 or currentDate == 1 or currentDate == 5:
            print(" schoolBell -- {0} is a school day").format(currentDay) #: go from 0 - 6.
            if currentTime == 558 or currentTime == 602 or currentTime == 604 or currentTime == 606 or currentTime == 608: chime()
        else:
            print(" schoolBell -- {0} not a school day.").format(currentDay)
# dateCheck: END
def logger(message):
# Open / Create Log File
    log_file = open(" schoolBell.log", "a")
#Program has started:
    if message == 0:
        log_file.write("schoolBell -- START\n")
        log_file.write(" ---- date: " + str(now) + "\n")
        log_file.close
# Current Day
    elif message == 1:
        log_file.write(" schoolBell -- Current Day: " + currentDay + "\n")
        log_file.close
# Bell has Chimed:
    elif message == 2:
        log_file.write(" schoolBell -- BELL CHIME\n")
        log_file.write(" ---- date: " + str(now) + "\n")
        log_file.close
# Error
    elif message == 3:
        log_file.write(" schoolBell -- ERROR\n")
        log_file.write(" ---- date: " + str(now) + "\n")
        log_file.close
    else:
        print(" help")
# logger: END
def main():
    print(":: schoolBell -- START")
    date_time()
    logger(0)
    dateCheck()
# main: END

if __name__ == "__main__":
    main()




