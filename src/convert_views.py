from pathlib import Path
from common import apply_common_rules

def run():
    for f in Path("input/views").glob("*.sql"):
        sql = apply_common_rules(f.read_text())
        sql = sql.replace("CREATE VIEW", "CREATE OR REPLACE VIEW")
        (f.parent / (f.stem + "_ora.sql")) \
            .write_text(sql + ";", encoding="utf-8")

if __name__ == "__main__":
    run()