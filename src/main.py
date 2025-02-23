import argparse


def parse_args(known=False) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='directory of asm file to be translated')
    args = parser.parse_known_args()[0] if known else parser.parse_args()

    return args

def main(args: argparse.Namespace):

    print(args.input)
        
if __name__ == "__main__":
    opt = parse_args()
    main(opt)