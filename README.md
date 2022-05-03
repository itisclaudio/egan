# Readme

Django project that parses the table on the Methodologies page of ejproxy.com and saves the results into an SQLite database. The is executable via a command line.

## Instructions

Run django shell and import the function “parse” or "parse2"

```bash
(venv) PS C:\egan\egan> python manage.py shell
>>> from parse import parse
>>> from parse import parse2
```
Using django commands:

```bash
(venv) PS C:\dev\egan\parse> python manage.py parse3
```
Runserver and the “Methodologies” table will be populated with the data.
