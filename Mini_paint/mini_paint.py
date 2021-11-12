import sys


def shape_empty(window, data):
    pos_x = int(data[1])
    pos_y = int(data[2])
    len_x = int(data[3])
    len_y = int(data[4])
    character = data[5]

    y = 0
    while y < len_y:
        x = 0
        while x < len_x:
            if (y == 0 or y == len_y - 1) or (x == 0 or x == len_x - 1):
                window[pos_y + y][pos_x + x] = character
            x += 1
        y += 1


def shape_full(window, data):
    pos_x = int(data[1])
    pos_y = int(data[2])
    len_x = int(data[3])
    len_y = int(data[4])
    character = data[5]

    y = 0
    while y < len_y:
        x = 0
        while x < len_x:
            window[pos_y + y][pos_x + x] = character
            x += 1
        y += 1


def fill_window(len_x, len_y, character):
    window = []

    y = 0
    while y < len_y:
        tmp_window = []
        x = 0
        while x < len_x:
            tmp_window.append(character)
            x += 1
        window.append(tmp_window)
        y += 1
    return window


def create_window(data):
    len_x = int(data[0])
    len_y = int(data[1])
    character = data[2]

    return fill_window(len_x, len_y, character)


def get_file_content(file):
    try:
        f = open(file, 'r')
        list_arg = f.read().splitlines()
        f.close()
    except OSError as err:
        list_arg = []
        print(err)
    return list_arg


def build_shape(list_arg, window):
    for elem in list_arg:
        if elem[0] == 'r':
            shape_empty(window, elem.split())
        elif elem[0] == 'R':
            shape_full(window, elem.split())


def parsing_drawing_line(window_arg):
    if not 0 < int(window_arg[0]) <= 300 or not 0 < int(window_arg[1]) <= 300 or len(window_arg) != 3:
        print("Error: parsing")
        sys.exit()


def parsing_rectangle_line(list_arg):
    for elem in list_arg:
        elem = elem.split()
        if not elem[0] == 'r' and not elem[0] == 'R' or len(elem) != 6:
            print("Error: parsing")
            sys.exit()


def parsing(list_arg):
    parsing_drawing_line(list_arg[0].split())
    parsing_rectangle_line(list_arg[1:])


def print_window(window):
    display = [''.join(elem) for elem in window]
    display = '\n'.join(display)
    print(display)


def main():
    if len(sys.argv) != 2:
        print("Error: argument")
    else:
        file = sys.argv[1]
        list_arg = get_file_content(file)
        if list_arg == []:
            return
        parsing(list_arg)
        window = create_window(list_arg[0].split())
        build_shape(list_arg[1:], window)
        print_window(window)


if __name__ == "__main__":
    main()
