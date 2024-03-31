from netbox.plugins import PluginConfig

from .version import __version__

class ExternalDataListConfig(PluginConfig):
    name = "netbox_external_data_list"
    verbose_name = "External data list"
    description = "An example NetBox plugin"
    version = __version__
    author = "Markku Leiniö"
    # base_url is what comes after /plugins/ in the URL
    base_url = "externaldata"
    required_settings = []
    default_settings = {}

config = ExternalDataListConfig
