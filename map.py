import sys


def read_inputs(file):
    for line in file:
        line = line.strip()
        yield line.split()


if __name__ == '__main__':
    file = sys.stdin
    lines=read_inputs(file)
    for words in lines:
        for word in words:
            print("{}\t{}".format(word, 1))