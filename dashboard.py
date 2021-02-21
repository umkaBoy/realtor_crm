"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'project.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"

        self.children.append(modules.Group(
            title='Контент',
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    title='Лоты',
                    column=1,
                    collapsible=False,
                    models=(
                        'crm.models.lots.OldBuildingLot',
                        'crm.models.lots.NewBuildingLot',
                    ),
                ),
                modules.ModelList(
                    title='Прочее',
                    column=1,
                    collapsible=False,
                    models=(
                        'crm.models.developers.Developer',
                        'crm.models.complexes.Complex',
                        'crm.models.complexes.Corp',
                    ),
                )
            ]
        ))

        self.children.append(modules.Group(
            title='Административная панель',
            column=2,
            collapsible=True,
            children = [
                modules.AppList(
                    '',
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*', 'crm.models.users.UserProfile'),
                ),
                modules.ModelList(
                    title='Базовые настройки',
                    column=1,
                    collapsible=False,
                    models=(
                        'crm.models.base.Region',
                        'crm.models.base.ConstructionTech',
                        'crm.models.base.PremisesType',
                        'crm.models.base.ObjectClass',
                        'crm.models.complexes.Floor',
                    ),
                )
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
