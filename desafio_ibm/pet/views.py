from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from . import models, forms


class PetList(LoginRequiredMixin, ListView):
    model = models.Pet
    template_name = "pet/pet_list.html"

    def get_queryset(self):
        queryset = super(PetList, self).get_queryset()

        return queryset.filter(creator=self.request.user)


class PetCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Pet
    form_class = forms.PetForm
    template_name = "pet/pet_create_form.html"
    success_url = reverse_lazy("pet:pet_list")
    success_message = "Pet criado com sucesso!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class PetUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Pet
    form_class = forms.PetForm
    template_name = "pet/pet_update_form.html"
    success_url = reverse_lazy("pet:pet_list")
    success_message = "Pet atualizado com sucesso!"


class PetDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Pet
    template_name = "pet/pet_confirm_delete.html"
    success_url = reverse_lazy("pet:pet_list")
    success_message = "Pet removido com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PetDelete, self).delete(request, *args, **kwargs)
