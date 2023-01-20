#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=argparse.FileType('r\
'), default='hidden_4.pyc')
    args = parser.parse_args()

    for line in args.filename:
        for character in line:
            if line[0] != "__":
                print(line.strip())
