from django.shortcuts import render
from rest_framework import viewsets

from .models import Product

# Create your views here.
from .serializers import ProductSerializer


def index(request):
    return render(request, 'index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-date_added')
    serializer_class = ProductSerializer


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Profile
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from backend_api.models import Product
from price_tracker_backend import settings
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProductSerializer
from django.http import JsonResponse


def home(request):
    context = {

        'products': Product.objects.all(),
        'title': 'Home'

    }
    return render(request, 'track/home.html', context)  # title is optional


class ProductListView(ListView):
    model = Product
    template_name = 'track/home.html'  # <app>/<model>_<viewtype>.html ...django searches for this covention template

    context_object_name = 'products'  # i dont understand where we defined this 'posts'...eariler home() was being called..there
    # 'posts' was defined but now when we give route as blog/ it will come diretly to postview class
    # we never defining  'posts':Post.objects.all(),.....but still it works
    ordering = ['-date_posted']
    paginate_by = 5  # how mnay pages you want to show on home page


class ProductCreateView(LoginRequiredMixin, CreateView):  # <app>/<model>_form.html ....this view follow this convention
    # LoginRequiredMixin this is written bcoz user will see post form only if he
    # logged in otherwid=se if he try toa access that route blog/post/new then it will ask
    # for login first
    # we have done this ealier while showing profile and we had used decorators there..
    # e cant use decorators with functions so we used it
    model = Product

    fields = ['product_url', 'desire_price']  # this fields should be in your model Post
    context = {

        'products': Product.objects.all(),
        'title': 'Home'

    }

    def form_valid(self, form):
        f = self.new_product(form)
        if f == 1:
            messages.success(self.request,
                             f'Product Added successfully! We will notify you via email when price drop under your desire price')
            return HttpResponseRedirect(reverse('user-products', args=[self.request.user.username]))
        if f == 0:
            messages.warning(self.request, f"Invalid URL or couldn't find proper price of product..try again")
            return HttpResponseRedirect(reverse('user-products', args=[self.request.user.username]))

    def new_product(self, form):

        from django.http import JsonResponse
        from django.views.decorators.csrf import csrf_exempt
        from scrapyd_api import ScrapydAPI
        from uuid import uuid4
        import time

        import sys
        # this path will remain in sys.path untill this program terminated
        sys.path.append("/app")
        sys.path.append("/app/price_scraper")  # in heroku we have base dir as /app

        # this path will be used in price_scraper.items,
        from price_scraper.price_scraper.spiders import jumia_spider
        from price_scraper.price_scraper.pipelines import PriceScraperPipeline

        from scrapy import signals
        from twisted.internet import reactor
        from scrapy.crawler import Crawler, CrawlerRunner, CrawlerProcess
        from scrapy.settings import Settings
        from scrapy.utils.project import get_project_settings

        from crochet import setup

        setup()
        print('hello' * 10)

        if form == -1:

            url = self.product_url

            settings = {
                'url': url,
                'USER_AGENT': 'price_scraper (+http://www.yourdomain.com)',
                'timepass': 'kya chal raha hai bhai'
            }

            def spider_closing(spider):
                """Activates on spider closed signal"""
                print("Spiderclose" * 10)
                # reactor.stop()

            crawler = Crawler(jumia_spider.jumia_spider, settings)

            crawler.signals.connect(spider_closing, signal=signals.spider_closed)

            p_obj = self

            crawler.crawl(product_object=p_obj, check=1)

            while True:
                time.sleep(1)
                # print(crawler.stats.get_stats())
                try:
                    fr = crawler.stats.get_stats()['finish_reason']
                    if fr == 'finished':
                        break
                except:
                    pass



        else:
            print("we are in else part")
            url = self.request.POST['product_url']
            d_price = self.request.POST['desire_price']

            settings = {
                'url': url,
                'USER_AGENT': 'price_scraper (+http://www.yourdomain.com)',
                'timepass': 'kya chal raha hai bhai'
            }

            def spider_closing(spider):
                """Activates on spider closed signal"""
                print("Spiderclose" * 10)

            def if_spyder_open(spider):
                print("spyderOpen__" * 10)

            u = self.request.user
            ulen1 = len(u.product_set.all())

            crawler = Crawler(jumia_spider.jumia_spider, settings)

            crawler.signals.connect(spider_closing, signal=signals.spider_closed)
            crawler.signals.connect(if_spyder_open, signal=signals.spider_opened)

            crawler.crawl(url=url, d_price=d_price, author=self.request.user, check=0, timepass='whats up..!!')

            while True:
                print(crawler.stats.get_stats())
                time.sleep(1)
                try:
                    fr = crawler.stats.get_stats()['finish_reason']
                    if fr == 'finished':
                        break
                except:
                    pass
            ulen2 = len(u.product_set.all())
            if ulen2 > ulen1:
                return 1
            elif ulen2 == ulen1:
                return 0


def about(request):
    return render(request, 'track/about.html', {'title': 'about '})  # title is optional


def first_view(request):
    return render(request, 'track/first_view.html')


def why(request):
    return render(request, 'track/why.html')


def benefits(request):
    return render(request, 'track/benefits.html')


def announce(request):
    return render(request, 'track/announcements.html')


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'desire_price']
    template_name = 'track/update_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Updated successfully!')
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # this fucntion restric user to update others post..he can update only his own post not others
        # UserPassesTestMixin thats why we write this
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserProductListView(ListView):  # when we click on title tis executed
    model = Product
    template_name = 'track/user_products.html'  #
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created..!')
            return redirect('login')
    else:

        form = UserRegisterForm()
    myform = {
        'form': form

    }
    return render(request, 'users/register.html', myform)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,

    }

    return render(request, 'users/profile.html', context)


class ProductList(APIView):
    def get(self, request, format=None):
        all_products = Product.objects.all()
        serializers = ProductSerializer(all_products, many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
