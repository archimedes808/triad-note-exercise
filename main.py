triads = {
    'a': {
        'major': 'a c# e',
        'minor': 'a c e',
        'augmented': 'a c# e#',
        'diminished': 'a c eb'
    },
    'b': {
        'major': 'b d# f#',
        'minor': 'b d f#',
        'augmented': 'b d# f##',
        'diminished': 'b d f'
    },
    'c': {
        'major': 'c e g',
        'minor': 'c eb g',
        'augmented': 'c e g#',
        'diminished': 'c eb gb'
    },
    'd': {
        'major': 'd f# a',
        'minor': 'd f a',
        'augmented': 'd f# a#',
        'diminished': 'd f ab'
    },
    'e': {
        'major': 'e g# b',
        'minor': 'e g b',
        'augmented': 'e g# b#',
        'diminished': 'e g bb'
    },
    'f': {
        'major': 'f a# c#',
        'minor': 'f a c#',
        'augmented': 'f a# c##',
        'diminished': 'f a c'
    },
    'g': {
        'major': 'g b d',
        'minor': 'g bb d',
        'augmented': 'g b d#',
        'diminished': 'g bb db'
    }
}

for natural, triads in triads.items():
    for triad, notes in triads.items():
        while True:
            answer = input(f"{natural} {triad}:")
            if answer.strip().lower() == notes:
                print('correct')
                break
            else:
                print('incorrect. try again')
