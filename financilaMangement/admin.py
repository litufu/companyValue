from django.contrib import admin

# Register your models here.
from .models import CompanyList,ReportType,BalanceSheet

admin.site.register(CompanyList)
admin.site.register(ReportType)
admin.site.register(BalanceSheet)
