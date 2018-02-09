from django.contrib.admin import forms
from .models import Cabecera, Posicion
from django.forms import ModelForm


class CabeceraForm(forms.ModelForm):
    class Meta:
        model = Cabecera
        fields = ['stras',
                  'house_num1',
                  'pstlz', 'ort01',
                  'ort02', 'land1', 'regio', 'observat']


class PosicionForm(forms.ModelForm):
    class Meta:
        model = Posicion
        fields = ['tp_reg', 'matnr', 'menge',
                  'netwr', 'ad_smtpadr']

