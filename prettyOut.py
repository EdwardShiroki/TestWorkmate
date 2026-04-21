import tabulate

def pretty_out(table:list[list]):
    table = sorted(table, key=lambda x: float(x[2]))
    print(tabulate.tabulate(table, headers=['title', 'ctr', 'retention_rate'], tablefmt='psql'))