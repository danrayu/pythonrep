class BrickLayer:
    #asks for inputs for the N and M dimension
    def input_n_m(self):
        print("Hello! Type in the height (N) and the width (M) in the format (N M) N and M shouldn't exceed 100:")
        while True:
            raw_input_size = input()
            n_and_m = raw_input_size.split(" ")
            try:
                n = int(n_and_m[0])
                m = int(n_and_m[1])
                if len(n_and_m) > 2 or n not in range(100) or m not in range(100):
                    raise Exception('')
                if n*m % 2 != 0:
                    raise Exception('Uneven number of cells will have no solution.')
                break
            except Exception as ex:
                print(ex, "Incorrect input. Type in the length (N) and the width (M) in the format (N*M):")
        return n, m


    #creates the first brick layer from user inputs
    def input_bricks(self, n):
        layer1 = []
        long_brick_check = ''
        for row in range(n):
            while True:
                print("Current row:", row, "Type in a row of numbers separated by a space:")
                raw_input_row = input()
                numbers = raw_input_row.split(" ")
                for number in numbers:
                    long_brick_check += str(number)
                    if not number.isdigit():
                        print("Input should be digits. Type in again:")
                        continue
                layer1.append(numbers)
                break
        for index in long_brick_check:
            if long_brick_check.count(index) > 2:
                print("Bricks with abnormal sizes found. Try again.")
                self.input_bricks(n)
        return layer1


    #creates an empty second layer to be filled in later
    def create_layer2(self, layer1):
        layer2 = []
        for row in layer1:
            new_row = []
            for item in row:
                new_row.append('')
            layer2.append(new_row)
        return layer2


    #solves layer 2, and prints it out
    def solve_layer2(self, layer1, layer2):
        brick_index = 1
        for row in range(len(layer1)):
            for row_item in range(len(layer1[0])):
                if layer2[row][row_item] == '':
                    if row_item != len(layer1[0])-1 and layer1[row][row_item] != layer1[row][row_item + 1]:
                        layer2[row][row_item] = brick_index
                        layer2[row][row_item + 1] = brick_index
                        brick_index += 1
                    elif layer1[row][row_item] != layer1[row + 1][row_item]:
                        layer2[row][row_item] = brick_index
                        layer2[row + 1][row_item] = brick_index
                        brick_index += 1
                    else:
                        raise Exception('-1')
        for row in layer2:
            print(row)

bl = BrickLayer()
n_m = bl.input_n_m()
n = n_m[0]
m = n_m[1]

layer1 = bl.input_bricks(n)

layer2 = bl.create_layer2(layer1)

bl.solve_layer2(layer1, layer2)
