from enum import Enum


class RangoArticial(Enum):
    """ CyberDesastre, CyberHelper, CyberProgramer, CyberMech """
    CYBER_DISASTER = "CyberDesastre"
    CYBER_MECH = "CyberMech"
    CYBER_HELPER = "CyberHelper"
    CYBER_PROGRAMER = "CyberProgramer"

class Laboratorio(Enum):
    """ DEXTER LABORATORIO, LABORATORIO UMBRELLA, LABORATORIO FIXER, LABORATORIO BAD BUNNY"""
    DEXTER_LABORATORIO = "Dexter Labatorio"
    LABORATORIO_UMBRELLA = "Labotorio UMBRELLA"
    LABORATORIO_FIXER = "Labotorio Fixer"
    LABORATORIO_BAD_BUNNY = "Labotorio Bad Bunny"

class Estado(Enum):
    VIVO = "VIVO"
    MUERTO = "MUERTO"

class HumanStatus(Enum):
    CABO = "CABO"
    CORONEL = "CORONEL"
    COMANDANTE = "COMANDANTE"
    SOLDADO_RAZO= "SOLDADO_RAZO"
    PILOTO_ = "PILOTO"

class Sexo(Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"

class RazaAlienigena(Enum):
    NOXIANOS = "NOXIANOS"
    REDRAGONIANOS = "REDRAGONIANOS"
    PITUFOS = "PITUFOS"
    XARAMAS = "XARAMAS"

class Elemento(Enum):
    FUEGO = "FUEGO"
    HIELO = "HIELO"
    TIERRA = "TIERRA"
    AIRE = "AIRE"
    PSIQUICO = "PSIQUICO"
    VENENO = "VENENO"
    NORMAL = "NORMAL"

class ShClass(Enum):
    DESASTRE = "DESASTRE"
    NORMAL = "NORMAL"
    SUPERFUERTE = "SUPERFUERTE"
    VELOCISTA = "VELOCISTA"
    PSIQUICOS = "PSIQUICOS"
    PIROMANOS = "PIROMANOS"