from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Abstract class for all Vocab tables
class Vocab(models.Model):


	image = models.ImageField(upload_to='images',blank=True)
	sound = models.FileField(upload_to='sounds',blank=True)
	definition = models.TextField(blank=True)
	tags = models.CharField(max_length=100,blank=True)
	created = models.DateTimeField(auto_now_add=True,blank=True)
	modified = models.DateTimeField(auto_now=True,blank=True)

	class Meta:
		abstract = True
		ordering =['created']

	def __unicode__(self):
		return u'%s' % (self.word)

#Models for the languages
class Languages(models.Model):
	language = models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s' % (self.language)

#English Class
class English(Vocab):
	word = models.CharField(max_length=100)
	translation1 = models.ForeignKey('Chinese',related_name='englishtrans1',null=True, blank=True,default='no')
	translation2 = models.ForeignKey('Chinese',related_name='englishtrans2',null=True, blank=True,default='no')
	translation3 = models.ForeignKey('Spanish',related_name='englishtrans3',null=True, blank=True,default='no')
	translation4 = models.ForeignKey('Spanish',related_name='englishtrans4',null=True, blank=True,default='no')
	translation5 = models.ForeignKey('English',related_name='englishtrans5',null=True, blank=True,default='no')
	translation6 = models.ForeignKey('English',related_name='englishtrans6',null=True, blank=True,default='no')
#Chinese Class
class Chinese(Vocab):
	word = models.CharField(max_length=100)
	symbol = models.CharField(max_length=20) #HOW TO PUT CHINESE CHARACTERS??
	translation1 = models.ForeignKey('Chinese',related_name='chinesetrans1',null=True, blank=True,default='no')
	translation2 = models.ForeignKey('Chinese',related_name='chinesetrans2',null=True, blank=True,default='no')
	translation3 = models.ForeignKey('Spanish',related_name='chinesetrans3',null=True, blank=True,default='no')
	translation4 = models.ForeignKey('Spanish',related_name='chinesetrans4',null=True, blank=True,default='no')
	translation5 = models.ForeignKey('English',related_name='chinesetrans5',null=True, blank=True,default='no')
	translation6 = models.ForeignKey('English',related_name='chinesetrans6',null=True, blank=True,default='no')

#Spanish Class
class Spanish(Vocab):
	word = models.CharField(max_length=100)
	translation1 = models.ForeignKey('Chinese',related_name='spanishtrans1',null=True, blank=True,default='no')
	translation2 = models.ForeignKey('Chinese',related_name='spanishtrans2',null=True, blank=True,default='no')
	translation3 = models.ForeignKey('Spanish',related_name='spanishtrans3',null=True, blank=True,default='no')
	translation4 = models.ForeignKey('Spanish',related_name='spanishtrans4',null=True, blank=True,default='no')
	translation5 = models.ForeignKey('English',related_name='spanishtrans5',null=True, blank=True,default='no')
	translation6 = models.ForeignKey('English',related_name='spanishtrans6',null=True, blank=True,default='no')
####################################################################################

#Models for the user
class WafUser(User):
	firstLanguage = models.ForeignKey('Languages',related_name='firstLanguage')
	secondLanguage = models.ForeignKey('Languages',related_name='secondLanguage',blank=True)
	thirdLanguage = models.ForeignKey('Languages',related_name='thirdLanguage',blank=True)



