from django.contrib import admin
from .models import University, Candidate, Degree

# Register your models here.
admin.site.register(Candidate)
admin.site.register(University)
admin.site.register(Degree)
