class VoiceCalculatorCore:

    def __init__(self):
        self.numbers = []

    def add_spoken_number(self, spoken_text):

        cleaned = spoken_text.replace(" ", "")

        if cleaned.isdigit():
            number = int(cleaned)
            self.numbers.append(number)

        return self.get_expression()

    def get_expression(self):
        return " + ".join(map(str, self.numbers)) + " +"

    def get_total(self):
        return sum(self.numbers)

    def clear(self):
        self.numbers = []