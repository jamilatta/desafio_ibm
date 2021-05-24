from __future__ import absolute_import, unicode_literals

import math

from collections import OrderedDict

from django.http import Http404
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

import pysolr


solr = pysolr.Solr(
    settings.HAYSTACK_CONNECTIONS["default"]["URL"],
    timeout=settings.HAYSTACK_CONNECTIONS["default"]["SOLR_TIMEOUT"],
)


def search(request):
    fqs = []
    filters = {}
    search_query = request.GET.get("q", None)
    search_field = request.GET.get("search-field", None)
    fqfilters = request.GET.get("filters", None)
    facet_name = request.GET.get("more_facet_name", None)
    facet_count = request.GET.get("more_facet_count", None)
    sort_by = request.GET.get("selectSortKey", "score asc")

    if search_query == "" or not search_query:
        search_query = "*:*"

    if search_field:
        search_query = search_field

    # Page
    try:
        page = abs(int(request.GET.get("page", 1)))
    except (TypeError, ValueError):
        raise Http404("Not a valid number for page.")

    rows = int(request.GET.get("itensPage", settings.SEARCH_PAGINATION_ITEMS_PER_PAGE))

    start_offset = (page - 1) * rows

    filters["start"] = start_offset
    filters["rows"] = rows

    if facet_name and facet_count:
        filters["f." + facet_name + ".facet.limit"] = facet_count

    if fqfilters:
        fqs = fqfilters.split(",")

    fqs = ['%s:"%s"' % (fq.split(":")[0], fq.split(":")[1]) for fq in fqs]

    # Adiciona sempre a coleção do usuário, quando tem unidade caso contrário
    # retornará os registros de todas as unidades.
    if request.user.is_authenticated:
        if request.user.city:
            fqs.append('city:"%s"' % request.user.city.name)

    # Adiciona o Solr na pesquisa
    search_results = solr.search(search_query, fq=fqs, sort=sort_by, **filters)

    # Cria um dicionário ordenado dos facets considerando a lista settings.SEARCH_FACET_LIST
    facets = search_results.facets["facet_fields"]
    ordered_facets = OrderedDict()

    for facet in settings.SEARCH_FACET_LIST:
        ordered_facets[facet] = facets.get(facet, "")

    if request.GET.get("raw"):
        return JsonResponse(search_results.raw_response, safe=False)

    total_pages = int(math.ceil(float(search_results.hits) / rows))

    return render(
        request,
        "search.html",
        {
            "search_query": "" if search_query == "*:*" else search_query,
            "search_results": search_results,
            "facets": ordered_facets,
            "page": page,
            "fqfilters": fqfilters if fqfilters else "",
            "start_offset": start_offset,
            "itensPage": rows,
            "settings": settings,
            "total_pages": total_pages,
            "selectSortKey": sort_by,
        },
    )
