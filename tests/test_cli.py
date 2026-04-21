from pathlib import Path

import pytest

from main import main


def write_csv(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines), encoding="utf-8")


def test_cli_success(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    file_path = tmp_path / "stats.csv"
    write_csv(
        file_path,
        [
            "title,ctr,retention_rate,views,likes,avg_watch_time",
            "Video A,18,35,1,1,1.0",
            "Video B,24,20,1,1,1.0",
            "Video C,10,30,1,1,1.0",
        ],
    )

    code = main(["--files", str(file_path), "--report", "clickbait"])
    captured = capsys.readouterr()

    assert code == 0
    assert "title" in captured.out
    assert "retention_rate" in captured.out
    assert "Video C" not in captured.out
    assert captured.out.index("Video B") < captured.out.index("Video A")


def test_cli_unknown_report(tmp_path: Path):
    file_path = tmp_path / "stats.csv"
    write_csv(
        file_path,
        [
            "title,ctr,retention_rate,views,likes,avg_watch_time",
            "Video A,18,35,1,1,1.0",
        ],
    )

    with pytest.raises(SystemExit) as error:
        main(["--files", str(file_path), "--report", "unknown"])

    assert error.value.code == 2


def test_cli_missing_file():
    with pytest.raises(SystemExit) as error:
        main(["--files", "missing.csv", "--report", "clickbait"])

    assert error.value.code == 2
