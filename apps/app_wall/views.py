# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Comment
from django.core.urlresolvers import reverse

def wallpage(request):
    #Message.objects.all().delete()
    if request.method == "POST":
        if request.POST['action'] == "postmsg":
            context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
                }
            result = User.objects.addmsgs(request.POST,context)
            print request.method
            if not result['status']:
                for error in result['errors']:
                    messages.error(request,error)
                    return redirect(reverse('my_wall'))
            else: 
                messages.success(request,"Successful")
                return redirect(reverse('my_wall'))
        else:
            context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
                }
            result = User.objects.addcomments(request.POST,context)
            print request.method
            if not result['status']:
                for error in result['errors']:
                    messages.error(request,error)
                    return redirect(reverse('my_wall'))
            else: 
                messages.success(request,"Successful")
                return redirect(reverse('my_wall'))

            print "DIDNT ENTER"
    else:
            print "ENTERED GET"
            context = {
                    'blog' :  Message.objects.order_by('-id'),
                    "name": request.session['first_name'],
                    "usercomments" : Comment.objects.order_by('-id')
                }
    return render(request,'app_wall/wall.html', context)




   




