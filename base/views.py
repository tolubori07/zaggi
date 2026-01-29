from django.shortcuts import render,redirect,get_object_or_404
from.models import Items,ItemView,User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from.forms import Myusercreationform,addressform
from.utils import add_to_bag
from django.http.response import JsonResponse
from django.db.models import Q
from django.template import RequestContext
from .utils import get_random_activity
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
     types = Items.types
     context={'types': types}
     return render(request, 'base/home.html',context)

def loginpage(request):
    types = Items.types
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

    context = {'page': page,'types': types}
    return render(request, 'base/login_register.html', context)

def registerpage(request):
    types = Items.types
    form = Myusercreationform()
    if request.method == 'POST':
        form = Myusercreationform(request.POST)
        if form.is_valid():
           user = form.save(commit = False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           subject = 'welcome to Zaggi Wears!!'
           message = f'Hi {user.username}, thank you for registering in Zaggi.'
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [user.email]
           send_mail( subject, message, email_from, recipient_list )
           return redirect('home')
        else:
            messages.error (request, 'An error occurred while registering you')
    return render(request,'base/login_register.html', {'form':form,'types': types})


def logoutuserpage(request):
    logout(request)
    return redirect('home')

def all(request):
      q = request.GET.get('q') if request.GET.get('q') != None else ''
      items = Items.objects.filter(
        Q(category__icontains = q) |
        Q(name__icontains =q) |
        Q(description__icontains =q)
        )
      search_string = request.GET.get('q', '')
      types = Items.types
      context={"item":items,"search_string":search_string,'types':types}
      return render(request, 'base/all.html', context,)



def view(request, item_id):
    types = Items.types
    items = get_object_or_404(Items, pk=item_id)
    if request.method == 'POST':
        try:
            add_to_bag(request, item_id)
            messages.success(request, "Item added to bag successfully")
        except:
            messages.error(request,"failed to add item to bag, please try again")
    return render(request, 'base/room.html', {'items': items,'types': types})




def bag(request):
    types = Items.types
    bag_dict = request.session.get('bag', {})
    bag_items = []
    total_price = 0
    for item_id, quantity in bag_dict.items():
        item = get_object_or_404(Items, pk=item_id)
        total_price += item.price * quantity
        bag_items.append({'item': item, 'quantity': quantity})
    return render(request, 'base/bag.html', {'bag_items': bag_items, 'total_price': total_price,'types': types})



def checkout(request):
    types = Items.types
    bag_dict = request.session.get('bag', {})
    bag_items = []
    total_price = 0
    for item_id, quantity in bag_dict.items():
        item = get_object_or_404(Items, pk=item_id)
        total_price += item.price * quantity
        bag_items.append({'item': item, 'quantity': quantity})
    return render(request, 'base/checkout.html' ,{'bag_items': bag_items, 'total_price': total_price,'types': types})






def custom_404(request, exception):
    activity = get_random_activity()
    return render(request, '404.html', {'activity': activity}, status=404)
