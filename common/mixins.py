from typing import Any

from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin


class DisableFormFieldsMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

class RecentObjectsMixin:
    recent_results_limit = 3

    @property
    def object_list(self):
        return self.__object_list

    @object_list.setter
    def object_list(self, value):
        self.__object_list = value[:self.recent_results_limit]

class SuccessMessageMixin(SingleObjectMixin):
    success_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response