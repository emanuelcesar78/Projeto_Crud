import pandas
import matplotlib.pyplot as plt
import numpy


class Funcionario:

    __slots__=['_nome_','_idade_','_CPF_']

    _DATA_Funcionario = {
        'nome':[],
        'idade':[],
        'cpf':[],
        'Crachar':[],
        'numero':[]
    }
    _dados_funcionario_= _DATA_Funcionario
    @classmethod
    def crachar_e_numeros_de_Funcionario(cls):
        NUMERO =  len(cls._dados_funcionario_['nome']) + 1
        cls._dados_funcionario_['numero'].append(NUMERO)

        crachar_novo = ''.join(map(str,numpy.random.randint(0,9,5)))
        cls._dados_funcionario_['Crachar'].append(crachar_novo)




    def __init__(self,_nome_,_idade_,_CPF_):
        self._nome_=_nome_
        self._idade_ = _idade_
        self._CPF_= _CPF_
        Funcionario._dados_funcionario_['nome'].append(_nome_)
        Funcionario._dados_funcionario_['idade'].append(_idade_)
        Funcionario._dados_funcionario_['cpf'].append(_CPF_)
        Funcionario.crachar_e_numeros_de_Funcionario()



    @classmethod
    def adicionar_Banco(cls,nome,idade,CPF):

        if nome in cls._dados_funcionario_['nome']:
            return "O nome já esta no banco de dados!"
        if idade < 18 or idade >65:
            return "A idade não bate com os requisitos!"
        if CPF in cls._dados_funcionario_['cpf']:
            return "cpf existente, algo não esta certo aqui!"

        cls._dados_funcionario_['nome'].append(nome)
        cls._dados_funcionario_['idade'].append(idade)
        cls._dados_funcionario_['cpf'].append(CPF)
        return "Dados cadastrados!"

    @classmethod
    def Demitir(cls,cpf):

        if cpf not in cls._dados_funcionario_['cpf']:
            return "CPF não existente"

        index = cls._dados_funcionario_['cpf'].index(cpf)
        for c in cls._dados_funcionario_.keys():
            cls._dados_funcionario_[c].pop(index)
        return "Funcionario demitido!"
    @classmethod
    def salvar_dados(cls):
        dados = pandas.DataFrame(cls._dados_funcionario_)

        dados.to_csv("historicos de funcionario.csv", index = False)

        return "Historico salvo"





























