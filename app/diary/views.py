from django.shortcuts import render, redirect  
from diary.forms import DiaryForm  
from diary.models import Diary  
# Create your views here.  
def diary(request):  
    if request.method == "POST":  
        form = DiaryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DiaryForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    diaries = Diary.objects.all()  
    return render(request,"show.html",{'diaries':diaries})  
def edit(request, did):  
    diary = Diary.objects.get(did=did)  
    return render(request,'edit.html', {'diary':diary})  
def update(request, did):  
    diary = Diary.objects.get(did=did)  
    form = DiaryForm(request.POST, instance = diary)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'diary': diary})  
def destroy(request, did):  
    diary = Diary.objects.get(did=did)  
    diary.delete()  
    return redirect("/show")  