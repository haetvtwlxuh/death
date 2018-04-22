from django.db import models

class DeathLang(models.Model):
	title=models.CharField(max_length=100,primary_key=True,verbose_name="说的话")
	date=models.DateTimeField()
	def __str__(self):
		return self.title
class Langlist(models.Model):
	name=models.CharField(max_length=10,primary_key=True,verbose_name="语言")
	
	def __str__(self):
		return self.name
		
class LangText(models.Model):
	title=models.CharField(max_length=100,primary_key=True)
	data=models.DateTimeField()
	text=models.TextField()
	fors=models.ForeignKey(Langlist,on_delete=models.CASCADE)

	def __str__(self):
		return self.title