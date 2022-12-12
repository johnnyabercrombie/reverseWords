# Reverse the letters of the words in a sentence such as:
# the big black cat -> eht gib kcalb tac
def reverseWords(sentence):
    newWords = []
    words = sentence.split(" ")

    for word in words:
        # Reverse the word
        newWord = ""
        for letter in word[::-1]:
            newWord += letter
        newWords.append(newWord)

    newSentence = " ".join(newWords)

    return newSentence


if __name__ == "__main__":
    words = reverseWords("the big black cat")
    assert words == "eht gib kcalb tac"
