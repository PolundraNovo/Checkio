# Next Birthday
# Task: https://py.checkio.org/en/mission/next-birthday/


from typing import Dict, Tuple
from datetime import date, timedelta


Date = Tuple[int, int, int]


def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:
    d1 = date(today[0], today[1], today[2])
    to_go = 400  # day to nearest birthday
    kto = {}
    for item in birthdates:
        d_birth = date(birthdates[item][0], birthdates[item][1], birthdates[item][2])
        years = today[0] - birthdates[item][0]
        try:   # check February, 29
            d_birth = d_birth.replace(year=d_birth.year + years)  # add years to next birthday
        except:
            d_birth = d_birth.replace(year=d_birth.year + years, month = 3, day = 1)
        if d_birth < d1: # go to next year
            years +=1
            try:   # check February, 29
                d_birth = d_birth.replace(year=d_birth.year + 1)
            except:
                d_birth = d_birth.replace(year=d_birth.year + 1, month = 3, day = 1)
        print(d_birth)
        delta = d_birth - d1
        if delta.days <= to_go: # our new candidate
            if delta.days < to_go: # clear dictionary (if need)
                kto = {}
            to_go = delta.days 
            kto[item] = years  # add item to dictionary
    return ((to_go, kto))


if __name__ == '__main__':
    FAMILY = {
        'Brian': (1967, 5, 31),
        'Lena': (1970, 10, 3),
        'Philippe': (1991, 6, 15),
        'Yasmine': (1996, 2, 29),
        'Emma': (2000, 12, 25),
    }

    TESTS = [
        ((2020, 9, 8), (25, {'Lena': 50})),
        ((2021, 10, 4), (82, {'Emma': 21})),
        ((2022, 3, 1), (0, {'Yasmine': 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f'You failed the test #{nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answer}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')