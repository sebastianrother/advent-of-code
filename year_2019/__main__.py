import glob
import sys

def get_solution(day_string):
    solution_module = __import__(f'year_2019.{day_string}.solution', fromlist=['Solution'])
    solution = getattr(solution_module, 'Solution')();
    solution.print_solutions()

def main():
    available_days = set(glob.glob('year_2019/day_[0-2][0-9]'))
    day = input('Select day: ')
    if day is None or day == '':
        print('You didn\'t enter a day')
        sys.exit()
    print(available_days)
    day_string = 'day_' + f'0{day}' if int(day) < 10 else day
    if 'year_2019/' + day_string not in available_days:
        print('You didn\'t enter a solved day')
        sys.exit()
    get_solution(day_string)

if __name__ == '__main__':
    main()


