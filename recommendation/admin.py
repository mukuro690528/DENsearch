from django.contrib import admin
from .models import WordScore, Hospital, HospitalScore

# Register your models here.
admin.site.register(WordScore)
admin.site.register(Hospital)
admin.site.register(HospitalScore)