# python-to-android-db

![Coverage](coverage.svg)
[![Build Status](https://travis-ci.org/gnud/python-to-android-db.svg?branch=master)](https://travis-ci.org/gnud/python-to-android-db)

Convert an existing Django database to Android compatible database.

# Project purpose
This project is a meta project, with one goal in mind, ships with one task that converts Django database into a plain SQL dump.
Structure and data must be created by you in a form of tasks.

## Rules:
1. Omit committing:
  - Migration files specific to mymodels.py
  - Django command tasks that use the mymodels.py


## Before start
Create mymodels.py in the databuilder app, along side the models.py file.

# Usage
## Before commit

```bash
coverage run --source='.' manage.py test
coverage-badge -f -o coverage.svg
```

## Tasks

Build the sql dump

```bash
./manage dumpsql
```

**Note**:

Before we can have a dump, we need to create tasks:
- create db structure
- which fill the database.

Samples can be found [here](docs/tasks.md).
