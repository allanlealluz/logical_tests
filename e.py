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
    if len(string) == 1:
        string = ''.join(string)
        if string.find('-') != -1:
            parse = string.split('-')
            print(parse)
            values = [numbers[word] for word in parse if word in numbers]
            tot = 0
            [tot := tot + x for x in values]
            print(tot)
        else:
            print(numbers[string])
            return numbers[string]
    else:
        total = 0
        num = []
        for i,word in enumerate(string):
            n = string[i - 1]
            if word in numbers and word != 'hundred':
                num.append(numbers[word])
            if word == 'hundred':
                print(int(num[-1]) )
                total += int(num[-1]) * 100
            elif word == 'thousand':
                total += int(num[-1]) * 1000
            elif word == 'million':
                total += int(num[-1]) * 1000000
            elif word.find('-') != -1:
                parse = word.split('-')
                print(parse)
                values = [numbers[word] for word in parse if word in numbers]
                tot = 0
                [tot := tot + x for x in values ]
                total += tot
                print(tot)
            elif word in numbers:
                print(numbers[word])
                total += numbers[word]
        print(f'total = {total}')
parse_int('one hundred two')
parse_int('three hundred nine')

