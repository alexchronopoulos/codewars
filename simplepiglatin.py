def pig_it(text):
    return ' '.join([(word[1:] + word[0] + 'ay')
                    if word not in ('!', '?')
                    else word
                    for word in text.split(' ')])

def test_answer():
    assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
