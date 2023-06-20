from django.db import models

# Create your models here.
#1) 데이터 모델
# idx				x
# memo_text			o
# published_date	o
# modified_times	o
# modified_date		o
# last_value		o

class Memo( models.Model ):
	memo_text = models.CharField( max_length=200 )
	published_date = models.DateTimeField( auto_now_add=True )
	
	def __str__(self):
		return self.memo_text
#	modified_times = models.NumericField()
#	modified_date = models.DateTimeField()
#	last_value = models.CharField(max_length=200)

# 2) 작성 후 --> 반영을 위해서 --> 어디에? --> Admin 사이트에 반영 --> admin.py 열고 추가 작성.

