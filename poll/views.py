from django.shortcuts import render,redirect
from .forms import CreatePollform
from .models import polldata
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth,User
from datetime import datetime

# Create your views here.
def home(request):
    
    data = polldata.objects.all()
    context={
        "data":data
    }
    return render(request, 'templates/home.html',context)

def create(request):
    poll=polldata.objects.all()
    if request.method=="POST":
        form=CreatePollform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form = CreatePollform()
        
    context={
        "poll":poll,
        "form":form
    }
   
    return render(request, 'templates/create.html',context)

def vote(request,pk):
    poll = polldata.objects.get(id=pk)
    options = polldata.objects.all()
    
    if request.method=="POST":
        selectedoption=request.POST['choice']
        if selectedoption=="option1":
            poll.option_one_count+=1
            poll.users+=" "+str(request.user.id)
        elif selectedoption=="option2":
            poll.option_two_count+=1
            poll.users+=" "+str(request.user.id)
        elif selectedoption=="option3":
            poll.option_three_count+=1
            poll.users+=" "+str(request.user.id)
        elif selectedoption=="option4":
            poll.option_four_count+=1
            poll.users+=" "+str(request.user.id)
            
        else:
            print('error')
    
    else:
        print('error')
    poll.save()
    
    
    poll.total=poll.option_one_count+poll.option_two_count+poll.option_three_count
    context={
        "poll":poll,
        "options":options,
        
        
    }
   
    return render(request, 'templates/vote.html',context)




def userprofile(request):
    poll = polldata.objects.all()
    context ={
        "poll":poll
    }
    return render(request, 'templates/profile.html',context)

def delete(request,id):
    poll=polldata.objects.get(id=id)
    poll.delete()
    return redirect('/')