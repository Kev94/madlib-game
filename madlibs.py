test_string = "PLACE is really ADJECTIVE"
parts_of_speech = ["PLACE", "ADJECTIVE", "PERSON", "PLURALNOUN", "NOUN"]


def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced=[]
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word,parts_of_speech)
        if replacement != None:
            user_input = raw_input("Please enter a: " + replacement)
            word = word.replace(replacement,user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string,parts_of_speech)
