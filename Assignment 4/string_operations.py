def reduce_whitespace(string):
    '''
    This function takes a list of strings and returns another list of strings after removing the extra white spaces.
    '''
    updated = []
    for i in string:
        i = " ".join(i.split())
        updated.append(i)
    return updated