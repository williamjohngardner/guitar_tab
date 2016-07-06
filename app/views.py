from django.shortcuts import render


def tab_list_view(request):
    return render(request, "index.html", {})
