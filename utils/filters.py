FILTERS = {
    'solicitudes': {
        'id': {
            'column': 0,
            'unique': True,
        },
        'estado': {
            'column': 1,
            'unique': False,
        },
        'username': {
            'column': 2,
            'unique': False,
        },
        'certificado': {
            'column': 3,
            'unique': False,
        },
        'encargado': {
            'column': 4,
            'unique': False,
        },
    },
    'certificados': {
        'nombre': {
            'column': 0,
            'unique': True,
        },
        'grupo': {
            'column': 1,
            'unique': False,
        },
    }
}
