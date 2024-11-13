from . models import User, AbstractUser
user = User.objects.get(email="fareedsayed@gmail.com")
print(user.email, user.check_password("12345"))
