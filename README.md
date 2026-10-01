# Exercícios práticos de Python --- Fundamentos de Programação

**Material de apoio acadêmico**\
**Área:** Engenharia de Software\
**Tema:** Lógica de programação e fundamentos da linguagem Python\
**Nível:** Iniciante

## 1. Apresentação

Este conjunto reúne quatro exercícios introdutórios desenvolvidos para
praticar conceitos fundamentais da linguagem Python. As atividades foram
organizadas em arquivos independentes, permitindo executar, testar e
modificar cada programa separadamente.

O objetivo é construir familiaridade com a escrita de código, a entrada
e saída de dados, o uso de variáveis, operadores, estruturas
condicionais, laços de repetição e coleções.

## 2. Objetivos de aprendizagem

Ao concluir as atividades, espera-se que o estudante consiga:

-   Declarar variáveis e reconhecer tipos numéricos e textuais.
-   Receber informações por meio da função `input()`.
-   Converter dados com `int()` e `float()`.
-   Exibir resultados com `print()` e f-strings.
-   Utilizar operadores aritméticos e relacionais.
-   Construir decisões com `if`, `elif` e `else`.
-   Repetir instruções com `for` e `while`.
-   Armazenar e percorrer dados em listas.

## 3. Organização dos arquivos

  ------------------------------------------------------------------------------------
  Arquivo                              Atividade               Conteúdos principais
  ------------------------------------ ----------------------- -----------------------
  `01_calculadora_simples.py`          Calculadora             Entrada de dados,
                                                               conversão de tipos,
                                                               operadores e
                                                               condicionais

  `02_media_aprovacao.py`              Média do aluno          Variáveis, operações
                                                               matemáticas e tomada de
                                                               decisão

  `03_tabuleiro_de_multiplicacao.py`   Tabuada                 Laço `for` e função
                                                               `range()`

  `04_lista_de_compras.py`             Lista de compras        Listas, laço `while`,
                                                               `append()` e
                                                               `enumerate()`
  ------------------------------------------------------------------------------------

## 4. Requisitos para execução

-   Python 3 instalado.
-   Editor de código, como Visual Studio Code, ou um terminal.
-   Conhecimentos básicos de utilização do computador.

Não é necessário instalar bibliotecas externas. Todos os exercícios
utilizam recursos nativos do Python.

Para verificar a instalação, abra o terminal e execute:

``` bash
python --version
```

Em alguns sistemas Linux, o comando pode ser:

``` bash
python3 --version
```

## 5. Como executar

Abra o terminal na pasta em que os arquivos foram salvos. Em seguida,
execute um arquivo por vez.

Exemplo no Windows:

``` bash
python 01_calculadora_simples.py
```

Exemplo no Linux:

``` bash
python3 01_calculadora_simples.py
```

Para executar outra atividade, substitua o nome do arquivo pelo
exercício desejado.

## 6. Fundamentação das atividades

### Exercício 01 --- Calculadora simples

A primeira atividade apresenta a interação entre usuário e programa. Os
valores informados são convertidos para o tipo `float`, permitindo
operações com números inteiros ou decimais. A estrutura condicional
seleciona a operação solicitada. Também existe uma verificação para
impedir divisão por zero.

### Exercício 02 --- Média e situação do aluno

Nesta atividade, três notas são armazenadas em variáveis e utilizadas no
cálculo da média aritmética. Depois, estruturas condicionais classificam
o resultado conforme faixas previamente definidas. Os critérios são
apenas exemplos didáticos e podem ser adaptados às regras de uma
disciplina.

### Exercício 03 --- Tabuada

O terceiro programa utiliza o laço `for` para repetir uma operação dez
vezes. A função `range(1, 11)` gera os valores de 1 a 10, que são usados
como multiplicadores. A atividade demonstra como automatizar tarefas
repetitivas.

### Exercício 04 --- Lista de compras

A última atividade introduz o conceito de lista, uma estrutura capaz de
armazenar vários elementos. O laço `while` mantém o programa em execução
até que o usuário digite `fim`. Cada produto válido é incluído com o
método `append()`, e a função `enumerate()` permite apresentar os itens
numerados.

## 7. Sugestões de aperfeiçoamento

Depois de executar os códigos originais, recomenda-se realizar pequenas
modificações para aprofundar o aprendizado:

1.  **Calculadora:** incluir uma opção para calcular porcentagem e
    arredondar os resultados.
2.  **Média:** permitir que o usuário escolha quantas notas serão
    informadas e validar valores entre 0 e 10.
3.  **Tabuada:** permitir escolher o número inicial e final da
    multiplicação.
4.  **Lista de compras:** implementar opções para remover um produto e
    pesquisar um item já cadastrado.

Essas modificações incentivam a resolução de problemas e a autonomia na
programação.

## 8. Considerações finais

Os exercícios apresentam uma sequência de aprendizagem que parte de
operações simples e avança para estruturas de controle e armazenamento
de dados. A prática é uma etapa importante no estudo de lógica de
programação: executar, observar os resultados, identificar erros e
modificar o código ajuda a desenvolver o raciocínio computacional.

O material pode ser utilizado como roteiro de estudos, atividade
complementar ou base para novos projetos em Python.

------------------------------------------------------------------------

**Observação acadêmica:** os programas foram elaborados com finalidade
educacional. Recomenda-se que o estudante leia cada instrução, execute
os exemplos e experimente as alterações propostas, em vez de apenas
copiar o código.
