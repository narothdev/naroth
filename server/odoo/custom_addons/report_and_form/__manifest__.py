{
    'name': 'Report and Form Extension',
    'version': '1.0',
    'summary': 'Custom report and form view extension for Odoo',
    'description': 'This module extends the report and form views in Odoo to provide additional'
                     ' functionality and customization options.',
    'category': 'Tools/Extensions',
    'author': 'Naroth',
    'depends': ['base','purchase'],
    'data': [
        'reports/action_list.xml',
        'reports/purchase_order_hmc.xml',

    ],
    'assets': {
        'web.report_assets_common': [
            'report_and_form/static/src/css/report.css',
        ],
    },
    'installable': True,
    'application': True,
}