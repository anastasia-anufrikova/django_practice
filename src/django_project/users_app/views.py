from django.views.generic import DetailView, UpdateView, CreateView
from .forms import ProfileForm, CustomCreationForm
from .models import Profile
from django.urls import reverse, reverse_lazy


class ProfileView(DetailView):
    model = Profile
    template_name = "users_app/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileUpdateView(ProfileView, UpdateView):
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_edit"] = True
        return context

    def get_success_url(self):
        return reverse("users:profile_view")

class RegistrationView(CreateView):
    form_class = CustomCreationForm
    template_name = 'users_app/register.html'
    success_url = reverse_lazy('users:register')
