from netbox.plugins import PluginMenu, PluginMenuItem

# If you don't need any menu items, just leave this file out


menuitem1 = PluginMenuItem(
    # "datalist" is defined in urls.py
    link="plugins:netbox_external_data_list:datalist",
    link_text="External Data List",
)

menu = PluginMenu(
    label="External Data",
    groups=(
        ("Data", (menuitem1,)),
    ),
    # See the icons in https://pictogrammers.com/library/mdi/
    # (remember to add the "mdi-" prefix)
    icon_class="mdi mdi-invoice-list-outline",
)
