from django.urls import path

from . import views

urlpatterns = [
	path( '' , views.index, name='index' ),
	path( 'createMemo/' , views.createMemo ),
    
	# 하나의 요청 --> 2개의 방식
	path('writeMemo/', views.writeMemo),
    
	# 수정 페이지 요청
	path('edit/<str:idx>',views.editPage),
    
	# 수정 결과 처리
	path('edit/update/', views.updateMemo),
    
	# 삭제 요청 및 처리
	path('delete/<str:idx>', views.deleteMemo),
]

