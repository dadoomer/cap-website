

def ignoreChar(c):
    '''Check if a character c should be ignored.
        Opening and closing brackets and parenthesis should not be ignored.
    '''
    if(c in ['(', ')']):
        return False
    else:
        return True

def checkParenthesis(word):
    '''Check if a string is properly parenthesized.
    The function returns a boolean True or false depending on
    whether the word is properly parenthesized or not.
    Base case:
        Words of length zero are always properly parenthesized.
    Inductive case 1:
        If the first letter in a word is not a parenthesis or a bracket,
        the word is properly parenthesized if the rest of the word is properly parenthesized
    Inductive cases 2 and 3:
        If the first letter is  '(', call completeRound
        to check until the matching ')'.
        If they failed to find a match, return False. Otherwise,
        check the rest of the word.
    '''
    # print 'checkParenthesis' + word
    if(len(word)==0):
        return True
    if ignoreChar(word[0]):
        return checkParenthesis(word[1:])
    if word[0] == '(':
        rv, newword = completeRound(word[1:])        
        if(not rv):
            return False    
        return checkParenthesis(newword)
    return False



def completeRound(word):
    '''
        The function assumes that word contains the text immediately
        after an opening parenthesis. It will check parenthesization between
        the beginning of word and the matching closing parenthesis.        
        The function returns a pair (b, rest), where b is a boolean describing
        whether it encountered an error, and rest is the rest of the word
        after the matching closing parenthesis.
        Base case 1:
            If the word is of length zero, it means there was no text after
            the opening parenthesis. This is an error, so the function should
            return (False, something). It doesn't matter what something is,
            because it should be ignored.

        Base case 2:
            If the first character is a closing round parenthesis ')', we have found a match,
            so we can return (True, rest), where rest is the rest of the word after the closing parenthesis.

        Base case 3:
            If the first character is a closing square bracket this is an error, because we were
            looking for a closing *round* parenthesis. We should then return (False, something)
            
        Inductive case 1:
            If the first letter is not a parenthesis or a bracket, it can be ignored.
            The return values should be the same as if the function had been called with word[1:] instead of with word.
        Inductive case 2:
            Can you figure out the details of what happens when the first
            character is an opening parenthesis '('?
            Hint: we need to find a match for this new open parenthesis before
            we can continue looking for a match for the current open parenthesis
            in the rest of the word.
    '''
    if(len(word) == 0):
        return False, word
    if ignoreChar(word[0]):
        return completeRound(word[1:])
    if word[0] == ')': # completed the round, so far so good.
        return True, word[1:]
    if word[0] == '(':
        rv, newword = completeRound(word[1:])        
        if(not rv):
            return False, word 
        return completeRound(newword)
    return False, word



def testerFunction(checker):
    def check(instr, expected):
        if( checker(instr) != expected ):
            print 'Test for "' + instr + '" failed '
            return False
        else:
            print 'Test for "' + instr + '" passed'
        return True
    #The following should be true
    rv = True
    rv = check('( x (y + z ) w(a b c))(t + x(z))', True) and rv
    rv = check('((()() )(  (u)(  x )))', True) and rv    
    #The following should be false
    rv = check(')(())(', False) and rv
    rv = check('(x + y (z)', False) and rv
    rv = check(') ()', False) and rv
    rv = check(')))))))))) ()', False) and rv
    rv = check('())', False) and rv
    #Add more of your own tests here.

    
    if(rv):
        print 'All tests passed!'


testerFunction(checkParenthesis)
