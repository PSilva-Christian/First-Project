# Functions #

def result(letter: int, sentence: int, coleman: int) -> None:
    if coleman < 1:
        print(f"\tLetters: {letter} - Sentences: {sentence} - Grade: Before Grade 1\n")
    elif coleman > 16:
        print(f"\tLetters: {letter} - Sentences: {sentence} - Grade: 16+\n")
    else:
        print(f"\tLetters: {letter} - Sentences: {sentence} - Grade: {coleman}\n")

def calc_coleman(letter: int, sentence: int, word: int) -> int:
    coleman_l = float(letter / word) * 100
    coleman_s = float(sentence / word) * 100
    return round((coleman_l * 0.0588) - (coleman_s * 0.296) - 15.8)


# Main #

alphabet_chars = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                  'u','v','w','x','y','x','z']

end_sentence_chars = ['.','!','?']

with open("input.txt", "r") as file:

    for linha in file:

        print(linha, end="")
        words = letters = sentences = 0
        if linha != EOFError:

            for char in linha:

                if char in end_sentence_chars:
                    sentences += 1

                elif char == " ":
                    words += 1

                elif char.isalpha():
                    letters += 1

        result(letters, sentences, calc_coleman(letters, sentences, ( words + 1)))




