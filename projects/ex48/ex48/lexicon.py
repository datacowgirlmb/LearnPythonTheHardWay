lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "down": 'direction',
    "up": 'direction',
    "left": 'direction',
    "right": 'direction',
    "back": 'direction',
    "go": 'verb',
    "stop": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "from": 'stop',
    "at": 'stop',
    "it": 'stop',
    "door": 'noun',
    "bear": 'noun',
    "princess": 'noun',
    "cabinet": 'noun'
}

def scan(sentence):
    words = sentence.split()
    results = []
    for word in words:
        word_type = lexicon.get(word.lower())
        
        if word_type != None:
            results.append((word_type, word))        
        elif word.isdecimal() == True:
            results.append(('number', int(word)))
        else:
            results.append(('error', word))
        
    return results