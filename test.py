from calculator_core import VoiceCalculatorCore

calc = VoiceCalculatorCore()

print(calc.add_spoken_number("କୋଡିଏ"))
print(calc.add_spoken_number("ତିରିଶ ପାଞ୍ଚ"))
print(calc.add_spoken_number("ଏକଶହ"))
print(calc.add_spoken_number("ପାଞ୍ଚଶହ"))
print(calc.add_spoken_number("ଦୁଇ ହଜାର ପାଞ୍ଚଶହ"))

print("Final Total:", calc.get_total())