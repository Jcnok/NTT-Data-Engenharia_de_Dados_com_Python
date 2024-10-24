# Desafios de Análise de Dados com Python e Power BI

<img src="img/code.webp" referrerpolicy="same-origin" style="display: block; object-fit: cover; border-radius: 0px; width: 100%; height: 30vh; opacity: 1; object-position: center 50%;">

## Sobre

Este repositório contém uma série de desafios focados em análise de dados usando Python:

---
<a name="indice"></a>
## Índice

1. [Desafio 1 - Análise de Vendas Mensais](#desafio-1)
2. [Desafio 2 - Identificação de Produtos Mais Vendidos](#desafio-2)
3. [Desafio 3 - Criação de Classes para Dados de Vendas](#desafio-3)
4. [Desafio 4 - Agrupamento de Vendas por Categoria](#desafio-4)
5. [Desafio 5 - Fundamentos de Business Intelligence (BI)](#desafio-5)
6. [Desafio 6 - Fundamentos Sobre ETL](#desafio-6)


---



# Desafio 1
<a name="desafio-1"></a>

# Descrição do Desafio

Você está trabalhando em um projeto de **Power BI** onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o **total de vendas** e a **média mensal de vendas**, que serão usados para gerar relatórios e gráficos no Power BI. Além disso, você deverá criar uma lista em Python para calcular o **total de vendas** e a **média mensal**.

## Detalhamento

### Na função `obter_entrada_vendas()`, você deverá:

1. Utilizar o método `split(',')` para dividir a string de entrada em elementos separados por vírgula, criando uma **lista de strings**.
2. Aplicar a função `map(int, ...)` para converter cada elemento dessa lista de strings em um **inteiro**.
3. Usar a função `list()` para converter o objeto `map` resultante em uma **lista de inteiros**.

Essa lista de inteiros representará os **valores de vendas** que serão utilizados para calcular o **total** e a **média mensal de vendas** em outra função.

---

## Entrada

- Uma **lista** com 12 números inteiros, cada um representando o número de vendas realizadas em um **mês** do ano.

## Saída

- Um único número **inteiro** representando o **total de vendas** e um número **decimal** representando a **média mensal de vendas**, separados por um espaço.

---

## Exemplos

| Entrada | Saída |
| --- | --- |
| 120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190 | 2120, 176.67 |
| 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 | 780, 65.00 |
| 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 | 390, 32.50 |



```python
def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    entrada = entrada.split(',')
    vendas = list(map(int,entrada))

    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
```

     120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190


    2120, 176.67



```python
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
```

     10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120


    780, 65.00



```python
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
```

     5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60


    390, 32.50

[Voltar ao Índice](#indice)

# Desafio 2
<a name="desafio-2"></a>

# Identificando os Produtos Mais Vendidos
**XP:** 37163/41323  
**NÍVEL:** 20  
**Dificuldade:** 5/5  
**Categoria:** Básico  
**Tema:** Princípios Básicos  

## Descrição
Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido, que será usado para destacar produtos populares no relatório do Power BI.

## Detalhamento
1. **Encontre o produto com a maior contagem:**
   - Itere sobre o dicionário `contagem`, que contém a contagem de cada produto.
   - Compare a contagem atual com a contagem máxima armazenada em `max_count`.
   - Se a contagem atual for maior que `max_count`, atualize `max_count` e defina `max_produto` como o produto atual.

2. **Converter a entrada em uma lista de strings, removendo espaços extras:**
   - Use o método `split(',')` para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.
   - Utilize uma list comprehension para remover espaços em branco extras ao redor de cada string, usando o método `strip()`.

## Entrada
Uma lista de strings onde cada string representa o nome de um produto vendido.

## Saída
A string com o nome do produto mais vendido. Se houver empate, retorne qualquer um dos produtos mais vendidos.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                   | Saída   |
|----------------------------------------------------------|---------|
| Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado | Mouse   |
| Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora | Impressora |
| Webcam, Webcam, Headset, Monitor, Headset, Headset      | Headset |


```python
def produto_mais_vendido(produtos):
    contagem = {}

    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    max_produto = None
    max_count = 0

    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        if count > max_count:
            max_count = count
            max_produto = produto  

    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.split(',')
    produtos = [produto.strip() for produto in produtos]

    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
```

     Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado


    Mouse



```python
produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
```

     Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora


    Impressora



```python
produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
```

     Webcam, Webcam, Headset, Monitor, Headset, Headset


    Headset

[Voltar ao Índice](#indice)

# Desafio 3
<a name="desafio-3"></a>

# Criando Classes para Dados de Vendas
**XP:** 37163/41323  
**NÍVEL:** 20  
**Dificuldade:** 5/5  
**Categoria:** Intermediário  
**Tema:** Estrutura de Dados  

## Descrição
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, `Venda` e `Relatorio`, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

### Classe Venda
A classe `Venda` já está definida e contém as informações sobre uma venda, como:
- Produto
- Quantidade
- Valor

### Classe Relatorio
Na classe `Relatorio`, você precisa implementar os seguintes métodos:
- **adicionar_venda:** Este método deve verificar se o objeto passado é uma instância da classe `Venda` antes de adicioná-lo à lista de vendas.
- **calcular_total_vendas:** Este método deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

### Função main
Você deverá implementar a lógica para exibir o total de vendas utilizando o método `calcular_total_vendas` da classe `Relatorio`.

## Entrada
A entrada consiste em dados de vendas com as seguintes colunas:
- **Produto:** (string)
- **Quantidade:** (inteiro)
- **Valor:** (decimal)

## Saída
A saída é o total de vendas calculado pela classe `Relatorio`.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                  | Saída                  |
|------------------------------------------|------------------------|
| Notebook                                 |                        |
| 3                                        |                        |
| 1500.00                                  |                        |
| Mouse                                    |                        |
| 10                                       |                        |
| 50.00                                    |                        |
| Teclado                                  |                        |
| 5                                        |                        |
| 100.00                                   |Total de Vendas: 5500.0 |
|------------------------------------------|------------------------|
| Monitor                                  |                        |
| 2                                        |                        |
| 800.00                                   |                        |
| Webcam                                   |                        |
| 1                                        |                        |
| 120.00                                   |                        |
| Fone de Ouvido                           |                        |
| 4                                        |                        |
| 75.00                                    |Total de Vendas: 2020.0 |
|------------------------------------------|------------------------|
| Impressora                               |                        |
| 1                                        |                        |
| 350.00                                   |                        |
| Cartucho                                 |                        |
| 3                                        |                        |
| 60.00                                    |                        |
| Scanner                                  |                        |
| 2                                        |                        |
| 200.00                                   |Total de Vendas: 930.0  |



```python
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("Objeto fornecido não é uma instância da classe Venda.")

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # Calcule o total de vendas baseado nas vendas adicionadas:
            # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()

    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)

    # Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    print(f"Total de Vendas: {relatorio.calcular_total_vendas():.1f}")


if __name__ == "__main__":
    main()

```

     Notebook
     3
     1500.00
     Mouse
     10
     50.00
     Teclado
     5
     100.00


    Total de Vendas: 5500.0

[Voltar ao Índice](#indice)

# Desafio 4
<a name="desafio-4"></a>

# Agrupamento de Vendas por Categoria

**XP:** 37163/41323  
**NÍVEL:** 20  
**Nota:** 5/5  
**Dificuldade:** Intermediário  
**Área:** Estrutura de Dados  

## Descrição
Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe `Categoria` que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

## Tarefas

### 1. Método `adicionar_venda`
Na classe `Categoria`, crie um método chamado `adicionar_venda` que adiciona um objeto `Venda` à lista de vendas da categoria.

### 2. Método `total_vendas`
Na classe `Categoria`, crie um método chamado `total_vendas` que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

## Função `main`

### Entrada de Dados
Leia o nome das categorias e, para cada categoria, leia as vendas associadas.

### Implementação
Adicione cada venda à categoria correspondente usando o método `adicionar_venda`.

### Exibição dos Resultados
Exiba o total de vendas para cada categoria utilizando o método `total_vendas` para calcular e exibir o total das vendas.

## Entrada
A entrada consiste em:

- **Nome da Categoria** (string)
- **Lista de Vendas** (com as colunas Produto, Quantidade, Valor)

**Atenção:** O valor será o TOTAL GERAL de todos os produtos. Dessa forma:

**Exemplo:**

**Eletrônicos**
- Celular, 5, 1000  (Produto: Celular, 5 unidades, valor total: 1000)
- Fone de Ouvido, 10, 500  (Produto: Fone de Ouvido, 10 unidades, valor total: 500)

## Saída
A saída é o total de vendas por categoria.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                              | Saída                             |
|---------------------------------------------------------------------|-----------------------------------|
| Eletrônicos                                                         | Vendas em Eletrônicos: 1500.0    |
| Celular, 5, 1000                                                   |                                   |
| Fone de Ouvido, 10, 500                                            |                                   |
| Móveis                                                             | Vendas em Móveis: 1200.0         |
| Mesa, 2, 800                                                       |                                   |
| Cadeira, 4, 400                                                    |                                   |
|---------------------------------------------------------------------|-----------------------------------|
| Alimentos                                                          | Vendas em Alimentos: 340.0       |
| Arroz, 10, 200                                                     |                                   |
| Feijão, 7, 140                                                     |                                   |
| Jardinagem                                                         | Vendas em Jardinagem: 160.0      |
| Planta, 2, 60                                                      |                                   |
| Ferramentas, 1, 100                                               |                                   |
|---------------------------------------------------------------------|-----------------------------------|
| Livros                                                            | Vendas em Livros: 170.0           |
| Aventuras no Tempo, 1, 80                                          |                                   |
| Mistérios do Oceano, 2, 90                                         |                                   |
| Esportes                                                           | Vendas em Esportes: 330.0        |
| Tênis, 7, 210                                                      |                                   |
| Bola, 3, 120                                                       |                                   |



```python
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        # Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
        self.vendas.append(venda)

    def total_vendas(self):
        # Implementar o método total_vendas para calcular e retornar o total das vendas
        total = 0
        for venda in self.vendas:
            total += venda.valor
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2):
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)

    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # Exibir o total de vendas usando o método total_vendas:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas():.1f}")

if __name__ == "__main__":
    main()

```

     Eletrônicos
     Celular, 5, 1000
     Fone de Ouvido, 10, 500
     Móveis
     Mesa, 2, 800
     Ferramentas, 1, 100


    Vendas em Eletrônicos: 1500.0
    Vendas em Móveis: 900.0

---
[Voltar ao Índice](#indice)

# Desafio 5
<a name="desafio-5"></a>
# Fundamentos de Business Intelligence (BI)
XP 37723/41323
LEVEL 20
5/5
 Basic
 Princípios Básicos

## Descrição

Business Intelligence (BI) envolve o uso de ferramentas e técnicas para coletar, processar e analisar dados, com o objetivo de apoiar a tomada de decisões estratégicas em uma organização. Os conceitos fundamentais de BI incluem a integração de dados, armazenamento, análise e visualização. Complete o código associando os fundamentos de BI às suas respectivas descrições para entender melhor cada conceito e sua aplicação prática.

## Entrada

A entrada é um termo ou conceito relacionado aos fundamentos de BI para o qual você deve retornar a descrição. Os termos considerados são:

- ETL
- Data Warehousing
- Dashboard
- Data Mining

## Saída

A saída esperada é a descrição associada ao termo fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

- Armazenamento centralizado de dados para análise e relatórios.
- Processo de extrair, transformar e carregar dados de diversas fontes.
- Ferramenta visual para monitoramento e análise de métricas.
- Descoberta de padrões e insights em grandes conjuntos de dados.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
| --- | --- |
| ETL | Processo de extrair, transformar e carregar dados de diversas fontes. |
| Data Warehousing | Armazenamento centralizado de dados para análise e relatórios. |
| Dashboard | Ferramenta visual para monitoramento e análise de métricas. |

```python
def identificar_termo_bi(termo):
    if termo == "ETL":
        return "Processo de extrair, transformar e carregar dados de diversas fontes."
    elif termo == "Data Warehousing":
        return "Armazenamento centralizado de dados para análise e relatórios."
    elif termo == "Dashboard":
        return "Ferramenta visual para monitoramento e análise de métricas."
    elif termo == "Data Mining":
        return "Descoberta de padrões e insights em grandes conjuntos de dados."
    else:
        return "Termo não reconhecido"

entrada = input()

print(identificar_termo_bi(entrada))
```
ETL
Processo de extrair, transformar e carregar dados de diversas fontes.

---
[Voltar ao Índice](#indice)


# Desafio 6
<a name="desafio-6"></a>
# Fundamentos Sobre ETL
XP 37723/41323
LEVEL 20
5/5
 Basic
 Princípios Básicos

## Descrição

O processo ETL (Extract, Transform, Load) é uma etapa crítica em Business Intelligence que envolve a integração de dados provenientes de diferentes fontes para análises e relatórios. Cada etapa do processo ETL tem um papel específico na preparação dos dados para serem analisados. Complete o código associando os conceitos e etapas do processo ETL às suas respectivas descrições para entender como cada fase contribui para a análise de dados.

## Entrada

A entrada é um conceito ou etapa do processo ETL para o qual você deve retornar a descrição. Os conceitos considerados são:

- Extract
- Transform
- Load
- Data Integration

## Saída

A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

- Processo de coletar dados de diversas fontes.
- Processo de converter dados para um formato adequado.
- Carregamento de dados transformados em banco de dados ou warehouse.
- Unificação de dados provenientes de múltiplas fontes.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
| --- | --- |
| Extract | Processo de coletar dados de diversas fontes. |
| Transform | Processo de converter dados para um formato adequado. |
| Load | Carregamento de dados transformados em banco de dados ou warehouse. |

```python
# Função responsável por receber um conceito de ETL e retornar sua descrição.
def identificar_conceito_etl(conceito):
    if conceito == "Extract":
        return "Processo de coletar dados de diversas fontes."
    elif conceito == "Transform":
        return "Processo de converter dados para um formato adequado."
    elif conceito == "Load":
        return "Carregamento de dados transformados em banco de dados ou warehouse."
    elif conceito == "Data Integration":
        return "Unificação de dados provenientes de múltiplas fontes."
    else:
        return "Conceito não reconhecido"

entrada = input()

print(identificar_conceito_etl(entrada))
```
Extract
Processo de coletar dados de diversas fontes.

---
[Voltar ao Índice](#indice)
