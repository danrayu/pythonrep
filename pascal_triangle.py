def p_triangle_drawer(height):
    levels_array = []
    previous_layer = []
    for level in range(height):
        level_array = []
        for index in range(1, level+2):
            level_array.append(1)
        levels_array.append(level_array)

    for level in range(1, len(levels_array) + 1):
        current_layer = levels_array[level - 1]
        for index in range(level):
            if index == 0 or index == level - 1:
                digit = 1
            else:
                digit = previous_layer[index - 1] + previous_layer[index]
            current_layer[index] = digit
        previous_layer = current_layer
        if level:
            levels_array[level - 1] = current_layer

    for level in range(1, len(levels_array) + 1):
        current_layer = ''
        for digit in levels_array[level - 1]:
            current_layer += str(digit) + ' '
        print(' ' * (height - level), current_layer)


p_triangle_drawer(7)
