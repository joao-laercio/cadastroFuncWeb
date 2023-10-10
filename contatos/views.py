from django.shortcuts import render
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.


def index(request):
    if request.GET.get("q"):
        funcionarios = Funcionario.objects.filter(nome__icontains=request.GET["q"])
    else:
        funcionarios = Funcionario.objects.all()

    return render(request, "index.html", {"funcionarios": funcionarios})


def detalhar(request, id):
    funcionario = funcionarios = Funcionario.objects.get(id=id)
    return render(request, "detalhar.html", {"funcionario": funcionario})


class FuncionarioViewSet(ReadOnlyModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
