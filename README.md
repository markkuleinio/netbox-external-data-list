# NetBox External Data List Plugin

This is an example plugin for NetBox, showing how to show list-formatted
external data in the NetBox GUI.

![NetBox External Data List](docs/netbox-external-data-list.png)


## Installation

```shell
cd /opt/netbox
sudo venv/bin/pip install git+https://github.com/markkuleinio/netbox-external-data-list
echo git+https://github.com/markkuleinio/netbox-external-data-list | sudo tee -a local_requirements.txt
```

Add the plugin in the NetBox configuration in `/opt/netbox/netbox/netbox/configuration.py`:

```python
PLUGINS = ["netbox_external_data_list"]
```

Restart NetBox:

```shell
sudo systemctl restart netbox netbox-rq
```


## Features

- A data list view (page) that can be populated from whatever data (see `views.py`)
- The view has pagination and column sorting
- There is a menu item in the main NetBox menu (can be removed if not needed,
the view can be directly linked as `https://your-netbox-server-address/plugins/externaldata/datalist/`)
- The output is rendered using a Django template (see the `templates` directory)
- The view has restricted permissions by default (can be removed if not needed): must have
View access to prefixes to see the page
- Tested with NetBox 3.7
