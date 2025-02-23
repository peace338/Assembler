import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='directory of asm file to be translated')

    return parser.parse_args()

def main(args: argparse.Namespace):

    print(args.input)
        
if __name__ == "__main__":
    args = parse_args()
    main(args)