from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Portfolio
from .forms import PortfolioPost
# Create your views here.


def portfolio(request):
    portfolios = Portfolio.objects
    portfolio_list = Portfolio.objects.all()
    paginator = Paginator(portfolio_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'portfolio.html', {'portfolios': portfolios, 'posts':posts})


def portfoliopost(request):
    #입력된 내용 처리
    if request.method == 'POST':
        form = PortfolioPost(request.POST)
        #제대로된 값이 입력됐는지 확인
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')        
    #빈페이지를띄워줌
    else:
        form = PortfolioPost()
        return render(request, 'newport.html', {'form':form})