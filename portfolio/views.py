from django.shortcuts import render
from .forms import ContactForm

def landing_page(request):
    return render(request, 'portfolio/landing_page.html')

def me_by_me(request):
    return render(request, 'portfolio/me_by_me.html')

def categories(request):
    return render(request, 'portfolio/categories.html')

def best_sellers(request):
    return render(request, 'portfolio/best_sellers.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            return render(request, 'portfolio/contact.html')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def ano1_de_LEI(request):
    return render(request, 'portfolio/1st_year.html')

def ano2_de_LEI(request):
    return render(request, 'portfolio/2nd_year.html')

def ano3_de_LEI(request):
    return render(request, 'portfolio/3rd_year.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def videos(request):
    return render(request, 'portfolio/videos.html')
