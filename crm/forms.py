from django.forms import Form
from django.forms import fields


class LoginForm(Form):
    email = fields.EmailField(
        required=True,
        label='E-mail'
    )
    password = fields.CharField(
        required=True,
        label='Пароль'
    )


class PasswordResetRequestForm(Form):
    email = fields.EmailField(
        required=True,
        label='E-mail'
    )