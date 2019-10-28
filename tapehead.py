import gspread
import pygame
import RPi.GPIO as GPIO
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
from Polly import Polly
from gpiozero import Servo

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setup(14, GPIO.OUT) #relay for laser & pump
GPIO.output(14,False)

high = .25

myGPIO=15 #Servo Control Pin

myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

pygame.init()
ding = pygame.mixer.Sound("/home/pi/Music/laser.wav")
breath = pygame.mixer.Sound("/home/pi/Music/slowbreathing.wav")

tts = Polly('Brian')
tts.say('Destroy All Humans')

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/SpeakingSpreadsheet-6728bef2aa63.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Pi').sheet1

def last_row(sheet, cols_to_sample=2):
  # looks for empty row based on values appearing in 1st N columns
  cols = sheet.range(1, 1, sheet.row_count, cols_to_sample)
  return max([cell.row for cell in cols if cell.value]) #+ 1

prevID=0

while True: 
    ID = last_row(sheet)
    if ID != prevID:
        print("Different")
        print(ID)
        cell = sheet.cell(ID, 3).value
        print(cell)
        myServo.value= 0
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
        sleep(1)
        tts.say(cell)
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
        prevID = ID
        sleep(15)
    else:
        breath.play()
        sleep(19.8)
        
    prevID = ID