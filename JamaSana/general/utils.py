
from .models import PerfilParametrizado

def is_greater(values, input):
    return input >= values[0]

def is_lower(values, input):
    return input <= values[0]

def is_equal(values, input):
    return input == values[0]

def is_between(values, input):
    return input >= values[0] and input <= values[1]

def is_outer(values, input):
    return input < values[0] or input > values[1]

comparator_selector = {
    1: is_greater,
    2: is_lower,
    3: is_equal,
    4: is_between,
    5: is_outer
}

def search_in_pesos(perfiles, peso_enviado):
    lista_resultante = []
    modo = 0
    for perfil in perfiles:
        modo = perfil.peso_mode_comparator
        if modo  >= 1 and modo <= 5:
            temp = [perfil.peso_minimo, perfil.peso_maximo]
            if comparator_selector[modo](temp, peso_enviado):
                lista_resultante.append(perfil)
    return lista_resultante

def search_in_altura(perfiles, altura_enviado):
    lista_resultante = []
    modo = 0
    for perfil in perfiles:
        modo = perfil.altura_mode_comparator
        if modo  >= 1 and modo <= 5:
            temp = [perfil.altura_minimo, perfil.altura_maximo]
            if comparator_selector[modo](temp, altura_enviado):
                lista_resultante.append(perfil)
    return lista_resultante

def search_in_imc(perfiles, imc_enviado):
    lista_resultante = []
    modo = 0
    for perfil in perfiles:
        modo = perfil.imc_mode_comparator
        if modo  >= 1 and modo <= 5:
            temp = [perfil.imc_minimo, perfil.imc_maximo]
            if comparator_selector[modo](temp, imc_enviado):
                lista_resultante.append(perfil)
    return lista_resultante