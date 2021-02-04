from datetime import datetime

from peewee import *
import sqlite3

# db = SqliteDatabase('people.db')
mysql_db = MySQLDatabase('test', user='root', password='12345',
                         host='localhost', port=3306)
import MySQLdb

BOOK_STATUS = (
    (1, 'New'),
    (2, 'Used'),
    (3, 'Damaged'),
)


class Publish(Model):
    name = CharField(unique=True)
    location = CharField(null=True)

    class Meta:
        database = mysql_db


class Author(Model):
    name = CharField(unique=True)
    location = CharField(null=True)

    class Meta:
        database = mysql_db


class Category(Model):
    category_name = CharField(unique=True)
    parent_category = IntegerField()

    class Meta:
        database = mysql_db


class Books(Model):
    Title = CharField(unique=True)
    description = TextField(null=True)
    category = ForeignKeyField(Category, backref='category', null=True)
    code = CharField(null=True)
    barcode = CharField()
    # parts
    part_order = IntegerField(null=True)
    price = DecimalField()
    publisher = ForeignKeyField(Publish, backref='publish', null=True)
    author = ForeignKeyField(Author, backref='author', null=True)
    image = CharField(null=True)
    status = CharField(choices=BOOK_STATUS)
    date = DateTimeField(default=datetime.now)

    class Meta:
        database = mysql_db


class Clients(Model):
    name = CharField()
    phone = CharField(null=True)
    mail = CharField(null=True, unique=True)
    national_id = IntegerField(null=True, unique=True)
    date = DateTimeField(default=datetime.now)

    class Meta:
        database = mysql_db


class Employee(Model):
    name = CharField()
    phone = CharField(null=True)
    mail = CharField(null=True, unique=True)
    national_id = IntegerField(null=True, unique=True)
    periorty = IntegerField(null=True)
    date = DateTimeField(default=datetime.now)

    class Meta:
        database = mysql_db


class Brunch(Model):
    name = CharField()
    code = CharField(null=True, unique=True)
    location = CharField(null=True)

    class Meta:
        database = mysql_db


PRODREES_TYPE = (
    (1, 'rent'),
    (2, 'reteive'),

)


class Daily_Movement(Model):
    book = ForeignKeyField(Books, backref='book')
    client = ForeignKeyField(Clients, backref='clients',null=True)
    type_ = CharField(choices=PRODREES_TYPE)
    brunch = ForeignKeyField(Brunch, backref='Brunch', null=True)
    date = DateTimeField(default=datetime.now)
    book_from = DateField(null=True)
    book_to = DateField(null=True)
    employee = ForeignKeyField(Employee, backref='Employee', null=True)

    class Meta:
        database = mysql_db


ACTIONS_TYPE = (
    (1, 'Login'),
    (2, 'Update'),
    (3, 'Create'),
    (4, 'Delete'),

)
TABLE_TYPE = (
    (1, 'Books'),
    (2, 'Clients'),
    (3, 'Employee'),
    (4, 'Category'),
    (5, 'Brunch'),
    (6, 'Daily Movmente'),
    (7, 'Publisher'),
    (8, 'Author'),

)


class History(Model):
    employee = ForeignKeyField(Employee, backref='Employee')
    action = CharField(choices=ACTIONS_TYPE)
    table = CharField(choices=TABLE_TYPE)
    date = DateTimeField(default=datetime.now)
    brunch = ForeignKeyField(Brunch, backref='Brunch', null=True)

    class Meta:
        database = mysql_db


mysql_db.connect()
mysql_db.create_tables([Books, Author, Publish, History, Daily_Movement, Brunch, Category, Employee, Clients])
