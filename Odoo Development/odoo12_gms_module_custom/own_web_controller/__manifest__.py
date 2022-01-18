# -*- coding: utf-8 -*-
{
    'name': "Web Controller",

    'summary': """
        Module Custom
        """,

    'description': """
        Module Custom
    """,

    'author': "Module Custom",
    'website': "http://www.bizsolution.com.kh/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contact',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'views/template.xml',
    ],

    'qweb': [        
        'static/src/xml/*.xml',
    ],  
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'AGPL-3',
    'installable' : True,
    'application' : False,
    'images': ['static/description/icon.png'],
    'auto_install' : False
}