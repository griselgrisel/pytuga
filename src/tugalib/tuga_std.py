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
    Fabio vai pensar como será a abordagem.
    
    Examples
    --------
    '''
    return dict(x)
    
def enumerar(x)
    '''
    Return an enumerate object.
    Retorna um objeto enumerado.
    FABIO: Estava difícil fazer um exemplinho legal só com o enumerar.
    Por isso coloquei menção á função listar que não existe no tuga_std.py
    
    Examples
    --------
    
    >>> musica = ['uni', 'duni', 'te']
    >>> listar(enumerar(musica))
    >>> [(0, 'uni'), (1, 'duni'), (2, 'te')]    
    '''
    return enumerate(x)
    
def real(x)
    '''
    Convert a string or number to a floating point number, if possible.
    Converte um texto ou número a um número de ponto flutuante, se possível.
    
    Examples
    --------
    
    >>> real(5)
    >>> 5.0
    >>> real(673.23)
    >>> 673.23000000000002
    >>> valor = "673.23"
    >>> real(valor)
    >>> 673.23000000000002
    
    '''
    return float(x)
    
def formatar    '''
    GRISELDA: ver melhor
    Examples
    --------
    
    '''
    return format(x)
    
def ajuda(x)
    '''
    Fornece ajuda sobre módulos, palavras chaves ou tôpicos do Python.

    Examples
    --------
    
    >>> ajuda(binário)
    Retorna a representação binária de um [inteiro/número inteiro]. 
    '''
    return help(x)
    
def hexadecimal(x)
    '''
    Return the hexadecimal representation of an integer.
    Retorna a representação hexadecimal de um inteiro.
    
    Examples
    --------
    
    >>> hex(6745)
    >>> '0x1a59'
    '''
    return hex(x)
    
def inteiro(x)
    '''
    Convert a number or string to an integer, or return 0 if no arguments are given.
    Converte um número ou texto num inteiro, [ou retorna 0 se nenhum argumento é fornecido].
 
    Examples
    --------
    
    >>> int(4.3)
    >>> 4
    >>> int(44.6E-1)
    >>> 4
    >>> int()
    >>> 0  
    '''
    return int(x)
    
def tamanho(x)
    '''
    Return the number of items of a sequence or collection.
    Retorna o número de itens de uma sequência ou coleção.
    
    Examples
    --------
    >>> texto="programando em python"
    >>> len(texto)
    >>> 21
    '''
    return len(x)
    
def lista(x)
    '''
    FABIO PRECISA DEFINIR ABORDAGEM
    
    Examples
    --------
    '''
    return list(x)
    
def octal(x)
    '''
    Return the octal representation of an integer.
    Retorna a representação octal de um inteiro.
    
    Examples
    --------
    
    >>> octal(22052015)
    >>> '0o124076257'
    '''
    return oct(x)
    
#ord = ord

def invertido(x)
    '''
    Return a reverse iterator.
    Retorna um iterador reverso.
    
    Examples
    --------
    
    >>> musica = ['uni', 'duni', 'te']
    >>> list(reversed(musica))
    >>> ['te', 'duni', 'uni'] 
    '''
    return reversed(x)
    
def conjunto(x)
    '''
    FABIO PRECISA DEFINIR ABORDAGEM
    
    Examples
    --------
    '''
    return set(x)
    
def ordenado(x)
    '''
    Ordena uma lista.
    
    Examples
    --------
    
    >>> sorted([5, 2, 3, 1, 4])
    >>> [1, 2, 3, 4, 5]
    '''
    return sorted(x)
    
def texto(x)
    '''
 
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    
    Cria um novo texto a partir do texto fornecido.
    
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
