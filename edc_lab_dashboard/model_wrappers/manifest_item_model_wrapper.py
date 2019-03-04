from edc_model_wrapper import ModelWrapper
from edc_lab.models import Box, ManifestItem

from ..dashboard_urls import dashboard_urls


class ManifestItemModelWrapper(ModelWrapper):

    model_cls = ManifestItem
    next_url_name = dashboard_urls.get("manage_manifest_listboard_url")
    action_name = "manage"

    @property
    def manifest_identifier(self):
        return self.object.manifest.manifest_identifier

    @property
    def box_identifier(self):
        return self.object.identifier

    @property
    def box(self):
        return Box.objects.get(box_identifier=self.object.identifier)
