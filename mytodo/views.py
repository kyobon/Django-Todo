from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Do,Did
from .forms import CreateForm
from django.core.paginator import Paginator


#メインページの作成
def index(request,num=1):
    #ToDoの追加
    if (request.method=='POST'):
        do = request.POST['do']
        DDo = Do(do=do)
        DDo.save()
    #ToDoの更新
    data = Do.objects.all()
    #ページネーション
    page = Paginator(data,5)
    #共通処理
    params={
        'title':'ToDo',
        'msg':'Your ToDo',
        'data':page.get_page(num),
        'cform':CreateForm(),
    }
    return render(request, 'mytodo/index.html', params)

#達成したToDoをDidへ移動するときの処理
def achieved(request,num):
    #達成したToDoをDidへ移動する
    achieveddata = Do.objects.get(id=num)
    diddata = achieveddata
    diddid = Did(did=diddata)
    diddid.save()
    achieveddata.delete()
    #ToDoの更新
    data = Do.objects.all()
    #ページネーション
    page = Paginator(data,5)
    #共通処理
    params={
        'title':'ToDo',
        'msg':'Your ToDo',
        'data':page.get_page(num),
        'cform':CreateForm(),
    }
    return render(request, 'mytodo/index.html', params)

#過去に達成したToDoの表示(Didの表示)
def youdid(request,num=1):
    #全てのDidの表示
    data = Did.objects.all()
    #ページネーション
    page = Paginator(data,5)
    #共通処理
    params = {
        'title':'ToDo',
        'msg':'Things you did',
        'data':page.get_page(num),
    }
    return render(request,'mytodo/did.html', params)

#Didを消去する際の処理
def diddelete(request,num):
    #Didの消去
    deletedata = Did.objects.get(id=num)
    deletedata.delete()
    #Didの更新
    data = Did.objects.all()
    #ページネーション
    page = Paginator(data,5)
    #共通処理
    params = {
        'title':'ToDo',
        'msg':'Things you did',
        'data':page.get_page(num),
    }
    return render(request,'mytodo/did.html', params)
