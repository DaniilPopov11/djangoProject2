from django.db import models

class CSV(models.Model):
    file_name =  models.FileField(upload_to='csvs')

    def __str__(self):
        return f"File id: {self.id}"
