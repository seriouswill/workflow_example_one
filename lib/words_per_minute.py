def text_reader(wpm, text):
    if type(wpm) != int:
        print(f"position one {wpm}")
        return "The words per minute arguement is not an integer"
    else:
        print(f"position two {wpm}")
        text = text.split(" ")
        words_read = wpm * 5
        text = text[0:words_read]
        return " ".join(text)
