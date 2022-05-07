# REST API for YaMDb

Current library is REST API for YaMDb service which works with the following categories:

- Films;
- Books;
- Music;
- and other...

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

Use management command for importing data with CSV file into the SQLite data base:
```bash
python script_db.py
```

## Resources

- auth: authentication.
- users: users.
- titles: titles for reviews (particular film, book or song).
- categories: categories(types) of titles («Films», «Books», «Music»).
- genres: genres of titles. One title may be connected to many genres.
- reviews: reviews of titles. Review is connected to a particular title.
- comments: comments on titles. Comments is connected to a particular rewiew.

Каждый ресурс описан в документации: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, если это необходимо.

## Usage

Get the entire description from the link below while your project is running:

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
