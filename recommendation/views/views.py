from django.shortcuts import render
from recommendation.models import HospitalComment

# Create your views here.

def survey(request):
    return render(request, 'survey.html')

def detail(request, id):
    comment = HospitalComment.objects.filter(hospital_id=id)
    return render(request, 'detail.html', {'comment': comment})