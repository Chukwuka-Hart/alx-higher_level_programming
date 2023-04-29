#!/usr/bin/python3
"""Reads line from standard input and computes metrics.

After every ten lines or if the execution encounters a \
keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def display_stats(size, codes):
    """Print computed metrics.

        Args:
            size (int): The accumulated read file size.
            codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    from sys import stdin

    count = 0
    size = 0
    valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    codes = {}

    try:
        for line in stdin:
            if count == 10:
                display_stats(size, codes)
                code = 1
            else:
                count += 1
            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in valid:
                    if codes.get(line[-2], -1) == -1:
                        codes[line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass

        display_stats(size, codes)

    except KeyboardInterrupt:
        display_stats(size, codes)
        raise
