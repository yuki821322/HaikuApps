import random
from django.http import HttpResponse
from .model import Kigo
def index(request):
  Kigo=random.choice(list(Kigo.objects.all()))
  return HttpResponse(f"お題:{kigo.word}
  ({Kigo.get_season_display()}・{kigo.get_genre_display()})")