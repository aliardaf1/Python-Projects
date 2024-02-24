import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

 if wanted := re.search(r'(?:src="http).+\/embed\/(.+?)"', s):
        return f'https://youtu.be/{wanted.group(1)}'

if __name__ == "__main__":
    main()