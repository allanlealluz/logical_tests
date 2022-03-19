def parse_int(string):
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'twenty': 20,
        'hundred': 100,
        'thousand': 1000,
        'thirty': 30,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'million' : 1000000,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'forty': 40,
        'teen': 10,
        'ty': 10,
    }
    string = string.split()
    num = []
    for i,word in enumerate(string):
        if word in numbers and word != 'hundred' and word != 'thousand' and word != 'million':
            num.append(numbers[word])
        elif word.find('-') != -1:
            word = word.split('-')
            parse = [numbers[n] for n in word if n in numbers]
            tot = 0
            [tot := tot + x for x in parse]
            num.append(tot)
        else:
            num.append(word)
    for i,n in enumerate(num):
        s = ['t' for c,n in enumerate(num) if c > i and n == 'thousand']
        if n == 'hundred':
            if 't' not in s:
                num[i-1] *= 100
            else:
                num[i - 1] *= 100000
        elif n == 'thousand':
            num[i-1] *= 1000
        elif n == 'million':
            num[i - 1] *= 1000000
    t = 0
    resu = [t := t + n for n in num if isinstance(n,int) ]
    print(f'the result is {t}')
parse_int('one hundred two')
parse_int('three hundred nine')
parse_int('thirty-three thousand nine hundred fifty-eight')
parse_int('nine')
parse_int('thirty-four')
parse_int('fifty-eight')
parse_int('three hundred seven')
parse_int('one million ten thousand three hundred fifty-nine')
parse_int('ninety-four')
parse_int('seven hundred eighty-three thousand nine hundred  nineteen')