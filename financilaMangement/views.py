from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import CompanyList,ReportType,BalanceSheet


# Create your views here.
def index(request):
    objs = BalanceSheet.objects.all()
    exclude_fields = ('id',)
    params = [f for f in BalanceSheet._meta.fields if f.name not in exclude_fields] #obj._meta.fields获取obj所有的字段对象
    import collections
    data = collections.OrderedDict()  #建立有序的字典
    for parm in params:
        values = [getattr(obj, parm.name) for obj in objs]
        data[parm.verbose_name]=values

    context = {
        'data':data,
    }
    return render(request, 'financilaMangement/index.html', context)



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)