from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.urls import reverse

from .models import Blocktable
from .form import Blockform

def index(request):
    listBlock = Blocktable.objects.order_by('-date')
    return render(request,'index.html',{"listblock" : listBlock})


def showBlock(request, blockid):
    oneBlock = get_object_or_404(Blocktable, id=blockid)
    print(oneBlock)
    return render(request,'detailOneBlock.html',{"blockone" : oneBlock})


def createBlockform(request):
    return render(request,'createBlockForm.html')

def creteBlock(request):
    if request.method  == "POST" :
        form = Blockform(request.POST)
        if form.is_valid():
            obj = Blocktable()
            obj.title = form.cleaned_data['title']
            obj.content = form.cleaned_data['content']
            obj.authId = 1
            obj.save()
            return HttpResponseRedirect(reverse('blockapp:oneblock',args=(obj.id,)))
        return Http404("Error")
    else:        
        return Http404("Error")
    

def updateBlock(request, blockid):
    return HttpResponse("updateBlock %s" % blockid)


def delete(request, blockid):
    block = get_object_or_404(Blocktable, id=blockid)
    block.delete()
    return HttpResponseRedirect(reverse('blockapp:index'))