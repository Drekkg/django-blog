from django.shortcuts import render
from django.views import generic
from .models import About
from django.shortcuts import render, get_object_or_404


# Create your views here.


def about_me(request):
    """
  Display the about me content`.

  **Context**

  ``post``
      An instance of :model:`blog.Post`.

  **Template:**

  :template:`about/about_detail.html`
  """
    about = About.objects.all().order_by('-created_on').first()
    return render(
        request,
        "about/about_detail.html",
        {"about": about
         }
    )
