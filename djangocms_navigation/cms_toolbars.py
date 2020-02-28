from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, PlaceholderToolbar
from cms.toolbar_pool import toolbar_pool

from .models import MenuContent


class NavigationToolbar(PlaceholderToolbar):
    menu_model = MenuContent

    def _add_navigation_menu(self):
        if not self.request.user.has_perm(f"{self.menu_model._meta.app_label}.change_menucontent"):
            return
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER)
        url = reverse(f"admin:{self.menu_model._meta.app_label}_menucontent_changelist")
        admin_menu.add_sideframe_item(_("Navigation"), url=url, position=4)

    def post_template_populate(self):
        self._add_navigation_menu()


toolbar_pool.register(NavigationToolbar)
