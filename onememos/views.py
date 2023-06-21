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

def editPage( request, idx ) :
#	return HttpResponse('수정페이지 = ' + idx)

	article = Memo.objects.get(id=idx)
	data = {'article': article}

	return render( request, 'edit.html', data )

def updateMemo( request ) :
	idx = request.POST['idx']
	memoContent = request.POST['memoContent']
#	return HttpResponse( idx + ' ' + memoContent )
#	return HttpResponse( f'현재 넘어온 idx는 {idx}번이고, 수정된 memoContent는 {memoContent} 입니다.' )


#	db update 처리
	db_article = Memo.objects.get(id=idx)
	db_article.memo_text = memoContent
	db_article.save()

	return HttpResponseRedirect( reverse('index') )

def deleteMemo( request, idx ) :
	db_article = Memo.objects.get(id=idx)
	db_article.delete()

	return HttpResponseRedirect( reverse('index') )