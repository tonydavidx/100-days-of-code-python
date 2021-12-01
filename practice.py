def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for s in string_:
        if s in vowels:
            string_ = string_.replace(s, '')
    return string_


print(disemvowel('This website is for losers LOL!'))
