from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from django.views.decorators.http import etag

from .serializers import NotesSerializers
from .models import Notes
# from rest_framework_extensions.etag.decorators import etag
from rest_framework_extensions.mixins import ( CacheResponseAndETAGMixin )
import uuid

def etag_note(request, id):
    if id:
        try:
            return "%s-%s" % (str(int(Notes.objects.get(id=id).modified_date.timestamp())), str(Notes.objects.get(id=id).id))
        except Notes.DoesNotExist:
            pass
    else:
        return None


class DocumentViewSetMixin(viewsets.ModelViewSet):
    lookup_field = 'id'

    @method_decorator(etag(etag_func=etag_note))
    def retrieve(self, request, *args, **kwargs):
        return super(DocumentViewSetMixin, self).retrieve(request, *args, **kwargs)

class NotesViewSet(DocumentViewSetMixin):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers
