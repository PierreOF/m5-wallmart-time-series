# Previsão de Vendas da Base M5 do Walmart

Este repositório contém a análise e previsão das séries temporais da base de vendas de produtos M5 do Walmart. Utilizando a biblioteca Nixtla, a previsão é feita para diferentes categorias, como produtos, estados, valor e lojas.

## Análise do Projeto X
 - Foi observado uma falha na divisão de dados para treino e teste. Para séries temporais o ideal seria dividir os dados de teste com 6 meses os dados , estava (80% para treino e 20% para teste)

## Análise do Projeto Y
 - Foi observado uma falha na divisão de dados para treino e teste. Para séries temporais o ideal seria dividir os dados de teste com 6 meses os dados , estava (80% para treino e 20% para teste)
 - Realizaram Forecasting de todas as séries de uma vez. 
 - Poderiam dividir melhor as células de código (organização).
 - (Remoção de outliers) - É recomendável tentar entender o padrão por trás daquela variação dos dados .
 - Casos que não são adequados de fazer a remoção de outliers
   1 - Sazonalidades - Ex : mês de dezembro ter uma alta de venda comparado a outros meses. 
   2 - Promoções - Ex : a loja costuma fazer promoções e por isso as vendas daquele mês foram mais altos do que em outros meses 
   
## Descrição

Os notebooks neste repositório fazem previsões de séries temporais usando a biblioteca Nixtla e seguem a metodologia CRISP-DM. A base de dados M5 do Walmart é amplamente utilizada em competições de previsão, contendo informações detalhadas sobre vendas de produtos ao longo do tempo.

## Metodologia

### CRISP-DM

CRISP-DM (Cross Industry Standard Process for Data Mining) é uma metodologia padrão para mineração de dados. As etapas incluem:

1. **Entendimento do Negócio:** Compreensão dos objetivos e requisitos do negócio.
2. **Entendimento dos Dados:** Coleta inicial de dados para familiarização.
3. **Preparação dos Dados:** Limpeza e transformação dos dados para análise.
4. **Modelagem:** Aplicação de técnicas de modelagem para criar modelos preditivos.
5. **Avaliação:** Avaliação dos modelos para garantir que atendem aos objetivos do negócio.
6. **Desdobramento:** Implementação dos modelos em um ambiente de produção.

![CRISP-DM](https://miro.medium.com/v2/resize:fit:988/0*tA5OjppLK627FfFo)

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas principais:

- **models:** Contém os modelos em pkl.
- **notebooks:** Diretório principal contendo os notebooks de previsão e EDA.
  - 1. **N1 - EDA (Análise Exploratória de Dados)**
     - Explora e visualiza a base de dados M5, fornecendo insights iniciais sobre as séries temporais.
  
  - 2. **N2 - Previsão por Lojas**
     - Realiza a previsão das vendas com base nas lojas.

  - 3. **N3 - Previsão por Produtos**
     - Realiza a previsão das vendas com base nos produtos.

  - 4. **N4 - Previsão por Valor**
     - Realiza a previsão das vendas com base no valor.

  - 5. **N5 - Previsão por Estados**
     - Realiza a previsão das vendas com base nos estados.
  
- **preds:** Diretório com os resultados das previsões dos modelos.
- **scripts:** Diretório com os scripts em python.


  
## Bibliotecas Utilizadas

- **Nixtla**: Biblioteca principal utilizada para a previsão de séries temporais.
- **Pandas**: Utilizada para manipulação e análise de dados.
- **NumPy**: Utilizada para operações numéricas.
- **Holidays**: Para entender as vendas por feriados
