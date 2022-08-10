import argparse
import os
import subprocess


def parse_args() -> argparse.Namespace:
    arguments_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    arguments_parser.add_argument(
        "dir",
        nargs="?",
        default=os.getcwd(),
        type=str,
        help="Directory where to use isort and black (defaults to current directory)",
    )
    arguments_parser.add_argument(
        "--line-length",
        default=80,
        type=int,
        required=False,
        help="Parameter for black with same name, determines max. length for formatter.",
    )
    args = arguments_parser.parse_args()
    return args


def main() -> None:
    args = parse_args()

    subprocess.run(
        ["black", "--line-length", f"{args.line_length}", f"{args.dir}"]
    )
    subprocess.run(["isort", f"{args.dir}"])
