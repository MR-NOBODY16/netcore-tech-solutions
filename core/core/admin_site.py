from django.contrib.admin import AdminSite


class NetCoreAdminSite(AdminSite):
    """
    Custom Django AdminSite for NetCore TECH Solutions.
    """

    site_header = "NetCore TECH Solutions"

    site_title = "NetCore Administration"

    index_title = "NetCore TECH Solutions Administration"

    site_url = "/"

    enable_nav_sidebar = True


netcore_admin_site = NetCoreAdminSite(
    name="netcore_admin",
)