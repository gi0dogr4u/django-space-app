from django.shortcuts import render, get_object_or_404

from gallery.models import Gallery


def index(request):
    gallery = Gallery.objects.order_by("-date").filter(publish=True)
    return render(request, 'gallery/index.html', {"cards": gallery})


def imagem(request, photo_id):
    photo = get_object_or_404(Gallery, pk=photo_id)
    return render(request, 'gallery/imagem.html', {"photo": photo})


def search_for_keyword(request):
    gallery = Gallery.objects.order_by("-date").filter(publish=True)

    if "search" in request.GET:
        keyword = request.GET['search']
        if keyword:
            gallery = gallery.filter(name__icontains=keyword)

    return render(request, "gallery/search.html", {"cards": gallery})

