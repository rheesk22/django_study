from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index( request ) :
#	return HttpResponse("Onememos~Hello, World~ ^.~")

#	return render ( request, 'main.html')
	
	lists = Memo.objects.all()
	data = { 'lists' : lists }
	
	return render ( request, 'main.html', data )
	

def createMemo( request ) :
#	memoContent = request.GET.get('memoContent')
#
#	memoContent = request.POST['memoContent']
	memoContent = request.POST.get('memoContent')

#	if memoContent == None :
#		return HttpResponse( "Create Memo = " )

#	db save	
#	article = Memo( memo_text = memoContent )
#	article.save()
	
#	return HttpResponse( "Create Memo = " + memoContent )

	return HttpResponseRedirect( reverse( 'index' ) )
