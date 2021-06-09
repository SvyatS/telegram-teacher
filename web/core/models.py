from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """Модель вопроса"""

    _choose = (
        ("Занятия", "Занятия"),
        ("Работа Вуза", "Работа Вуза"),
        ("Преподаватели", "Преподаватели"),
        ("Другой вопрос", "Другой вопрос")
    )

    question = models.CharField("Вопрос", max_length=256)
    category = models.CharField("Категория", choices=_choose, default="Другой вопрос", max_length=64)
    answer = models.TextField("Ответ", null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernames", null=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.question[:40])
