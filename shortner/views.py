from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import ShortURL
from .forms import URLCreateForm, URLEditForm
from .utils import generate_short_key

@login_required  
def dashboard_view(request):
    # fetch only current user's URLs
    urls = ShortURL.objects.filter(user=request.user)
    return render(request, 'shortener/dashboard.html', {'urls': urls})


@login_required
def create_url_view(request):
    if request.method == 'POST':
        form = URLCreateForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            custom_key = form.cleaned_data.get('custom_key')

            if custom_key:
                if ShortURL.objects.filter(short_key=custom_key).exists():
                    form.add_error('custom_key', 'This key is already taken')
                    return render(request, 'shortener/create.html', {'form': form})
                url.short_key = custom_key
            else:
                url.short_key = generate_short_key()
            url.user = request.user
            url.save()
            return redirect('dashboard')
    else:
        form = URLCreateForm()
    return render(request, 'shortener/create.html', {'form': form})
 
 
@login_required
def edit_url_view(request, pk):
    url = get_object_or_404(ShortURL, pk=pk, user=request.user)
    if request.method == 'POST':
        form = URLEditForm(request.POST, instance=url)
        if form.is_valid():
            url = form.save(commit=False)
            custom_key = form.cleaned_data.get('custom_key')
            if custom_key:
                if ShortURL.objects.filter(short_key=custom_key).exclude(pk=url.pk).exists():
                    form.add_error('custom_key', 'This key is already taken')
                    return render(request, 'shortener/edit.html', {'form': form})
                url.short_key = custom_key
            url.save()
            return redirect('dashboard')
    else:
        form = URLEditForm(instance=url)
    return render(request, 'shortener/edit.html', {'form': form})
 
 
@login_required
def delete_url_view(request, pk):
    url = get_object_or_404(ShortURL, pk=pk, user=request.user)
    if request.method == 'POST':
        url.delete()
        return redirect('dashboard')
    return redirect('dashboard')
 
 
def redirect_view(request, short_key):
    url = get_object_or_404(ShortURL, short_key=short_key)
    if url.expires_at and url.expires_at < timezone.now():
        return HttpResponse('This link has expired.', status=410)
    url.click_count += 1
    url.save()
    return HttpResponseRedirect(url.original_url)