import argparse
import sys
from typing import Tuple

from {{cookiecutter.module_name}}.{{cookiecutter.module_name}} import main

_possible_modes = ["train", "process", "export"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train, export or run a deep learning model."
    )
    parser.add_argument(
        "mode",
        metavar="MODE",
        type=str,
        help="Mode to run the program with (train, process or export)",
    )

    args = parser.parse_args()

    return args


def check_args(args: argparse.Namespace) -> Tuple[bool, str]:
    if args.mode not in _possible_modes:
        return False, f"mode {args.mode} is not a valid mode."

    return True, ""


def entrypoint():
    args = parse_args()

    ret, msg = check_args(args)
    if not ret:
        print("Error: incorrect argument(s).")
        print(msg)
        sys.exit(1)

    main(args)


if __name__ == "__main__":
    entrypoint()
