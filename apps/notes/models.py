# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AddManager(models.Manager):
    def validate(self, postData):
        error = []
        if len(postData['notes']) < 2:
            error.append("Note must be more than 2 characters")
        if len(error) > 0:
            response = {
                'status': 'error',
                'data': error
            }
            return response
        else:
            note = Note.objects.create(content=postData['notes'])
            response = {
                'status': 'good',
                'data': note
            }
            return response

class Note(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddManager()