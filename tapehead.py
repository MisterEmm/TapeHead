import gspread # For accessing Google Sheets via Python
import pygame # Needed for breathing & laser sound, and Polly speech
import RPi.GPIO as GPIO
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials # Needed for Google Sheets access
from Polly import Polly # Save the Polly.py script into the same folder as the main script
from gpiozero import Servo # Control the moving eyes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setup(14, GPIO.OUT) #relay for laser & pump
GPIO.output(14,False)

myGPIO=15 #Servo Control Pin

# Servo specific settings, adjust if you need more range of movement

myCorrection=0.45 
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

# Sound settings

pygame.init()
ding = pygame.mixer.Sound("/home/pi/Music/laser.wav") # Laser sound
breath = pygame.mixer.Sound("/home/pi/Music/slowbreathing.wav") # Breathing sound

# Tell the Polly service which voice to use

tts = Polly('Brian')
tts.say('Destroy All Humans')

# Google Sheets access - as part of the setup export your credentials to json and save to path below

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/SpeakingSpreadsheet.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Pi').sheet1 # Name of the spreadsheet you're accessing

def last_row(sheet, cols_to_sample=2):
  # looks for empty row based on values appearing in 1st N columns
  cols = sheet.range(1, 1, sheet.row_count, cols_to_sample)
  return max([cell.row for cell in cols if cell.value]) #+ 1

prevID=0

while True: 
    ID = last_row(sheet)
    if ID != prevID: # Only read out the cell value if it hasn't been read out already
        print("Different")
        print(ID)
        cell = sheet.cell(ID, 3).value # Which cell to read out, 3 is column C
        print(cell)
        myServo.value= 0
        GPIO.output(14,True) # Lasers & Pump ON
        ding.play() # Laser sound
        sleep(1.2)
        myServo.value= -0.2 # Move eyes
        ding.play()
        sleep(1.2)
        myServo.value= 0.2
        ding.play()
        sleep(1.2)
        myServo.value= -0.3
        ding.play()
        sleep(1.2)
        myServo.value= 0.3
        ding.play()
        sleep(1.2)
        myServo.value= 0
        GPIO.output(14,False) #Lasers & Pump OFF
        sleep(1)
        tts.say(cell) # Read out the text contents of the spreadsheet cell
        sleep(1)
        GPIO.output(14,True)
        ding.play()
        sleep(1.2)
        myServo.value= -0.2
        ding.play()
        sleep(1.2)
        myServo.value= 0.2
        ding.play()
        sleep(1.2)
        myServo.value= -0.3
        ding.play()
        sleep(1.2)
        myServo.value= 0.3
        ding.play()
        sleep(1.2)
        myServo.value= 0
        GPIO.output(14,False)
        prevID = ID # Remember which spreadsheet row was just read out
        sleep(15)
    else:
        print("Same")
        breath.play() # Carry on breathing if no new rows in spreadsheet
        sleep(19.8)
        
    prevID = ID
