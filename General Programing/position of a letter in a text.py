def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position2("K4imutaipwpqdkoqwe3irf34rdk3p4o                     ???????!!!!!!!!!!!!n  !!!!!!!!!!"))
