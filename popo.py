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
        'nineteen': 90,
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
    total = 0
    num = []
    for i, word in enumerate(string):
        n = string[i - 1]
        if n.find('-') != -1:
            parse = n.split('-')
            data = [numbers[n] for n in parse if n in numbers]
            tot = 0
            [tot := tot + x for x in data]
            n = tot
            if len(string) == 1:
                print(tot)
        else:
            n = numbers[n]
        if word == 'hundred':
            total += n * 100
        elif word == 'thousand':
            total += n * 1000
        elif word == 'million':
            total += n * 1000000
        elif word in numbers:
            total += numbers[word]
    print(total)
parse_int('one hundred two')
parse_int('three hundred nine')
parse_int('thirty-three thousand nine hundred fifty-eight')
parse_int('nine')
parse_int('thirty-four')
parse_int('fifty-eight')