import argparse
from pathlib import Path

from csvData import proceed_all_files
from prettyOut import pretty_out
from reports import REPORTS


def existing_file(path: str) -> str:
    if not Path(path).is_file():
        raise argparse.ArgumentTypeError(f"File not found: {path}")
    return path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="YouTube metrics reports")
    parser.add_argument(
        "--files",
        nargs="+",
        type=existing_file,
        help="CSV file paths",
        required=True,
    )
    parser.add_argument(
        "--report",
        type=str,
        choices=sorted(REPORTS.keys()),
        help="Report name",
        required=True,
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    result = proceed_all_files(args.files, args.report)
    pretty_out(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
