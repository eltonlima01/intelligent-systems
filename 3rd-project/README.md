<div align="center">

# 3º PROJETO

| Disciplina | Semestre | Docente | Horário |
| :---: | :---: | :---: | :---: |
| PAM0466 - SISTEMAS INTELIGENTES | 2026.1 | PEDRO THIAGO VALÉRIO DE SOUZA | 3M23 4M45 |

| Discente | Matrícula |
| :---: | :---: |
| ELTON CAIO VIEIRA DE LIMA | 2020010673 |
| LUCAS VIERES ARAÚJO FARIAS | 2025022531 |
</div>

## INTRODUÇÃO E CONTEXTO

A indústria vinícola depende historicamente de avaliações humanas — caras, lentas e subjetivas. Um modelo preditivo de qualidade tem aplicações diretas no controle de lotes antes do engarrafamento, na precificação e na certificação de denominação de origem por ́orgãos reguladores. Na pesquisa enológica (ciência que estuda a produção, conservação e análise de vinhos), ele também ajuda a identificar quais variáveis químicas mais influenciam a percepção de qualidade, orientando decisões de produção.

Plataformas como a Vivino (https://www.vivino.com/BR/pt-BR/) já utilizam *machine learning* com esse objetivo. No Brasil, o contexto do Vale do São Francisco — maior polo de vinhos tropicais do mundo, localizado aqui no Nordeste — torna o problema especialmente próximo e motivador para nossa realidade.

Neste projeto, você é convidado a construir um modelo de classificação de vinhos em três categorias de qualidade (baixa, média e alta) a partir de um conjunto de dados químicos utilizando o 𝑘-NN (*k-Nearest Neighbors*).

## CONJUNTO DE DADOS

O projeto utiliza o arquivo winequality-red.csv do *dataset* Wine Quality (https://archive.ics.uci.edu/ml/datasets/Wine+Quality). O *dataset* foi criado por Paulo Cortez et al. (Universidade do Minho, Portugal) e publicado em 2009. Ele reúne 1.599 amostras de vinho tinto da região do Vinho Verde, no noroeste de Portugal. Cada amostra foi submetida a testes laboratoriais que geraram 11 atributos físico-químicos — como acidez fixa, acidez volátil, teor de ácido cítrico, açúcar residual, cloretos, dióxido de enxofre, densidade, pH, sulfatos e teor alcoólico. O rótulo de qualidade (quality)  ́e um valor inteiro de 0 a 10 atribuído por *sommeliers* em avaliações cegas, representando a mediana de pelo menos três avaliações humanas.

## [ATIVIDADES](/3nd-project/main.ipynb)