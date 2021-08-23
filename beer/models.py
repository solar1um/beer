from django.db import models


class Generation(models.Model):
    name = models.CharField('Будьте добры ввести ваше имя. (rus/eng) результаты могут разниться.', max_length=12)

    def __self__(self):
        return self.name
