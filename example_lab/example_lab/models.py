from django.conf import settings

if settings.APP_NAME == 'example_lab':

    from django.db import models
    from django.db.models.deletion import PROTECT
    from edc_base.model_managers import HistoricalRecords
    from edc_base.model_mixins import BaseUuidModel
    from edc_base.utils import get_utcnow
    from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
    from edc_lab.model_mixins.requisition import RequisitionIdentifierMixin
    from edc_lab.model_mixins.requisition import RequisitionModelMixin
    from edc_lab.model_mixins.requisition import RequisitionStatusMixin
    from edc_lab.model_mixins.result import ResultItemModelMixin
    from edc_lab.model_mixins.result import ResultModelMixin

    class SubjectVisit(NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

        report_datetime = models.DateTimeField(default=get_utcnow)

    class SubjectRequisition(RequisitionModelMixin,
                             RequisitionStatusMixin,
                             RequisitionIdentifierMixin,
                             BaseUuidModel):

        subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

        @property
        def visit(self):
            return self.subject_visit

        @property
        def subject_identifier(self):
            return self.visit.subject_identifier

    class Result(ResultModelMixin, BaseUuidModel):

        requisition = models.ForeignKey(SubjectRequisition, on_delete=PROTECT)

        history = HistoricalRecords()

    class ResultItem(ResultItemModelMixin, BaseUuidModel):

        result = models.ForeignKey(Result, on_delete=PROTECT)

        history = HistoricalRecords()
