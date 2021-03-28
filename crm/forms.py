from django.forms import Form
from django.forms import fields


class LoginForm(Form):
    email = fields.CharField(
        required=True,
        label='Имя пользователя'
    )
    password = fields.CharField(
        required=True,
        label='Пароль'
    )


class PasswordResetRequestForm(Form):
    email = fields.CharField(
        required=True,
        label='E-mail'
    )