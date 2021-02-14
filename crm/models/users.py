from django.db import models
from django.contrib.auth.models import User

__all__ = ['UserProfile']


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='profile', \
                             on_delete=models.CASCADE, null=True, blank=False)
    phone = models.CharField(null=False, blank=False, verbose_name='Телефон', max_length=16)


    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['user__last_name']

    def __str__(self):
        user_name_list = []
        if self.user.first_name != '':
            user_name_list.append(self.user.first_name)
        if self.user.last_name != '':
            user_name_list.append(self.user.last_name)
        return ' '.join(user_name_list)

