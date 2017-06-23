# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class Post_comments(models.Manager):  
    def addmsgs(request,postData,sessiondata):
        print " In addmsgs %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if len(postData['messages'])<1:
            print "In validation "
            result['status'] = False
            results['errors'].append("Please enter a valid post")
            return results
        user1 = User.objects.get(id = sessiondata['id'])
        print "Successfully done@@@@@@@@@@@@@@"
        if postData['messages']:
            Message.objects.create(message=postData['messages'],user1 = user1)
            results['status'] = True
            print "Successfully done!!!!!!!!!"
        print "Not Succesful*************"
        return results

    def addcomments(request,postData,sessiondata):
        print " In addmsgs %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if len(postData['commenting'])<1:
            print "In validation "
            result['status'] = False
            results['errors'].append("Please enter a valid post")
            return results
        user = User.objects.get(id = sessiondata['id'])
        #print postData
        print postData['msgid']
        message = Message.objects.get(id = postData['msgid'])
      
        if postData['commenting']:
            Comment.objects.create(comment=postData['commenting'],user = user, message = message)
            results['status'] = True
            print "Successfully done!!!!!!!!!"
        print "Not Succesful*************"
        return results
        

class Message(models.Model):
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user1 = models.ForeignKey('app_login.User', related_name="users1")
    #msg
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey('app_login.User', related_name="users")
    message = models.ForeignKey(Message, related_name="msg")


 
    
