from django.shortcuts import render
from .models import Post
from .forms import ContactForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email)
            # Here you can access form.cleaned_data to get the form data
            # Example: name = form.cleaned_data['name']
            # Then perform necessary actions (e.g., send email)
            return render(request, 'blog/contact_success.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'blog/contact_us.html', {'form': form})