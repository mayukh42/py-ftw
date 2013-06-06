# pig_latin.py
'''
Pig Latin: boot -> ootbay; image -> imagehay
consonants considered together: th, st, qu, pl, or tr
stop -> opstay, there -> erethay etc
'''

vowels = 'aeiou'
pairs = ['pl','qu','st','th','tr']

def convert(word):
    word = word.lower()
    l = len(word)
    if l <= 1:
        return word
    else:
        if word[0] in vowels:
            return word + 'hay'
        else:
            if l > 2 and word[:2] in pairs:
                return word[2:] + word[:2] + 'ay'
            else:
                return word[1:] + word[0] + 'ay'

def convert_phrase(phrase):
    phrase = phrase.lower()
    words = phrase.split()
    ans = ''
    for word in words:
        ans += convert(word) + ' '
    return ans


def main():
    print convert('boot')
    print convert('image')
    print convert_phrase('My name is John Smith')
    print convert_phrase('stop there')


if __name__ == '__main__':
    main()
