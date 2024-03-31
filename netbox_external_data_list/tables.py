import django_tables2 as tables


class ExternalDataListTable(tables.Table):
    id = tables.Column()
    name = tables.Column()
    age = tables.Column()

    class Meta:
        attrs = {
            "class": "table table-hover",
        }
