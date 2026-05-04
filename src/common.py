import re

DATA_TYPE_MAP = {
    r"\bINT\b": "NUMBER(10)",
    r"\bBIGINT\b": "NUMBER(19)",
    r"\bSMALLINT\b": "NUMBER(5)",
    r"\bTINYINT\b": "NUMBER(3)",
    r"\bVARCHAR\b": "VARCHAR2",
    r"\bCHAR\b": "CHAR",
    r"\bDATETIME\b": "TIMESTAMP",
    r"\bDATE\b": "DATE",
    r"\bBIT\b": "NUMBER(1)",
    r"\bTEXT\b": "CLOB",
    r"\bIMAGE\b": "BLOB", 
    r"\bNUMERIC\b": "NUMBER",
    r"\bDECIMAL\b": "NUMBER"
}

def apply_common_rules(sql: str) -> str:
    for s, o in DATA_TYPE_MAP.items():
        sql = re.sub(s, o, sql, flags=re.I)
    sql = re.sub(r"^\s*GO\s*$", "", sql, flags=re.I | re.M)
    return sql.strip()
