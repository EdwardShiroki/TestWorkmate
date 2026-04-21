import argparse
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('--files', nargs='+', type = str, help='Filenames', required=True)
parser.add_argument('--report', type=str, help='Report name', required=True)
args = parser.parse_args()
print(args.files, args.report)