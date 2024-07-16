- GLD.txt
  - contém a gramática
  - podem ser adicionadas novas regras de produção abaixo das demais
  - a estrutura do txt deve ser mantida para garantir a leitura
  - defini as variáveis para serem formadas so por um caractere
  - a gramática de exemplo aceita palavras que seguem a expressão regular =   a(ba)*   ,(a, aba, abababa, ...)

- main.py é o código em si
  - código vai validar a GLD do .txt, vai encerrar caso recuse
  - inserção da palavra, vai ser mostrado o ponteiro para cada passo
  - a execução é encerrada ao encontrar erro, mostrando a posição atual do ponteiro e o erro em si


Foi usado Python 3.12.3 com nenhuma dependência

Com o python instalado, no terminal executar:

python main.py
ou
python3 main.py