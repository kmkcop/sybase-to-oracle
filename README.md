---
## Introduction
Name: Sybase to Oracle Migration Toolkit

Description: The tool looks Sybase DDL files with ".sql" extension under the "input" folder. For each file, it generates corresponding Oracle DDL file with "_ora.sql" suffix in the same location as the source file. The input folder is subdivided into object types such as tables, views etc.

---
## Usage

# Single command to convert all object files:
python src\convert_all.py


# To convert specific object files, example tables, views etc:

# tables
python src\convert_tables.py

# temp_tables
python src\convert_temp_tables.py

# views
python src\convert_views.py

# mviews
python src\convert_mviews.py

# triggers
python src\convert_triggers.py

# functions
python src\convert_functions.py

# procedures
python src\convert_procedures.py
