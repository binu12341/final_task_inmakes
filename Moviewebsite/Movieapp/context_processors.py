from .models import Add_movies

def menu_links(request):
    links=Add_movies.objects.all()
    return dict(links=links)