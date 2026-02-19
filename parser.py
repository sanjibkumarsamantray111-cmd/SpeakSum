# # parser.py

# odia_units = {
#     "ଶୁନ୍ୟ": 0,
#     "ଏକ": 1,
#     "ଦୁଇ": 2,
#     "ତିନି": 3,
#     "ଚାରି": 4,
#     "ପାଞ୍ଚ": 5,
#     "ଛଅ": 6,
#     "ସାତ": 7,
#     "ଆଠ": 8,
#     "ନଅ": 9,
# }

# odia_tens = {
#     "ଦଶ": 10,
#     "କୋଡିଏ": 20,
#     "ତିରିଶ": 30,
#     "ଚାଳିଶ": 40,
#     "ପଚାଶ": 50,
#     "ଷାଠି": 60,
#     "ସତର": 70,
#     "ଅଶୀ": 80,
#     "ନବେ": 90,
# }

# odia_scales = {
#     "ଶହ": 100,
#     "ହଜାର": 1000,
# }


# def parse_odia_number(text):
#     text = text.strip()

#     # Normalize combined words
#     text = text.replace("ଏକଶହ", "ଏକ ଶହ")
#     text = text.replace("ଦୁଇଶହ", "ଦୁଇ ଶହ")
#     text = text.replace("ତିନିଶହ", "ତିନି ଶହ")
#     text = text.replace("ପାଞ୍ଚଶହ", "ପାଞ୍ଚ ଶହ")

#     words = text.split()

#     total = 0
#     current = 0

#     for word in words:
#         if word in odia_units:
#             current += odia_units[word]

#         elif word in odia_tens:
#             current += odia_tens[word]

#         elif word in odia_scales:
#             if current == 0:
#                 current = 1
#             current *= odia_scales[word]
#             total += current
#             current = 0

#     return total + current



# parser.py

english_units = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

english_teens = {
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
}

english_tens = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

scales = {
    "hundred": 100,
    "thousand": 1000,
}


def parse_english_number(text):
    words = text.lower().split()
    total = 0
    current = 0

    for word in words:
        if word in english_units:
            current += english_units[word]

        elif word in english_teens:
            current += english_teens[word]

        elif word in english_tens:
            current += english_tens[word]

        elif word in scales:
            if current == 0:
                current = 1
            current *= scales[word]
            total += current
            current = 0

    return total + current