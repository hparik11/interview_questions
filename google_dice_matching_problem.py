def dice(word, die):
    """
        word - String
        die - List[Char]
    """
    die = [tuple(x) for x in die]

    def helper(word, visited):
        if word == "":
            return True
        
        topCharacter = word[0]

        for d in die:
            if d not in visited:
                for topCharacter in d:
                    visited.add(d)
                    if helper(word[1:], visited):
                        return True
                    visited.remove(d)
        
        return False

    return helper(word, visited=set())
                

# Tests
# print(dice("hello", [['a', 'l', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'h', 'e', 'f'], ['a', 'b', 'c', 'd', 'o', 'f'], ['a', 'b', 'c', 'l', 'e', 'f']]))
# dice("hello", [['a', 'l', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'h', 'e', 'f'], ['a', 'b', 'c', 'd', 'o', 'f'], ['a', 'b', 'c', 'l', 'e', 'f']])
print(dice("aaaa", [['a', 'a','a','a','a','a'], ['b', 'b','b','b','b','b',], ['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'c', 'd', 'e', 'f']]))