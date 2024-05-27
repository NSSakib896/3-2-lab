from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())


def members(request):
    text = "Add"
    template = loader.get_template('all_members.html')
    member_list = Member.objects.all().values()
    context = {
        'member_list': member_list,
        "button_text": text,
    }
    return HttpResponse(template.render(context, request))