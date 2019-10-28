# TapeHead
Python script used in the Dr. Tape Head project.

Dr.Tape Head is based on a Raspberry Pi and retrieves text from a Google Sheets spreadsheet, fed by IFTTT, reading it out with Amazon's Polly text to speech service. While reading lasers shoot from his eyes, smoke is generated and his mouth lights up thanks to a Pimoroni pHAT Beat. 

The project is documented at:

Instructables: https://www.instructables.com/id/Dr-Tape-Head-Undead-Media

Youtube: https://youtu.be/mykrJEozIoM

--------

The code here may be useful but there are quite a few prerequisites before it will work, as it was designed for this specific use-case. 

For this project the setup steps needed in advance of running the code were:

- Set up the Pimoroni pHAT Beat: https://shop.pimoroni.com/products/phat-beat

- Set up Amazon Polly: Guide at http://catqbat.com/make-your-pi-speak-with-text-to-speech-fom-amazon-polly/

- Set up a Google Sheets spreadsheet for access via Python: https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2
