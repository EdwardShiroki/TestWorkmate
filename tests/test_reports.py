from reports import clickbait_report


def test_clickbait_report_filters_and_sorts_by_ctr_desc():
    rows = [
        {"title": "A", "ctr": "18", "retention_rate": "35"},
        {"title": "B", "ctr": "25", "retention_rate": "22"},
        {"title": "C", "ctr": "14", "retention_rate": "20"},
        {"title": "D", "ctr": "19", "retention_rate": "45"},
        {"title": "E", "ctr": "21", "retention_rate": "38"},
    ]

    result = clickbait_report(rows)

    assert result == [
        ["B", 25.0, 22.0],
        ["E", 21.0, 38.0],
        ["A", 18.0, 35.0],
    ]
