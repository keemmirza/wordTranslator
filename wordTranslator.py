import goslate

def translator(sentence, language="en"):
    gs = goslate.Goslate();
    result = gs.translate(sentence, language)
    return result


val = input("Enter a sentence to translate : ")
print(translator(val, "malay"))
