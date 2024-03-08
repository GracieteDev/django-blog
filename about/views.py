from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    renders the most recent information on the website author and allows user collaboration requests.
    Displays an individual instance of the About model:model:`about.About` and a form to submit a collaboration request.
    
    **Context** 
    The two variables returned in the context by the view are:
    ``about``
        The most recent instance of : model:`about.About`.
    ``collaborate_form``
        An instance of : form:`about.CollaborateForm`. (This is the form that is rendered by this view.)
    **Template**
        :template:`about/about.html`. (This is the template that is rendered by this view.)
        
    Conclusion: This format is the standard  for documentation in Django models and views. Using markdown enables emphasis on the relationships between the view,model, form and template. It's important to to use docstrings to show to other devs which models, views, forms , and templates are linked. when working in a team in a large project with multiple apps. 
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )