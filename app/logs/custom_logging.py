import logging

class DatabaseHandler(logging.Handler):
    def emit(self, record):
        from .models.ModelLog import Log

        Log.objects.create(
            level=record.levelname,
            message=self.format(record)
        )
