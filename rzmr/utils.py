import pymorphy3


MORPH = pymorphy3.MorphAnalyzer()


def get_loct(word: str) -> str:
    word_parse = MORPH.parse(word)[0]
    word_loct = word_parse.inflect({'loct'}).word
    return word_loct
