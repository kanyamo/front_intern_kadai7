from django.db import models

class Todo(models.Model):
    title = models.CharField("Todo", max_length=30, blank=False)
    contents = models.TextField("詳細", max_length=300, blank=True)
    deadline_date = models.DateField("期日(日付)")
    deadline_time = models.TimeField("期日(時間)", blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Todo"

    def __str__(self):
        return f"{self.title} - {self.deadline_date:%Y/%m/%d} {self.deadline_time:%H:%M}"
