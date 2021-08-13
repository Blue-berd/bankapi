from django.shortcuts import render

# Create your views here.
from .models import Branches, Banks
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BranchSerializer

from .my_pagination import MyLimitOffsetPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import json
from rest_framework_extensions.mixins import PaginateByMaxMixin
from django.views.decorators.csrf import csrf_protect
# Create your views here.


class BankViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    search_fields = ['^ifsc','^city','^state']
    queryset = Branches.objects.filter(ifsc__startswith='')
    serializer_class = BranchSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    
    filterset_fields =['ifsc']
    ordering_fields = ['ifsc']

def home(request):
    
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html')

@csrf_protect
def search_ifsc(request):
    if request.is_ajax():
        q = request.GET.get('q', '').capitalize()
        search_qs = Branches.objects.filter(ifsc__startswith=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.ifsc)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)