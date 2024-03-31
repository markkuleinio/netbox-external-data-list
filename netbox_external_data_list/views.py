import django_tables2 as tables
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.htmx import is_embedded, is_htmx
from utilities.paginator import EnhancedPaginator, get_paginate_count
from .tables import ExternalDataListTable


EXTERNAL_DATA = [
    # This is an example of some external data that you
    # want to show in NetBox GUI
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Alice", "age": 45},
    {"id": 3, "name": "Bob", "age": 32},
    {"id": 4, "name": "Mary", "age": 18},
    {"id": 5, "name": "David", "age": 70},
    {"id": 6, "name": "Emma", "age": 37},
    {"id": 7, "name": "James", "age": 28},
    {"id": 8, "name": "Sarah", "age": 52},
    {"id": 9, "name": "Michael", "age": 65},
    {"id": 10, "name": "Sophia", "age": 23},
    {"id": 11, "name": "Chris", "age": 41},
    {"id": 12, "name": "Olivia", "age": 30},
    {"id": 13, "name": "Daniel", "age": 49},
    {"id": 14, "name": "Emily", "age": 20},
    {"id": 15, "name": "William", "age": 58},
    {"id": 16, "name": "Ava", "age": 27},
    {"id": 17, "name": "Matthew", "age": 47},
    {"id": 18, "name": "Grace", "age": 36},
    {"id": 19, "name": "Andrew", "age": 53},
    {"id": 20, "name": "Chloe", "age": 22},
    {"id": 21, "name": "Ryan", "age": 39},
    {"id": 22, "name": "Lily", "age": 44},
    {"id": 23, "name": "Ethan", "age": 19},
    {"id": 24, "name": "Isabella", "age": 34},
    {"id": 25, "name": "Nathan", "age": 61},
    {"id": 26, "name": "Mia", "age": 26},
    {"id": 27, "name": "Joseph", "age": 43},
    {"id": 28, "name": "Charlotte", "age": 31},
    {"id": 29, "name": "Jason", "age": 50},
    {"id": 30, "name": "Samantha", "age": 29},
    {"id": 31, "name": "Luke", "age": 38}
]


class ExternalDataListView(PermissionRequiredMixin, View):
    # This allows only users having View access to prefixes.
    # If you don't need this kind of control, just remove this and
    # the PermissionRequiredMixin from the class.
    permission_required = "ipam.view_prefix"

    def get(self, request):
        table = ExternalDataListTable(EXTERNAL_DATA)
        paginate = {
            'paginator_class': EnhancedPaginator,
            'per_page': get_paginate_count(request),
        }
        tables.RequestConfig(request, paginate).configure(table)
        if is_htmx(request):
            if is_embedded(request):
                table.embedded = True
            return render(request, 'htmx/table.html', {'table': table})
        return render(
            request,
            "netbox_external_data_list/datalist.html",
            {
                "table": table,
            },
        )
