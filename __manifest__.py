# -*- coding: utf-8 -*-
{
    'name': "Location des Biens Immobiliers",


    'author': "Diamila",
    'website': "http://www.goaddons.com",
    'description': """
Module pour la gestion locative des biens immobiliers
    """,


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','portal','resource','analytic','sale','product','crm'],

    # always loaded
    'data': [
        'views/biens_view.xml',
        'views/locataires_view.xml',
        'views/locataire_potentiel_view.xml',
        'views/locations_view.xml',
        'views/etat_des_lieux_view.xml',
        'views/rapport_paiement.xml',
        'views/bailleur_view.xml',
        'views/villes_quartiers_view.xml',
        'views/article.xml',
        'reports/contratpdf_templete.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',
        'reports/contratpdf_close.xml',
        'wizard/create_locataire.xml',
        'views/locataire_p.xml',
        'views/assets.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',    ],
}

