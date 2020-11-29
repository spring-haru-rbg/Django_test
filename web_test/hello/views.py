# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm #追加
from .models import Friend #追加
from django.shortcuts import redirect #追加

# Create your views here.

def index(request):
    data = Friend.objects.all()
    params = {
        #'sample' : 'こんにちは',
        #'bun' : '3限',
        #'memo' : '次のページ',
        #'nextpage' : 'test',
        'title' : 'Hello',
        #'message' : 'all friends.',
        'data' : data,
        #'form' : HelloForm()        #pythonの型
    }
    #if(request.method == 'POST'):
     #   params['message'] = '名前:' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢:' + request.POST['age'] #if文追加
     #   params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html',params)

def test(request):
    params = {
        'sample' : 'こんばんわ',
        'bun' : 'おやすみ',
        'memo' : '次のページ',
        'nextpage' : 'index',
    }
    return render(request, 'hello/index.html',params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title' : 'Hello/Form',
        'msg' : 'こんにちは' + msg + 'さん。',
    }
    return render(request, 'hello/index.html',params)

#create model
def create(request):
    params = {
        'title' : 'Hello',
        'form' : HelloForm(),
    }
    if(request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)




