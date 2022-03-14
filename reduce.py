# reduce函数以此读出经过排序后的map函数的输出，并统计单词的计数
import sys


def read_map_outputs(file):
    for line in file:
        yield line.strip().split("\t", 1)


def main():
    current_word = None
    word_count = 0
    lines = read_map_outputs(sys.stdin)
    for word, count in lines:
        try:
            count = int(count)
        except ValueError:
            continue
        if current_word == word:
            word_count += count
        else:
            if current_word:
                print("{}\t{}".format(current_word, word_count))
            current_word=word
            word_count=count
    if current_word:
        print("{}\t{}".format(current_word, word_count))


if __name__ == '__main__':
    main()