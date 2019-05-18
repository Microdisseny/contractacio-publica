from django.db import models


class Contractant(models.Model):
    codi = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    descartat = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.nom, self.codi)

    class Meta:
        verbose_name = 'Contractant'
        verbose_name_plural = 'Contractants'


# class Licitacio(models.Model):
#     codi = models.CharField(max_length=255, unique=True)
#     nom = models.TextField(null=True, blank=True)
#     estat = models.CharField(max_length=255, null=True, blank=True)
#     data_publicacio = models.CharField(max_length=255, null=True, blank=True)
#     url = models.TextField(null=True, blank=True)
#     codi_expedient =
#     tipus_expedient =
#     tipus_contracte =
#     subtipus_contracte =
#     procediment_licitacio =
#     compra_innovacio =
#     descripcio_prestacio =
#     observacions = models.TextField(null=True, blank=True)
#     ambit_geografic
#     Termini de presentació d'ofertes
#     valor_estimat_contracte
#     import_ = models.CharField(max_length=255, null=True, blank=True)
#     termini_execucio = models.CharField(max_length=255, null=True, blank=True)


camps = {
    # 'divisio-en-lots',
    'estat': 'estat',
    # 'resolucio-d-adjudicacio',
    # 'subhasta-electronica',
    'observacions': 'observacions',
    'motiu-d-adjudicacio': 'motiu_adjudicacio',
    # 'tramitacio-simplificada',
    # 'tipus-d-anul-lacio',
    # 'data-de-la-decisio-de-no-adjudicar-o-subscriure-el-contracte',
    'tipus-de-contracte': 'tipus_contracte',
    # 'compra-d-innovacio',
    'termini-de-presentacio-d-ofertes': 'termini_presentacio_ofertes',
    # 'projecte-constructiu-nova-captacio-cervia-de-ter-sig-pdf',
    'url': 'url',
    'import-sense-iva': 'import-sense-iva',
    'id': 'codi',
    'subtipus-de-contracte': 'subtipus_contracte',
    # 'contracte-harmonitzat',
    # 'plec-de-clausules-administratives',
    # 'tramitacio-simplificada-abreujada',
    'termini-d-execucio': 'termini_execucio',
    'import': 'import_',
    'pressupost-de-licitacio': 'pressupost_licitacio',
    'durada-del-contracte': 'durada_contracte',
    'descripcio-de-la-prestacio': 'descripcio-de-la-prestacio',
    'dades-de-l-empresa-adjudicataria': 'empresa-adjudicataria',
    # 'informes-tecnics',
    'procediment-de-licitacio': 'procediment-de-licitacio',
    'data-de-publicacio': 'data-de-publicacio',
    'condicions-d-execucio': 'condicions_execucio',
    # 'obertura-de-pliques',
    # 'criteris-d-adjudicacio',
    # 'plec-de-prescripcions-tecniques',
    # 'termini-per-a-la-formalitzacio-del-contracte',
    # 'organ-de-contractacio',
    # 'obertura-de-pliques-data-prevista-d-obertura-de-proposicions',
    # 'quadre-comparatiu-d-ofertes-i-puntuacions',
    # 'nacionalitat',
    # 'descripcio-de-l-anul-lacio',
    # 'data-de-l-anul-lacio',
    # 'data-d-adjudicacio-del-contracte',
    # 'codi-cpv',
    # 'numero-d-ofertes-rebudes',
    # 'descripcio-de-la-decisio-de-no-adjudicar-o-subscriure-el-contracte',
    # 'nombre-de-lots',
    # 'oferta-integradora',
    # 'identitat-d-empreses-licitadores',
    # 'classificacio-empresarial',
    'ambit-geografic': 'ambit-geografic',
    # 'informacio-complementaria-sobre-la-prorroga',
    # 'valor-estimat-del-contracte',
    # 'es-preveuen-modificacions-als-plecs',
    # 'motiu-d-anul-lacio', 'motiu_anul-lacio',
    # 'anunci-licitacio-1-pdf',
    # 'obertura-de-pliques-obertura-de-proposicions',
    # 'personal-pdf',
    # 'reserva-social',
    'codi-d-expedient': 'codi-d-expedient',
    'tipus-d-expedient': 'tipus_expedient',
    # 's-accepten-variants',
    # 'acords',
    # 'denominacio',
    # 'anunci-signat-pdf',
    'title': 'title'
    # 'garantia-provisional',
    # 'prorroga',
    # 'es-compra-innovacio'

}
