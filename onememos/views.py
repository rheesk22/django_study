from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index( request ) :
	#return HttpResponse("Onememos~Hello, World~ ^.~")
	return render ( request, 'main.html')

def createMemo( request ) :
#	memoContent = request.GET.get('memoContent')
#
#	memoContent = request.POST['memoContent']
	memoContent = request.POST.get('memoContent')

#	if memoContent == None :
#		return HttpResponse( "Create Memo = " )
	
	article = Memo( memo_text = memoContent )
	article.save()
	
	return HttpResponse( "Create Memo = " + memoContent )
