from django.shortcuts import render, redirect
from django_project.feedback_app.forms import FeedbackForm
from django_project.feedback_app.models import Feedback

def feedback_page(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Feedback.objects.create(**data)

            return redirect("feedback:success")
    else:
        form = FeedbackForm()

    return render(request, "feedback_app/feedback.html", context={"form": form})

def success_page(request):
    return render(request, "feedback_app/success.html")
