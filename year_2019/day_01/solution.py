import math
from year_2019.utils.solution_template import SolutionTemplate

def get_fuel_per_weight(weight):
    fuel_needed = math.floor(weight / 3) - 2
    if fuel_needed <= 0:
        return 0

    return fuel_needed + get_fuel_per_weight(fuel_needed)

class Solution(SolutionTemplate):
    @staticmethod
    def _clean_input(input):
        new_input = [int(line) for line in input.split('\n') if line != '']
        return new_input

    def part_1(self):
        fuel_per_part = [math.floor(part / 3) - 2 for part in self.data]
        return sum(fuel_per_part)

    def part_2(self):
        fuel_per_part = [get_fuel_per_weight(part) for part in self.data]
        return sum(fuel_per_part)




