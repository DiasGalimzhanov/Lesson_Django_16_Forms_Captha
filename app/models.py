from django.db import models


class Lego(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    size = models.PositiveIntegerField(verbose_name='размер')

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return self.name
    

class Figure(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    lego = models.ForeignKey(Lego, on_delete=models.CASCADE, verbose_name='деталь')

    class Meta:
        verbose_name = 'Фигура'
        verbose_name_plural = 'Фигуры'

    def __str__(self):
        return self.name
    
# class DateHandler(models.Model):
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     class Meta:
#         abstract = True