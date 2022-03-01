"""
Level 1
Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""

class Temperature:

    def __init__(self,f,c):
        self.f = f
        self.c = c

    def convertFahrenheit(self):
        fahrenheit = self.c*(9/5)+32
        print("Fahrenheit value of",self.c,"celcius is",fahrenheit,"fahrenheit")
    
    def convertCelsius(self):
        celcius = (self.f-32)*(5/9)
        print("Celcius value of",self.f,"fahrenheit is",celcius,"celcius")


t = Temperature(98,32)
t.convertFahrenheit()
t.convertCelsius()