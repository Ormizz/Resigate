from django.db import models

class AuthorizationStatus(models.Model):
    label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class AuthorizationType(models.Model):
    label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class AccessAuthorization(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField()
    status = models.ForeignKey(AuthorizationStatus, on_delete=models.CASCADE)
    authorization_type = models.ForeignKey(AuthorizationType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Authorization ID: {self.pk}"

class Brand(models.Model):
    label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class Country(models.Model):
    code = models.CharField(max_length=10)
    label = models.CharField(max_length=255)
    long_label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class City(models.Model):
    long_label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=255)
    active = models.BooleanField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.long_label

class ResidentialDistrict(models.Model):
    long_label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    active = models.BooleanField()

    def __str__(self):
        return self.long_label

class UserRole(models.Model):
    label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class Sex(models.TextChoices):
    FEMALE = 'FEMALE'
    MALE = 'MALE'

class ResiUser(models.Model):
    matricule = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    birth_date = models.DateField()
    sex = models.CharField(max_length=6, choices=Sex.choices)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=10)
    profession = models.CharField(max_length=255)
    active = models.BooleanField()
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    number_plate = models.CharField(max_length=10)
    car_model = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_registration_document = models.TextField()
    active = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.number_plate

class AccessStatus(models.Model):
    label = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.label

class AccessHistory(models.Model):
    access_date = models.DateTimeField()
    user = models.ForeignKey(ResiUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    access_status = models.ForeignKey(AccessStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Access ID: {self.pk}"
