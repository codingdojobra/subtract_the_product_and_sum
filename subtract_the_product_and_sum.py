# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtrai_soma_do_produto(entrada):
    produto = 1
    soma = 0
    for numero in entrada:
        produto = produto * int(numero)
        soma = soma + int(numero)

    return produto - soma

def primeiro_teste():
    esperado = 15
    resultado = subtrai_soma_do_produto("234")
    assert resultado == esperado

def segundo_teste():
    esperado = 21
    resultado = subtrai_soma_do_produto("4421")
    assert esperado == resultado
    
primeiro_teste()
segundo_teste()