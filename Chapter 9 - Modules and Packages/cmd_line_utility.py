import argparse
import sys


def calculator(args):
    if args.o == "add":
        return args.a + args.b
    elif args.o == "sub":
        return args.a - args.b
    elif args.o == "mul":
        return args.a * args.b
    elif args.o == "div":
        if args.b != 0:
            return args.a / args.b
        else:
            return "Error: Division by zero is not possible"
    else:
        return "Invalid Entry!!!"
    

parse = argparse.ArgumentParser()
parse.add_argument("--a", type=float, default=1.0)
parse.add_argument("--b", type=float, default=2.0)
parse.add_argument("--o", type=str, default="add")

args = parse.parse_args()
sys.stdout.write(str(calculator(args)))
