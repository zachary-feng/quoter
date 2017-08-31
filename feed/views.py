from django.shortcuts import render, HttpResponseRedirect
from .models import Quote
from .forms import QuoteForm

def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.cleaned_data["quote"]
            person = form.cleaned_data["person"]
            quote_obj = Quote()
            quote_obj.quote = quote
            quote_obj.person = person
            quote_obj.save()
            return HttpResponseRedirect('/feed/')
        all_quotes = Quote.objects.all()
    else:
        form = QuoteForm()
        all_quotes = Quote.objects.all()
    return render(request, 'feed/index.html', {'form': form, 'all_quotes': all_quotes})

'''
def submit(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.cleaned_data["quote"]
            person = form.cleaned_data["person"]
            quote_obj = Quote()
            quote_obj.quote = quote
            quote_obj.person = person
            quote_obj.save()
            return HttpResponseRedirect('/feed/')
    else:
        form = QuoteForm()
    return render(request, 'feed/index.html', {'form': form})
'''