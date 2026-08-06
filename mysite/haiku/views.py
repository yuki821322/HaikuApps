import random
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kigo, Haiku, Muchaburi
from .forms import HaikuForm

MUCHABURI_RATE = 0.4  # お題にmuchaburiが乗る確率

def index(request):
  if request.method == "POST":
    kigo = Kigo.objects.get(pk=request.POST.get("kigo_id"))
    muchaburi_id = request.POST.get("muchaburi_id")
    muchaburi = Muchaburi.objects.filter(pk=muchaburi_id).first() if muchaburi_id else None
    form = HaikuForm(request.POST)
    if form.is_valid():
      haiku = form.save(commit=False)
      haiku.kigo = kigo
      haiku.save()
      return redirect("index")
  else:
    kigo = random.choice(list(Kigo.objects.all()))
    muchaburi_pool = list(Muchaburi.objects.all())
    muchaburi = random.choice(muchaburi_pool) if muchaburi_pool and random.random() < MUCHABURI_RATE else None
    form = HaikuForm()

  return render(request, "haiku/index.html", {"kigo": kigo, "form": form, "muchaburi": muchaburi})


def haiku_list(request):
  haikus = Haiku.objects.select_related("kigo").order_by("-created_at")
  rankings = (
    Haiku.objects.values("author_name")
    .annotate(points=Count("id"))
    .order_by("-points")[:5]
  )
  return render(request, "haiku/list.html", {"haikus": haikus, "rankings": rankings})


def haiku_detail(request, pk):
  haiku = get_object_or_404(Haiku, pk=pk)
  points = Haiku.objects.filter(author_name=haiku.author_name).count()
  return render(request, "haiku/detail.html", {"haiku": haiku, "points": points})
