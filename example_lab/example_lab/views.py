from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_navbar import NavbarViewMixin


class HomeView(EdcBaseViewMixin, NavbarViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'example_lab/home.html'
    base_template_name = 'edc_base/base.html'
    app_config_name = 'example_lab'

    navbar_name = 'lab'
    navbar_selected_item = 'home'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdministrationView(EdcBaseViewMixin, NavbarViewMixin, AppConfigViewMixin, TemplateView):

    template_name = 'example_lab/administration.html'
    app_config_name = 'example_lab'

    navbar_name = 'lab'
    navbar_selected_item = 'administration'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(sections={
            'Consent': None,
            'Device': None,
            'Lab': None,
            'Labels': 'edc_label:home_url',
            'Metadata': None,
            'Protocol': 'edc_protocol:home_url',
            'Registration': None,
            'Synchronization': None,
            'Visit Schedule': None,
        })
        return context
