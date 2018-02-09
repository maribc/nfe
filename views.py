from django.shortcuts import render
# from search_views.views import SearchListView
# from .models import Posicion
# from .forms import SearchPosicionForm
# from search_views.filters import BaseFilter

def consulta_email(request):
    """View que exibe o formulário com o email do cliente a ser
    consultado no banco de dados para retornar a lista com todas
    as compras efetuadas pelo cliente.
    """

    return render(request)

# class PosicionFilter(BaseFilter):
#     search_fields = {
#         "search_ad_smtpadr": ["ad_smtpadr"]
#     }
# class PosicionView(SearchListView):
#     model = Posicion
#     form_class = SearchPosicionForm
#     filter_class = PosicionFilter


# def consulta_dados_nota(request):
#         form = CabeceraForm(request.GET)
#         cabecera = form.save(commit=False)
#         cabecera.id_doc = 'C'
#         query = request.GET.copy()
#         pos_queryset = Posicion.objects.filter(
#             ad_smtpadr=query['email']
#         )
