import os

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_label.apps import AppConfig as BaseEdcLabelAppConfig

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'example_lab'
    base_template_name = 'example_lab/base.html'
    dashboard_url_name = 'home_url'
    listboard_url_name = 'home_url'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'ExampleLab'
    institution = 'Botswana-Harvard AIDS Institute'
    copyright = '2017-{}'.format(get_utcnow().year)
    license = None


class EdcLabelAppConfig(BaseEdcLabelAppConfig):
    template_folder = os.path.join(
        settings.STATIC_ROOT, 'example_lab', 'label_templates')


class EdcLabAppConfig(BaseEdcLabAppConfig):
    requisition_model = 'example_lab.subjectrequisition'
    result_model = 'example_lab.result'
