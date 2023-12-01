import re

regex_map = {
    "%d": r"[-+]?\d+",
    "%f": r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?",
    "%s": r"\S+",
}

group_names = ["d", "f", "s"]


def scanf(line: str, format: str = None):
    if format is None:
        return auto_scanf(line)

    new_regex = format
    j = 0
    for i, key in enumerate(regex_map.keys()):
        regex = None
        while new_regex != regex:
            regex = new_regex
            new_regex = regex.replace(key, rf"(?P<G{j}>" + regex_map[key] + ")", 1)
            j += 1
        j -= 1

    match = re.match(regex, line)
    if match is None:
        return None

    str_values = list(match.groupdict().values())

    values = []
    for i in range(len(str_values)):
        try:
            values.append(int(str_values[i]))
        except ValueError:
            try:
                values.append(float(str_values[i]))
            except ValueError:
                values.append(str_values[i])
    return values


def auto_scanf(line: str):
    str_values = line.split()
    values = []
    for value in str_values:
        try:
            values.append(int(value))
        except ValueError:
            try:
                values.append(float(value))
            except ValueError:
                values.append(value)
    return values


if __name__ == "__main__":
    res = scanf("1.0abc23", "%f%s%d")
    print(res)
