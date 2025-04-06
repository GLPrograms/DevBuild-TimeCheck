import datetime
import requests
import os
import time
import json
                    
if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')

terminal_size = os.get_terminal_size()
text_width = terminal_size.columns

asciiIntro = """________              __________      .__.__       .___        
\\______ \\   _______  _\\______   \\__ __|__|  |    __| _/        
 |    |  \\_/ __ \\  \\/ /|    |  _/  |  \\  |  |   / __ |         
 |    `   \\  ___/\\   / |    |   \  |  /  |  |__/ /_/ |         
/_______  /\\___  >\\_/  |______  /____/|__|____/\\____ |         
        \\/     \\/             \\/                    \\/         
            __________       .__                               
            \______   \\ ____ |  |   ____ _____    ______ ____  
             |       _// __ \|  | _/ __ \\__  \  /  ___// __ \\ 
             |    |   \\  ___/|  |_\\  ___/ / __ \\_\\___ \\\\  ___/ 
             |____|_  /\___  >____/\___  >____  /____  >\\___  >
                    \\/     \\/          \\/     \\/     \\/     \\/ """

textIntro = "="*text_width
textIntro += "\nTumblrScript"
textIntro += "\n- Created by Kauntar\n"
textIntro += "="*text_width

if(text_width >= 63):
    print(asciiIntro+"\n\n")
else:
    print(textIntro+"\n\n")

while True:
    url = "https://uploadfiles.cc/get_progress.php"
    
    r = requests.get(url)
    data = r.json()
    
    progress = data['progress']
    timeRemaining = data['timeRemaining']
    
    os.system("cls")
    
    timeNow = int(time.time())
    timeSplit = timeRemaining.split(":")
    timeHr = int(timeSplit[0]) * 60 * 60
    timeMin = int(timeSplit[1]) * 60
    timeSec = int(timeSplit[2])
    timeNDate = datetime.datetime.fromtimestamp(timeNow)
    timeCS = timeNDate.strftime("%Y-%m-%d %H:%M:%S UTC")
    timeFull = timeHr + timeMin + timeSec
    timeFuture = timeNow + timeFull
    timeFDate = datetime.datetime.fromtimestamp(timeFuture)
    timeFS = timeFDate.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    if(text_width >= 63):
        print(asciiIntro+"\n\n")
    else:
        print(textIntro+"\n\n")
        
    print(f"URL: {url}")
    print(f"Progress: {progress}%")
    print(f"Time Remaining: {timeRemaining}")
    print(f"Current UTC: [{timeNow}] {timeCS}")
    print(f"Time Difference: {timeFull}")
    print(f"Expected UTC: [{timeFuture}] {timeFS}")
    time.sleep(0.5)
    