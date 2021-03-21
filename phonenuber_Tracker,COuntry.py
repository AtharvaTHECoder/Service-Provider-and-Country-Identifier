import phonenumbers
import pyttsx3
from phonenumbers import geocoder
from phonenumbers import carrier

engine = pyttsx3.init()
engine.say('Please enter your number with the country code')
engine.runAndWait()
number = input('Please enter your number with the country code:')
serviceProvider = phonenumbers.parse(number,'RO')
conNum = phonenumbers.parse(number,"CH")
region = geocoder.description_for_number(conNum, 'en')
engine.say('Your region is'+ region)
print('Your region is', region)
iSP = carrier.name_for_number(serviceProvider,"en")
print('Your service provider is', iSP)
engine.say('Your service provider is'+ iSP)
engine.runAndWait()