import sys
from pathlib import PurePath, Path
import inspect

class SolutionTemplate:
    def __init__(self, input = None):
        self.input_override = False

        if input is not None:
            self.input_override = True
            self.input = input
        else:
            self.input = self._get_input()
        self.data = self._clean_input(self.input)

    @property
    def input_path(self):
        base_path = Path(inspect.getmodule(self).__file__).parent
        return PurePath.joinpath(base_path, 'input.txt')

    def _get_input(self):
        try:
            with open(self.input_path, 'r') as raw_input:
                input = raw_input.read()
        except FileNotFoundError:
            print('No input file found, please make sure an input.txt file has been provided')
            sys.exit()
        return input

    @staticmethod
    def _clean_input(input):
        new_input = [line for line in input.split('\n') if line != '']
        return new_input

    def part_1(self):
        pass

    def part_2(self):
        pass

    def print_solutions(self):
        print(f'Solution part 1: {self.part_1()}')
        print(f'Solution part 2: {self.part_2()}')
