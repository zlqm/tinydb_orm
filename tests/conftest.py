from tinydb import TinyDB
import tinydb_orm as models

db = TinyDB('/tmp/test.json')


def truncate_db(db):
    for table_name in db.tables():
        db.table(table_name).truncate()


truncate_db(db)


class User(models.Model):
    name = models.Str()
    password = models.Str(default='')

    class Meta:
        db = db
        table_name = 'user'
        unique_together = ['name']


'''
class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.Str()
    content = models.Str()

    class Meta:
        db = db
        table_name = 'article'
'''
