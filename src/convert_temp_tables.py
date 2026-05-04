from pathlib import Path
from common import apply_common_rules

def convert(sql):
    sql = apply_common_rules(sql)
    sql = sql.replace("CREATE TABLE #", "CREATE GLOBAL TEMPORARY TABLE ")
    sql += "\nON COMMIT PRESERVE ROWS;"
    return sql

def run():
    for f in Path("input/temp_tables").glob("*.sql"):
        (f.parent / (f.stem + "_ora.sql")) \
            .write_text(convert(f.read_text()), encoding="utf-8")

if __name__ == "__main__":
    run()