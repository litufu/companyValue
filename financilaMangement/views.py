from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyList,ReportType,BalanceSheet

# Create your views here.
def index(request):
    rprtyp_objects = ReportType.objects.all()
    return HttpResponse("报表类型编码：{};报表类型名称：{}".format(rprtyp_objects[0].type,rprtyp_objects[0].name))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)