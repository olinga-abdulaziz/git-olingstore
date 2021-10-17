from django.shortcuts import render
from myaccount.models import Products,Profile
from myaccount.forms import AddProductForm
from django.views import generic

# Create your views here.
class HomeView(generic.ListView):
    model=Products
    template_name='baseapp/home.html'
    

    def get_context_data(self, *args, **kwargs):
        context=super(HomeView, self).get_context_data(*args, **kwargs)
        bycles=Products.objects.filter(category='Bycles')
        electronics=Products.objects.filter(category='Electronics')
        clothings=Products.objects.filter(category='Clothings')
        farms=Products.objects.filter(category='Farming')
        housing=Products.objects.filter(category='Housing')
        profile=Profile.objects.all()
        motobike=Products.objects.filter(category='Motorbikes')
        ordering='-id'
        others=Products.objects.filter(category='Others')
        school=Products.objects.filter(category='School')
        vehicle=Products.objects.filter(category='Vehicles')
        context['bycles']=bycles
        context['clothings']=clothings
        context['housing']=housing
        context['motobikes']=motobike
        context['others']=others
        context['schools']=school
        context['profiles']=profile
        context['vehicles']=vehicle
        context['electronics']=electronics
        context['farms']=farms
        return context

def searchView(request):
    if request.method == 'POST':
        
        searched=request.POST['searched']
        searchedQuery=Products.objects.filter(product_name=searched)
        context={
                "searched":searched
                 }
        return render(request,'baseapp/search.html',context)
    else:
        searched=Products.objects.filter(product_name='Farming')
        context={
    
                 }
        return render(request,'baseapp/search.html',context)


class ProductDetailView(generic.DetailView):
    model=Products
    context_object_name='product'
    template_name='baseapp/product_detail.html'
    

def aboutView(request):
    return render(request,'baseapp/about.html',{})



def contactView(request):
    return render(request,'baseapp/contact.html',{})


class ClothingList(generic.ListView):
    model=Products
    context_object_name='product'
    ordering='-id'
    template_name='baseapp/clothings.html'
    queryset=Products.objects.filter(category='Clothings')

class CyclesList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    template_name='baseapp/bycles.html'
    queryset=Products.objects.filter(category='Bycles')

class ElectronList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    queryset=Products.objects.filter(category='Electronics')
    template_name='baseapp/electronic.html'

class FarmList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    template_name='baseapp/farm.html'
    queryset=Products.objects.filter(category='Farming')

class HousinggList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    template_name='baseapp/housing.html'
    queryset=Products.objects.filter(category='Housing')

class MotobikeList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    template_name='baseapp/motobike.html'
    queryset=Products.objects.filter(category='Motorbikes')

class OthersList(generic.ListView):
    model=Products
    ordering='-id'
    context_object_name='product'
    queryset=Products.objects.filter(category='Others')
    template_name='baseapp/others.html'

class VehiclesList(generic.ListView):
    ordering='-id'
    model=Products
    context_object_name='product'
    queryset=Products.objects.filter(category='Vehicles')
    template_name='baseapp/vehicle.html'

class SchoolView(generic.ListView):
    ordering='-id'
    model=Products
    context_object_name='product'
    queryset=Products.objects.filter(category='School')
    template_name='baseapp/school.html'




def add_view(request):
    return render(request,'baseapp/add_post.html',{})
