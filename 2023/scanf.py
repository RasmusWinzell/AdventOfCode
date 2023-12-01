import re

regex_map = {
    "%d": r"[-+]?\d+",
    "%f": r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?",
    "%s": r"\S+",
}


def scanf(line: str, format: str = None):
    if format is None:
        return auto_scanf(line)

    regex = format
    for key in regex_map.keys():
        regex = regex.replace(key, r"(\S+)")

    match = re.match(regex, line)
    if match is None:
        return None

    values = []
    for i in range(1, len(match.groups()) + 1):
        try:
            values.append(int(match.group(i)))
        except ValueError:
            try:
                values.append(float(match.group(i)))
            except ValueError:
                values.append(match.group(i))
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
