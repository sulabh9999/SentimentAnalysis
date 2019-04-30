def getReplaceDict():
    return {
        'not able to': 'cant',
        'log in': 'login',
        'logging': 'login',
        'pop up': 'popup',
        'sign up': 'signup',
        'never': 'dont',
        'opening': 'open',
        'unable to': 'cant',
        'does not': 'cant',
        'doesn\'t': 'cant'
    }

def replaceWords(sentence):
    worsToReplace = getReplaceDict()
    for key, value in worsToReplace.items():
        sentence = sentence.replace(key, value, 1000)
    return sentence