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

def writeMemo( request ) :
	if request.method == "GET":
		return HttpResponse('GET방식 요청=> 폼페이지를 보여주세요')
#		return render( request, 'my_template.html', {'Method': 'GET 방식'})
	elif request.method == "POST":
		return HttpResponse("POST방식 요청=> DB로 넣어주세요")
#		return render( request, 'my_template.html', {'Method': 'POST 방식'})
	else :
		return HttpResponse('writePage요청??')