# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Add details for hospital management""",

    'author': "Bikram Karki, Vacker360 Pvt. Ltd.",
    'website': "http://www.vacker360.com",

    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
}
