from django.contrib import admin
from .models import WordScore, Hospital, HospitalScore, HospitalComment

# Register your models here.
admin.site.register(WordScore)
admin.site.register(Hospital)
admin.site.register(HospitalScore)
admin.site.register(HospitalComment)