'''
Outras funções
==============

Outras funções que não se encaixam em nenhuma categoria específica.
'''
import time as _time
from tugalib.util import synonyms


#
# Controle de tempo e de saída do programa
#
@synonyms('durma')
def dormir(intervalo):
    '''Permanece sem fazer nada o intervalo de tempo fornecido (em segundos)'''

    _time.sleep(intervalo)


@synonyms('pausa', 'pause')
def pausar():
    '''Interrompe a execução até o usuário apertar a tecla <enter>'''

    input('')


@synonyms('termine')
def terminar():
    '''
    Termina a execução do programa.

    Semelhante à função sair(cod_erro), mas não requer a especificação de um
    código de erro'''

    sair(0)


@synonyms('saia')
def sair(código_erro):
    '''
    Termina a execução do programa fornecendo um código de erro ou código
    de saída.

    Um ``código_erro=0`` sinaliza que o programa terminou com sucesso. Qualquer
    outro número ou um texto representa falha'''

    raise SystemExit(código_erro)


#
# TODO: fazer funções com strings de documentação
#
def binário(x):
    '''
    Return the binary representation of an integer.
    Retorna a representação binária de um [inteiro/número inteiro].
    
    Examples
    --------
    
    >>> bin(2796202)
    '0b1010101010101010101010'
    '''
    return bin(x)
    
def booleano(x):
    '''
    Retorna verdadeiro quando o argumento x é verdadeiro, falso em caso contrário.
    Os booleanos podem ser usados como inteiros, sendo que falso equivale a 0 e verdadeiro equivale a 1.
    
    Examples
    --------
    
    >>> booleano(0)
    falso
    >>> booleano(1)
    verdadeiro
    '''
    return bool(x)
    
# bytes = bytes
def caractere(x):
    '''
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
    Retorna um texto Unicode [(padrão de representãção de qualquer caractere de um sistema de escrita)] de um caractere.
    
    Examples
    --------
    >>> caractere(227)
    >>> 'ã'   
    >>> caractere(231)
    >>> 'ç'   
    >>> caractere(224)
    >>> 'à'
    '''
    return chr(x)

def dicionário(x)
    '''
    
    Examples
    --------
    '''
    return dict(x)
    
def enumerar(x)
    '''
    Return an enumerate object.
    Retorna um objeto enumerado.
    
    Examples
    --------
    >>> musica = ['uni', 'duni', 'te']
    >>> list(enumerate(musica))
    >>> [(0, 'uni'), (1, 'duni'), (2, 'te')]    
    '''
    return enumerate(x)
    
def real(x)
    '''
    
    Examples
    --------
    '''
    return float(x)
    
def formatar    '''
    
    Examples
    --------
    '''
    return format(x)
    
def ajuda(x)
    '''
    
    Examples
    --------
    '''
    return help(x)
    
def hexadecimal(x)
    '''
    
    Examples
    --------
    '''
    return hex(x)
    
def inteiro(x)
    '''
    
    Examples
    --------
    '''
    return int(x)
    
def tamanho(x)
    '''
    
    Examples
    --------
    '''
    return len(x)
    
def lista(x)
    '''
    
    Examples
    --------
    '''
    return list(x)
    
def octal(x)
    '''
    
    Examples
    --------
    '''
    return oct(x)
    
#ord = ord

def invertido(x)
    '''
    
    Examples
    --------
    '''
    return reversed(x)
    
def conjunto(x)
    '''
    
    Examples
    --------
    '''
    return set(x)
    
def ordenado(x)
    '''
    
    Examples
    --------
    '''
    return sorted(x)
    
def texto(x)
    '''
    
    Examples
    --------
    '''
    return str(x)
    
def tupla(x)
    '''
    
    Examples
    --------
    '''
    return tuple(x)
    
def tipo(x)
    '''
    
    Examples
    --------
    '''
    return type(x)
    
verdadeiro = Verdadeiro = True
falso = Falso = False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
