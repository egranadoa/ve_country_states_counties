{
    'name': "Venezuela - Estados, Municipios y Parroquias",

    'summary': "División político-territorial de Venezuela completa: 24 entidades federales, 335 municipios y 1.136 parroquias, listas para usar en contactos, ventas, CRM, facturación y reportes.",

    'description': """
Este módulo integra en Odoo la estructura geográfica oficial de Venezuela. Incluye los 24 estados o entidades federales, sus municipios y parroquias, con identificadores externos únicos que facilitan la importación, actualización y mantenimiento de los datos.

Permite seleccionar estado, municipio y parroquia en contactos y direcciones, mejorar la segmentación comercial, generar reportes por zona, planificar rutas de entrega y cumplir con requisitos de localización. Compatible con Odoo 19. Ideal para empresas, franquicias y organizaciones que operan en Venezuela.
    """,

    'author': "Efrain Granado Alfaro",
    'website': "https://egranadoa.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/res.country.state.csv',
        'data/res.country.state.municipality.csv',
        'data/res.country.state.municipality.parish.csv',
        'views/res_partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

