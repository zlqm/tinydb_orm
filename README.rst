###########
tinydb_orm
###########

ORM support for `tinydb <https://github.com/msiemens/tinydb>`_


demo
####

.. code:: python

    In [1]: import tempfile
       ...:
       ...: from tinydb import TinyDB
       ...: import tinydb_orm as models
       ...:
       ...: db_file = tempfile.NamedTemporaryFile(suffix='.json')
       ...: db = TinyDB(db_file.name)
       ...:
       ...:
       ...: class User(models.Model):
       ...:     name = models.Str()
       ...:     password = models.Str(default='')
       ...:
       ...:     class Meta:
       ...:         db = db
       ...:         table_name = 'user'
       ...:         unique_together = ['name']
       ...:
   
    In [2]: user = User.create(name='Jhon')
   
    In [3]: user
    Out[3]: <User: 1>
   
    In [4]: user.name
    Out[4]: 'Jhon'
   
    In [5]: user.password
    Out[5]: ''
   
    In [6]: user_2 = User.create(name='Kite', password='****')
   
    In [7]: user_2
    Out[7]: <User: 2>
   
    In [8]: user_2.name
    Out[8]: 'Kite'
   
    In [9]: user_2.password
    Out[9]: '****'
   
    In [10]: user_lst = User.filter(name='Jhon')
 
    In [11]: user_lst
    Out[11]: [<User: 1>]

