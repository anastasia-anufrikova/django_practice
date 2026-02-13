from django.views.generic import DetailView, UpdateView
from .forms import ProfileForm
from .models import Profile
from django.urls import reverse

class ProfileView(DetailView):
    model = Profile
    template_name = "users_app/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user.profile

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users_app/profile.html"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_edit"] = True
        return context

    def get_success_url(self):
        return reverse("users:profile_view")
