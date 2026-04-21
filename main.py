import argparse

from csvData import proceed_all_files
from prettyOut import pretty_out

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('--files', nargs='+', type = str, help='Filenames', required=True)
parser.add_argument('--report', type=str, help='Report name', required=True)
args = parser.parse_args()


res = proceed_all_files(args.files)
pretty_out(res)