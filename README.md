# python-to-android-db

![Coverage](coverage.svg)
[![Build Status](https://travis-ci.org/gnud/python-to-android-db.svg?branch=master)](https://travis-ci.org/gnud/python-to-android-db)


# Project purpose
This project aim is to generate Android compatible SQL dumps using the power of Django's ORM

## Usage

Build the sql dump

```bash
./manage toandroid
```

## Testing

```bash
./manage test
```

## Coverage

```bash
coverage run --source='.' manage.py tests
```

```bash
coverage run --source='.' manage.py toandroid
```


**Note**:
Samples can be found [here](docs/models.md).


# Development
## Before commit

```bash
coverage run --source='.' manage.py test
coverage-badge -f -o coverage.svg
```
