import pytest

from tinydb_orm import exceptions
from conftest import User


def test_single_model():
    assert User.all() == []
    user_1 = User.create(name='user_1')
    assert user_1.id == 1
    user_2 = User.create(name='user_2', password='password')
    assert user_2.id == 2

    assert len(User.all()) == User.count() == 2

    with pytest.raises(exceptions.FieldValueNotSet):
        User.create(password='test')
    with pytest.raises(exceptions.DuplicateError):
        User.create(name='user_1')
    with pytest.raises(exceptions.DuplicateError):
        user_1.name = 'user_2'
        user_1.save()
    lst = User.filter(name='user_1')
    assert len(lst) == 1
    assert lst[0].id == user_1.id
    assert User.get(name='user_1').id == user_1.id
