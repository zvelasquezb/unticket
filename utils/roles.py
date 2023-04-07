import random

ROLES = ['Recepción', 'Administrador', 'Solicitante', 'Gestor 1', 'Gestor 2']

def get_roles(n):
    return random.sample(ROLES, n)