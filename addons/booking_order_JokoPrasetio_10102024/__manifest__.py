{
    'name': 'Booking Order Joko Prasetio',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage booking orders, work orders, and service teams',
    'license': 'LGPL-3',
    'depends': ['sale', 'base'],
    'data': [
        'views/service_team_views.xml',
        'views/sale_order_views.xml',
        'views/work_order_views.xml',
        'data/sequence_data.xml',
    ],
    'installable': True,
    'application': True,
}
