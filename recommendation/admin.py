from django.contrib import admin
from .models import WordScore, Hospital, HospitalScore, HospitalComment, UserData, UserLike

# Register your models here.
admin.site.register(WordScore)
admin.site.register(Hospital)
admin.site.register(HospitalScore)
admin.site.register(HospitalComment)
admin.site.register(UserData)
admin.site.register(UserLike)