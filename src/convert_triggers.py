from pathlib import Path
from common import apply_common_rules

def convert(sql):
    sql = apply_common_rules(sql)
    sql = sql.replace("FOR INSERT", "BEFORE INSERT")
    sql = sql.replace("@", "v_")
    return "CREATE OR REPLACE " + sql + "\n/"

def run():
    for f in Path("input/triggers").glob("*.sql"):
        (f.parent / (f.stem + "_ora.sql")) \
            .write_text(convert(f.read_text()), encoding="utf-8")

if __name__ == "__main__":
    run()
