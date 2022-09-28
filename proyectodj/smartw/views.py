
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from smartw.forms import SmartbandForm  
from smartw.models import Smartband  
  
def smt(request):  
    if request.method == "POST":  
        form = SmartbandForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = SmartbandForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    smartw = Smartband.objects.all()  
    return render(request,"show.html",{'smartband':smartw})  
def edit(request, pk):  
    smartw = Smartband.objects.get(pk=pk)  
    return render(request,'edit.html', {'smartband':smartw})  
def update(request, pk):  
    smartw = Smartband.objects.get(pk=pk) 
    form = SmartbandForm(request.POST, instance = smartw)   
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'smartband': smartw})  
def destroy(request,pk):  
    smartw = Smartband.objects.filter(pk=pk)  
    smartw.delete()  
    return redirect("/show")  
