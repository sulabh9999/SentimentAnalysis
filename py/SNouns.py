def getNounList(sentence='', tokens = []):
    from nltk import word_tokenize, pos_tag
    if len(tokens) > 0:    
        nouns = [token for token, pos in pos_tag(tokens) if pos.startswith('NN')]
        return nouns
    else:
        nouns = [token for token, pos in pos_tag(word_tokenize(sentence)) if pos.startswith('NN')]
        return nouns