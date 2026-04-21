def clickbait_report(rows: list[dict[str, str]]) -> list[list]:
    result = []

    for row in rows:
        ctr = float(row["ctr"])
        retention_rate = float(row["retention_rate"])

        if ctr > 15 and retention_rate < 40:
            result.append([row["title"], ctr, retention_rate])

    result.sort(key=lambda item: item[1], reverse=True)
    return result


REPORTS = {
    "clickbait": clickbait_report,
}
