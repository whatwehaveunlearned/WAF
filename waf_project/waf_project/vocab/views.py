from django.shortcuts import render
from .models import English, Chinese, Spanish

import random
# Create your views here.

#Function to obtain random objects from the database it needs a model and a number of random objects when called.
def RandomVocab(model,number):
	vocab_id=[]
	vocab=[]
	for each in range (number):
		while True:	
			vocab_id.append(random.randint(1,model.objects.all().count()))
			try:
				model.objects.get(pk=vocab_id[each])
				break
			except model.DoesNotExist:
				vocab_id.append(random.randint(1,model.objects.all().count()))
		if each != 0:
			for i in range (each):
				while True:
					if vocab_id[i]==vocab_id[each]:
						vocab_id[each]=random.randint(1,model.objects.all().count())
					else:
						break
				i+=1
		vocab.append(model.objects.get(pk=vocab_id[each]))
    	return(vocab)