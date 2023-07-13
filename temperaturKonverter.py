#1)
class Temperatur:
    def __init__(self, temperatur, enhet):
        if enhet == "celsius" or enhet == "celsius" or enhet == "c" or enhet == "C":
            self._temperatur = temperatur
        elif enhet == "fahrenheit" or enhet == "Fahrenheit" or enhet == "f" or enhet == "F":
            self._temperatur = (temperatur - 32) * (5 / 9)
        elif enhet == "kelvin" or enhet == "Kelvin" or enhet == "k" or enhet == "K":
            self._temperatur = temperatur - 273.15


    def hent_celsius(self):
        return self._temperatur


    def hent_fahrenheit(self):
        fahrenheit = (self._temperatur * 9/5) + 32
        return fahrenheit


    def hent_kelvin(self):
        kelvin = self._temperatur + 273.15
        return kelvin

temp = Temperatur(73.4, "f")
print(f"Celsius: {temp.hent_celsius():.2f}")
print(f"Fahrenheit: {temp.hent_fahrenheit():.2f}")
print(f"Kelvin: {temp.hent_kelvin():.2f}")
