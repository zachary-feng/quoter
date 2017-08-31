from django.db import models

class Quote(models.Model):

    quote = models.CharField(max_length=3000)
    person = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"' + self.quote + '"' + ' by ' + self.person