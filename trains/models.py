from django.db import models
from django.forms import ValidationError

from cities.models import City


class Train(models.Model):
    '''trains_train'''
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название поезда')
    travel_time = models.PositiveSmallIntegerField(
        verbose_name='Время в пути'
    )
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Из какого города'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                  related_name='to_city_set',
                                  verbose_name='В какой город'
                                  )
    
    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city}'
    
    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
    
    
    def clean(self) -> None:
        if self.from_city == self.to_city:
            raise ValidationError('Изменитьгород прибытия')
        qs = Train.objects.filter(from_city=self.from_city, 
                                  to_city=self.to_city, 
                                  travel_time=self.travel_time
                                  ).exclude(pk=self.pk)
        
        if qs.exists():
            raise ValidationError('Измените время в пути')
        
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)