from django.db import models

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = True
        db_table = "app_logs"