from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.db import connection

from django.core import serializers

from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):

    cursor = connection.cursor()
    cursor.execute("select  staff.name , job.name, count(*)     from core_staff as staff, core_job as job, core_record as record where record.staff_id = staff.id  and record.job_id = job.id group by job_id , staff_id ",None)
    record_list = cursor.fetchall()

    print(record_list)
    data = {'result': record_list , 'code':"正常" }

    #json_data = serializers.serialize("json", data, ensure_ascii=False)
    #,content_type='application/json, charset=utf-8'

    
    return JsonResponse(data , json_dumps_params={'ensure_ascii':False })



def show(request):

    
    cursor = connection.cursor()
    cursor.execute("select  staff.name , job.name, count(*)     from core_staff as staff, core_job as job, core_record as record where record.staff_id = staff.id  and record.job_id = job.id group by job_id , staff_id ",None)
    record_list = cursor.fetchall()

    print(record_list)
    data = {'result': record_list , 'code':"正常" }

    #json_data = serializers.serialize("json", data, ensure_ascii=False)
    #,content_type='application/json, charset=utf-8'

    template = loader.get_template('show.html')
    
    context = {
        'latest_question_list': 12,
    }
    return HttpResponse(template.render(context, request))

