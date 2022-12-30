from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Story
from .forms import StoryForm

# Create your views here.
def index(request):
    story=Story.objects.all()
    context={
        'story_list':story
    }
    return render(request,'index.html',context)
def detail(request,story_id):
    story=Story.objects.get(id=story_id)
    return render(request,"detail.html",{'story':story})

def add_story(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        story=Story(name=name,desc=desc,year=year,img=img)
        story.save()

    return render(request,'add.html')

def update(request,id):
    story=Story.objects.get(id=id)
    form=StoryForm(request.POST or None,request.FILES,instance=story)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})
def delete(request,id):
    if request.method=='POST':
        story=Story.objects.get(id=id)
        story.delete()
        return redirect('/')
    return render(request,'delete.html')


