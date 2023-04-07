import random

roles = ['Recepción', 'Administrador', 'Solicitante', 'Gestor 1', 'Gestor 2']

def get_roles(n):
    return random.sample(roles, n)