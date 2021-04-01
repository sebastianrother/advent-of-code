from year_2019.utils.solution_template import SolutionTemplate

class Solution(SolutionTemplate):
    @staticmethod
    def _clean_input(input):
        new_input = [int(num) for num in input.split(',')]
        return new_input

    def part_1(self):
        data = self.data.copy()
        if not self.input_override:
            data[1] = 12
            data[2] = 2
        for index in range(0, len(data), 4):
            command = data[index]
            if command == 99:
                return data[0]

            input_01 = data[index + 1]
            input_02 = data[index + 2]
            output = data[index + 3]

            if command == 1:
                data[output] = data[input_01] + data[input_02]

            if command == 2:
                data[output] = data[input_01] * data[input_02]

    def part_2(self):
        TARGET = 19690720

        for new_verb in range(0, len(self.data)):
            for new_noun in range(0, len(self.data)):
                data = self.data.copy()
                data[1] = new_verb
                data[2] = new_noun
                for index in range(0, len(data), 4):
                    command = data[index]

                    if command not in [1, 2, 99]:
                        break

                    if command == 99:
                        break

                    input_01 = data[index + 1]
                    input_02 = data[index + 2]
                    output = data[index + 3]

                    if command == 1:
                        data[output] = data[input_01] + data[input_02]

                    if command == 2:
                        data[output] = data[input_01] * data[input_02]

                if data[0] == TARGET:
                    return new_verb * 100 + new_noun
