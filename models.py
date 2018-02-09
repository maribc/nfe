# coding=utf-8
from django.db import models
from django.conf import settings


class Cabecera(models.Model):
    UF_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceara"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    # email = models.CharField('Email')
    tp_reg = models.CharField('Tipo', max_length=1, default='C', editable=False)
    id_doc = models.CharField('Id Cabecera', max_length=6, primary_key=True)
    branch = models.CharField('Branch', max_length=4, default='4001', editable=False)
    waers = models.CharField('Moeda', max_length=5, default='BRL', editable=False)
    client = models.CharField('Cliente', max_length=10, default='BRD005', editable=False)
    name = models.CharField('Nombre Cliente', max_length=35)
    stras = models.CharField('Rua', max_length=35)
    house_num1 = models.CharField('Número', max_length=10)
    pstlz = models.CharField('CEP', max_length=10)
    ort01 = models.CharField('Cidade', max_length=35)
    ort02 = models.CharField('Bairro', max_length=40)
    land1 = models.CharField('País', max_length=3, default='BRA', editable=False)
    regio = models.CharField('Regio', choices=UF_CHOICES, max_length=4)
    stcd2 = models.CharField('CPF', max_length=11)
    observat = models.TextField('Observação', max_length=200)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # db_column = u'PortalUsuarioNome'
    # db_column = u'PortalUsuarioCPF_CNPJ'

    class Meta:
        verbose_name = "NFe"
        verbose_name_plural = "NFe"
        app_label = 'nota_fiscal'

    def __init__(self, *args, **kwargs):
        super(Cabecera, self).__init__(*args, **kwargs)


class PosicionManager(models.Model):
    def search(self):
        return self.get_queryset().filter(search=True)


class Posicion(models.Model):
    tp_reg = models.CharField('Tipo', max_length=1, default='P', editable=False)
    id_doc = models.ForeignKey(Cabecera, on_delete=models.CASCADE, related_name='id_doc_Posicion')
    matnr = models.CharField('Material', max_length=18, editable=False, default='80010030')
    menge = models.CharField('Cantidad', max_length=3, default='1', editable=False)
    netwr = models.CharField('Valor Total', max_length=15)
    ad_smtpadr = models.EmailField('Email', max_length=70)

    objects = PosicionManager()
    # db_column = u'portal_historicopagamentoValor')
    # db_column = u'portal_usuarioEmail'

    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posicion"
        app_label = 'nota_fiscal'
        # db_table = u'portal_usuario'
        # db_table = u'portal_historicopagamento'

    def __int__(self, *args, **kwargs):
        super(Posicion, self).__int__(*args, **kwargs)


# class de Conexão do db eiplus
class EiplusRouter(object):
    """
    DATABASES_APPS_MAPPING = {'nota_fiscal' : 'default', 'nota_fiscal' : 'eiplus_db'}

    """

    def db_for_read(self, model, **hints):
        if settings.DATABASES_APPS_MAPPING.has_key(model._meta.app_label):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        if settings.DATABASE_APPS_MAPPING.has_key(model._meta.app_label):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = settings.DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = settings.DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_syncdb(self, db, model):
        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label) == db
        elif settings.DATABASE_APPS_MAPPING.has_key(model._meta.app_label):
            return False
        return None
