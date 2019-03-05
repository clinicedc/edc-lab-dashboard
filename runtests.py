#!/usr/bin/env python
import django
import logging
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from os.path import abspath, dirname, join


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


base_dir = dirname(abspath(__file__))
app_name = 'edc_lab_dashboard'

installed_apps = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_crypto_fields.apps.AppConfig",
    "django_revision.apps.AppConfig",
    "edc_base.apps.AppConfig",
    "edc_protocol.apps.AppConfig",
    "edc_device.apps.AppConfig",
    "edc_identifier.apps.AppConfig",
    "edc_label.apps.AppConfig",
    "edc_search.apps.AppConfig",
    "edc_registration.apps.AppConfig",
    "edc_lab.apps.AppConfig",
    "edc_lab_dashboard.apps.AppConfig",
]

DEFAULT_SETTINGS = dict(
    BASE_DIR=base_dir,
    SITE_ID=10,
    ALLOWED_HOSTS=['localhost'],
    ROOT_URLCONF=f'{app_name}.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    DATABASES={
        # required for tests when acting as a server that deserializes
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(base_dir, 'db.sqlite3'),
        },
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "edc_dashboard.middleware.DashboardMiddleware",
        "edc_lab_dashboard.middleware.DashboardMiddleware",
    ],

    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,

    APP_NAME=app_name,
    EDC_BOOTSTRAP=3,
    DASHBOARD_URL_NAMES={
        "subject_listboard_url": "edc_subject_dashboard:subject_listboard_url",
        "subject_dashboard_url": "edc_subject_dashboard:subject_dashboard_url",
    },
    LAB_DASHBOARD_REQUISITION_MODEL="edc_lab.subjectrequisition",
    LAB_DASHBOARD_URL_NAMES={},
    LAB_DASHBOARD_BASE_TEMPLATES={},

    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    MIGRATION_MODULES=DisableMigrations(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),
)


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
