err = ["Nao ha epsilon [gramatica].",
       "Caractere nao presente no alfabeto [gramatica].",
       "Caractere nao presente no alfabeto ou variavel nao declarada [gramatica].",
       "Caractere nao presente no alfabeto [palavra].",
       "Final de palavra inesperado [palavra].",
       "Nao ha regra que aceite a palavra [palavra]"]

class Producao:
    def __init__(self, prod):
        self.variavel = prod[0].replace('\n', '')
        self.regras = prod[5:].replace('\n', '').split('|') #tratando as regras
    def __str__(self): #so tratamento pra printar a producao
        return f'{self.variavel} -> {self.regras}'

class Gramatica:
    def __init__(self, file):
        self.variaveis = []
        self.alfabeto = []
        self.producoes = []
        self.ini = ''
        self.le_gramatica(file)

    def le_gramatica(self, file): #leitura do arquivo, no caso so aceita o arquivo no formato que eu defini
        with open(file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('G'):
                    self.variaveis = line.split('{')[1].split('}')[0].split(',')
                    self.alfabeto = line.split('{')[2].split('}')[0].split(',')
                    self.ini = line.split('P,')[1].split(')')[0].strip()
                else:
                    self.producoes.append(Producao(line))
    

    def eh_gld(self):
        has_epsilon = False
        for prod in self.producoes:
            if prod.variavel not in self.variaveis: #variavel nao declarada
                return False
            for regra in prod.regras:
                if regra == 'ε': #epsilon explicito
                    has_epsilon = True
                    continue
                if regra[-1] in self.variaveis: #verifica se eh gld efetivamente, ultimo simbolo = variavel, o resto alfabeto
                    if not all(char in self.alfabeto for char in regra[:-1]):
                        print(err[2])
                        return False
                else:
                    if not all(char in self.alfabeto for char in regra):
                        print(err[1])
                        return False
                    has_epsilon = True #aqui o epsilon tá subentendido

        if not has_epsilon:
            print(err[0])
            return False
        return True
        

    
    def __str__(self): #so tratamento pra printar a gramatica
        variaveis_str = ', '.join(self.variaveis)
        alfabeto_str = ', '.join(self.alfabeto)
        producoes_str = '     '.join(str(prod) for prod in self.producoes)
        return f'G = ({{{variaveis_str}}}, {{{alfabeto_str}}}, P, {self.ini})\nP:\n     {producoes_str}'

def verifica_palavra(palavra, g):
    ponteiro = 0
    cache = g.ini #variavel a ser tratada

    while ponteiro < len(palavra):
        print(f"{palavra[:ponteiro]}|{palavra[ponteiro:][:-1]}")
        if cache == 'ε':
            print(err[4])
            print(f"posicao do ponteiro: {ponteiro}")
        for prod in g.producoes:
            if prod.variavel == cache: #se for a variavel a ser tratada
                passou = False
                for regra in prod.regras:     
                    if regra[-1] in g.variaveis: #se terminar em variavel
                        if regra[:-1] == palavra[ponteiro:ponteiro+len(regra)-1]:
                            cache = regra[-1]
                            ponteiro += len(regra)-1
                            passou = True
                            break
                    if regra == palavra[ponteiro:ponteiro+len(regra)]: #regra sem variavel
                        ponteiro += len(regra)
                        cache = 'ε'
                        passou = True
                        break
                if not passou:
                    print(err[5])
                    print(f"posicao do ponteiro: {ponteiro}")
                    exit()
                    
            
            
        

g = Gramatica('GLD.txt')
if not g.eh_gld():
    print('Gramatica recusada.')
    exit()
print('gramatica aceita.')
print(g)


palavra = input('digite a palavra a ser verificada: ')
palavra = palavra + 'ε'

verifica_palavra(palavra, g)

print('palavra aceita.')