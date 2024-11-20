
from django.urls import reverse

def login_view(request):
    # ...existing code...
    return redirect(reverse('recipes:index'))
    # ...existing code...