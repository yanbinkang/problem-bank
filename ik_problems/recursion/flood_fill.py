import sys

textmap = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""


def get_world_from_textmap(some_text):
    world_width = len(some_text.strip().split('\n')[0])
    world_height = len(some_text.strip().split('\n'))

    text_map = some_text.strip().split('\n')

    world = []
    for i in range(world_width):
        world.append([''] * world_height)

    for x in range(world_width):
        for y in range(world_height):
            world[x][y] = text_map[y][x]
    return world


def print_world(world):
    world_width = len(world)
    world_height = len(world[0])

    for y in range(world_height):
        for x in range(world_width):
            sys.stdout.write(world[x][y])
        sys.stdout.write('\n')


def flood_fill(world, x, y, old_char, new_char):
    world_width = len(world)
    world_height = len(world[0])

    if old_char == None:
        old_char = world[x][y]

    if world[x][y] != old_char:
        return

    world[x][y] = new_char

    if x > 0:  # left
        flood_fill(world, x - 1, y, old_char, new_char)

    if y > 0:  # up
        flood_fill(world, x, y - 1, old_char, new_char)

    if x < world_width - 1:  #right
        flood_fill(world, x + 1, y, old_char, new_char)

    if y < world_height - 1:  #down
        flood_fill(world, x, y + 1, old_char, new_char)


def main():
    world = get_world_from_textmap(textmap)
    print_world(world)
    print()

    flood_fill(world, 5, 8, None, "+")
    print_world(world)
    print()

    flood_fill(world, 0, 0, None, "s")
    print_world(world)
    print()


if __name__ == '__main__':
    main()
