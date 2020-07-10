from django.db import models


# Create your models here.
class University(models.Model):
    name_of_university = models.CharField(max_length=40)
    city_of_university = models.CharField(max_length=40)
    country_of_university = models.CharField(max_length=40)

    def __str__(self):
        return self.name_of_university + ', ' + self.country_of_university


class Degree(models.Model):
    DEGREE_TYPE = (
        ('Masters', 'Masters'),
        ('Bachelor', 'Bachelor'),
        ('PhD', 'PhD')
    )
    name_of_degree = models.CharField(max_length=50)
    type_of_degree = models.CharField(choices=DEGREE_TYPE, max_length=10)
    grade = models.DecimalField(decimal_places=2, max_length=5, max_digits=5, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.type_of_degree + ' in ' + self.name_of_degree


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(null=True)
    first_degree = models.OneToOneField(Degree, on_delete=models.CASCADE, related_name='first_degree', blank=True, null=True)
    second_degree = models.OneToOneField(Degree, on_delete=models.CASCADE, related_name='second_degree', null=True, blank=True)
    third_degree = models.OneToOneField(Degree, on_delete=models.CASCADE, related_name='third_degree', blank=True, null=True)

    def __str__(self):
        return self.first_name
