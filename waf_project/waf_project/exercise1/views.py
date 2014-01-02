from django.shortcuts import render
from django.views.generic import ListView

from vocab.models import English
from vocab.views import RandomVocab

import random
# Create your views here.

#Exercise 1 Handler
#def exercise1_handler(request):

#Exercise 1 Viewer
def exercise1_viewer(request): 
	model=English # Here we will specify the vocab to be used for the exercise
	vocab=RandomVocab(English,2)
	value=int(random.getrandbits(1))#create random value between 0 and 1 to change the audio file
	if value==0:
		audio=vocab[0].sound
	else:
		audio=vocab[1].sound
	import pdb; pdb.set_trace()
	#return render_to_response('main/exercise3.html', {'vocab':vocab,'sound':sound},context_instance=RequestContext(request))