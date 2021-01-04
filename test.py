import re

from tinydb import TinyDB
import tinydb_orm
from tinydb_orm.exceptions import DuplicateError

import pytest

db = TinyDB('/tmp/test.json')

for table in db.tables():
    db.table(table).truncate()


class User(tinydb_orm.Model):
    name = tinydb_orm.Str()
    password = tinydb_orm.Str(default='')

    class Meta:
        db = db
        table_name = 'user'
        unique_together = ['name']


class Article(tinydb_orm.Model):
    author_id = tinydb_orm.Int()
    title = tinydb_orm.Str()
    content = tinydb_orm.Str()

    class Meta:
        db = db
        table_name = 'article'
        unique_together = ['author_id', 'title']

def test_main():
    # test create
    user = User.create(name='123')
    assert user.id == 1
    user = User.create(name='234')
    assert user.id == 2
    with pytest.raises(DuplicateError):
        User.create(name='234')
    # test query
    user = User.get(name='123')
    assert user.id == 1
    user = User.get(name='234')
    assert user.id == 2
    # test default value
    with pytest.raises(ValueError):
        Article.create(author_id=user.id, title='test article')
