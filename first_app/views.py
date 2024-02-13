from django.shortcuts import render

from .forms import practice


def home(request):
    form = practice()
    if request.method == 'POST':
        form = practice(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'home.html', {'form': form})
