import random
from django.shortcuts import render
from .models import Kigo
from .forms import HaikuForm

def index(request):
  if request.method == "POST":
    kigo = Kigo.objects.get(pk=request.POST.get("kigo_id"))
    form = HaikuForm(request.POST)
    if form.is_valid():
      haiku = form.save(commit=False)
      haiku.kigo = kigo
      haiku.save()
  else:
    kigo = random.choice(list(Kigo.objects.all()))
    form = HaikuForm()

  return render(request, "haiku/index.html", {"kigo": kigo, "form": form})