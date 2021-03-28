#!/usr/local/bin/python3
import glob
import sys

def get_solution(day_string):
    solution_module = __import__(f'{day_string}.solution', fromlist=['Solution'])
    solution = getattr(solution_module, 'Solution')();
    solution.print_solutions()
    pass

def main():
    available_days = set(glob.glob('day[0-2][0-9]'))
    day = input('Select day: ')
    if day is None or day == '':
        print('You didn\'t enter a day')
        sys.exit()
    day_string = 'day' + f'0{day}' if int(day) < 10 else day
    if day_string not in available_days:
        print('You didn\'t enter a solved day')
    get_solution(day_string)

if __name__ == '__main__':
    main()


