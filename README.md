# Readme

Django project that can parse the table on the Methodologies page of ejproxy.com and save the results into an SQLite database. The code should be executable via a command line.


Please include instructions on how to use it. Once you’re done, please either push your code into a repository (any will work) and share the link OR zip it up and attach it with your response. Also, please try not to spend more than 1 hour on this challenge.

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
