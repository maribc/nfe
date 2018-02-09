# coding=utf-8
from django.contrib import admin
from django.http import response
from django.http import HttpResponse
from .models import Cabecera, Posicion
import requests
import csv
class PosicionInlineAdmin(admin.StackedInline):
    model = Posicion
    # raw_id_fields = ("email",)


class CabeceraAdmin(admin.ModelAdmin):
    model = Cabecera
    list_display = ['id_doc', 'name', 'stcd2']
    inlines = [PosicionInlineAdmin]
    actions = ['gera_txt']
    search_fields = ['posicion__ad_smtpadr']

    # Action gera txt
    # def gera_txt(self, request, object):
    def gera_txt(self, request, object):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        for cabecera in Cabecera.objects.all():
            for posicione in cabecera.id_doc_Posicion.all():
                writer.writerow("write something")
                # writer.writerow(" ".join([cabecera, posicione]))
            return response
        # response = HttpResponse(content_type="text/csv")
        # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        # with open('cabecera.txt', 'w') as file:
        #     for cabecera in Cabecera.objects.all():
        #         cabecera.tp_reg, str(cabecera.id_doc), str(cabecera.branch), cabecera.waers, cabecera.client, cabecera.name, cabecera.stras, cabecera.house_num1, cabecera.pstlz, cabecera.ort01, cabecera.ort02, cabecera.land1, cabecera.regio, cabecera.stcd2, cabecera.observat
        #         for posicione in cabecera.id_doc_Posicion.all():
        #             posicione.tp_reg, posicione.id_doc, posicione.matnr, posicione.menge, posicione.netwr, posicione.ad_smtpadr
        #         file.write(" ".join(cabecera + posicione) + '\n')
        #     return response

    gera_txt.short_description = 'Enviar txt'


admin.site.register(Cabecera, CabeceraAdmin)
admin.site.disable_action('delete_selected')
