from django.db import models
from users.models import User
from django.db import models
from django.core.validators import RegexValidator


class Landlord(models.Model):
    phone_regex = RegexValidator(
        regex=r'^0[789][0]{9}$',
        message='Phone number must start in this format: "070, o71, 080, 081, 090, 091". 11 digits allowed.'
    )
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex],max_length=11)

    def __str__(self):
        return f"<landlord email={self.user.email}>"

