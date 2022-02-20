morse_code = {
    " ": "",
    "A": "•—",
    "B": "—•••",
    "C": "—•—•",
    "D": "—••",
    "E": "•",
    "F": "••—•",
    "G": "——•",
    "H": "••••",
    "I": "••",
    "J": "•———",
    "K": "—•—",
    "L": "•—••",
    "M": "——",
    "N": "—•",
    "O": "———",
    "P": "•——•",
    "Q": "——•—",
    "R": "•—•",
    "S": "•••",
    "T": "—",
    "U": "••—",
    "V": "•••—",
    "W": "•——",
    "X": "—••—",
    "Y": "—•——",
    "Z": "——••",
    "1": "•————",
    "2": "••———",
    "3": "•••——",
    "4": "••••—",
    "5": "•••••",
    "6": "—••••",
    "7": "——•••",
    "8": "———••",
    "9": "————•",
    "0": "—————",
}


def get_char(val):
    for key, value in morse_code.items():
        if val == value:
            return key
    return "key does not exist"


is_the_program_run = True
while is_the_program_run:
    menu = input("Type encode or decode or end:")
    if menu == "end":
        is_the_program_run = False
    elif menu == "encode":
        text = input("Please provide text to encode:")
        text_to_encode = text.upper()
        converted_string = ""

        for char in text_to_encode:
            try:
                converted_string += morse_code[char]
            except KeyError:
                print("Unknown char")
        print(converted_string)
    elif menu == "decode":
        text = input("Please provide text to decode (use '*' for dot and '-' for dash:")
        text = text.replace("*", "•")
        text = text.replace("-", "—")
        text = text.split(" ")
        new_text = []
        for word in text:
            if "/" in word:
                for e in word.split("/"):
                    new_text.append(e)
            else:
                new_text.append(word)
        decoded_text = ""
        for char in new_text:
            decoded_text += get_char(char)

        print(decoded_text)
