#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=argparse.FileType('r\
'), default='hidden_4.pyc')
    args = parser.parse_args()

    for line in sorted(args.filename):
        if not line.startswith("__"):
            print(line.strip())
