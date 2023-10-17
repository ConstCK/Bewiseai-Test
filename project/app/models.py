from django.db import models


class Quiz(models.Model):
    question_id = models.PositiveIntegerField(unique=True, verbose_name="Id вопроса")
    question = models.CharField(max_length=1024, verbose_name="Вопрос")
    answer = models.CharField(max_length=512, verbose_name="Ответ")
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Вопрос № {self.id}"

    class Meta:
        verbose_name = "Викторина"
        verbose_name_plural = "Викторины"
