import peewee  as pw


class core_question(pw.Model):
    id = pw.PrimaryKeyField()
    question = pw.CharField(column_name='question', max_length=256)
    category = pw.CharField(column_name="category", max_length=64)
    answer = pw.TextField(column_name="answer", null=True, default=None)
    # user = pw.ForeignKey(User, on_delete=models.CASCADE, related_name="username")
    count = pw.IntegerField(column_name="count", default=1)

    class Meta:
        database = pw.SqliteDatabase('../web/db.sqlite3')  # соединение с базой, из шаблона выше