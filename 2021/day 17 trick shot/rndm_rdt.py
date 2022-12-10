sample = """target area: x=20..30, y=-10..-5"""

my = """# target area: x=150..171, y=-129..-70"""


def parse_data(data):
    # target area: x=241..273, y=-97..-63
    coords = {"x": [], "y": []}
    data = data.split()
    for line in (line for line in data if "=" in line):
        for coord in (coord for coord in line.strip(",")[2:].split("..")):
            coords[line[0]].append(int(coord))

    return coords


def launch_probe(velocity, target):
    p_x, p_y = [0, 0]
    v_x, v_y = velocity
    t_x = sorted(target["x"])
    t_y = sorted(target["y"])
    max_y = p_y
    while (
        p_x < max(t_x) + 1
        and ((v_x != 0 or p_x >= min(t_x)))
        and (p_x <= min(t_x) or p_y >= min(t_y))
    ):
        p_x += v_x
        p_y += v_y
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        if p_y > max_y:
            max_y = p_y
        if (p_x in range(min(t_x), max(t_x) + 1)) and (
            p_y in range(min(t_y), max(t_y) + 1)
        ):

            return True, velocity, max_y

    return False, velocity, max_y


def main():
    target = parse_data(my)
    max_y = 0
    optimal = []
    count = 0
    for x in range(1, max(target["x"]) * 2):
        for y in range(min(target["y"]), max(target["x"])):
            r, velocity, this_max_y = launch_probe([x, y], target)
            if r == True:
                count += 1
                if this_max_y > max_y:
                    max_y = this_max_y
                    optimal = velocity

    print(optimal)
    print(max_y)
    print(count)


if __name__ == "__main__":
    main()
