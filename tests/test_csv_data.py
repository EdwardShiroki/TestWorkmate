from pathlib import Path

from csvData import proceed_all_files, read_rows_from_files


def write_csv(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines), encoding="utf-8")


def test_read_rows_from_multiple_files(tmp_path: Path):
    file1 = tmp_path / "stats1.csv"
    file2 = tmp_path / "stats2.csv"

    write_csv(
        file1,
        [
            "title,ctr,retention_rate,views,likes,avg_watch_time",
            "Video A,10,90,1,1,1.0",
            "Video B,20,30,1,1,1.0",
        ],
    )
    write_csv(
        file2,
        [
            "title,ctr,retention_rate,views,likes,avg_watch_time",
            "Video C,22,35,1,1,1.0",
        ],
    )

    rows = read_rows_from_files([str(file1), str(file2)])
    assert len(rows) == 3
    assert rows[0]["title"] == "Video A"
    assert rows[2]["title"] == "Video C"


def test_proceed_all_files_builds_clickbait_report(tmp_path: Path):
    file1 = tmp_path / "stats.csv"
    write_csv(
        file1,
        [
            "title,ctr,retention_rate,views,likes,avg_watch_time",
            "Video A,10,90,1,1,1.0",
            "Video B,20,30,1,1,1.0",
            "Video C,25,35,1,1,1.0",
        ],
    )

    result = proceed_all_files([str(file1)], "clickbait")
    assert result == [
        ["Video C", 25.0, 35.0],
        ["Video B", 20.0, 30.0],
    ]
