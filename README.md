# REST API for YaMDb

Current library is REST API for YaMDb service which works with the following categories:

- Films;
- Books;
- Music.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Make all necessary migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Use manegament command for importing data with CSV file into the SQLite data base:
```bash
python script_db.py
```

## Usage

Get the entire description from the like while you project is running:

```python
http://127.0.0.1:8000/redoc/
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors
> [Alex](https://github.com/learies)

>[Sergey](https://github.com/SergoSolo)

> [Artur](https://github.com/Archy-A)

## License
Free
