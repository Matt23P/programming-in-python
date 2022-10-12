import argparse
import args

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", "--help", help="Display help menu")
    parser.add_argument("-c", "--config", help="")
    parser.add_argument("-d", "--dir", help="")
    parser.add_argument("-l", "--log", help="")
    parser.add_argument("-r", "--rounds", help="")
    parser.add_argument("-s", "--sheep", help="")
    parser.add_argument("-w", "--wait", help="")

    args = parser.parse_args()
    if args.help:
        print("test")