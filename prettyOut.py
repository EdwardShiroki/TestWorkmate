import tabulate

def pretty_out(table: list[list]) -> None:
    print(tabulate.tabulate(table, headers=["title", "ctr", "retention_rate"], tablefmt="psql"))
