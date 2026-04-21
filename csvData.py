import csv

def add_clickbait_videos(result:list, file_path:str):
    with open(file_path, 'r', newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            try:
                if float(row[1]) > 15 and float(row[2]) < 40:
                    result.append(row[0:3])
            except ValueError:
                continue

def proceed_all_files(files:list[str]) -> list[list]:
    res = []
    for f in files:
        add_clickbait_videos(res, f)
    return res