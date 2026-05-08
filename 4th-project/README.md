<div align="center">

# 4º PROJETO

| Disciplina | Semestre | Docente | Horário |
| :---: | :---: | :---: | :---: |
| PAM0466 - SISTEMAS INTELIGENTES | 2026.1 | PEDRO THIAGO VALÉRIO DE SOUZA | 3M23 4M45 |

| Discente | Matrícula |
| :---: | :---: |
| ELTON CAIO VIEIRA DE LIMA | 2020010673 |
| LUCAS VIERES ARAÚJO FARIAS | 2025022531 |
</div>

## INTRODUÇÃO E CONTEXTO

A ionosfera é a camada da atmosfera terrestre que se estende de aproximadamente 60 a 1.000 km de altitude e é fortemente ionizada pela radiação solar. Seu monitoramento contínuo é essencial para aplicações de telecomunicações, navegação por GPS e previsão de tempestades geomagnéticas. Sistemas de radar de alta frequência (HF) são utilizados para sondar essa camada: pulsos de rádio são emitidos em direção à ionosfera e os sinais refletidos são analisados para determinar se a estrutura ionosférica está bem definida ou não.

O Brasil ocupa uma posição geograficamente privilegiada e ao mesmo tempo desafiadora. O país está situado sobre a Anomalia de Ionização Equatorial, uma região onde a estrutura da ionosfera é altamente irregular e sujeita a perturbações intensas. Neste projeto, você implementará uma Rede Adaline para classificar automaticamente retornos de radar ionosférico, distinguindo sinais que indicam a presença de estrutura eletrônica coerente na ionosfera daqueles que não a indicam.

O projeto utiliza o *dataset* Ionosphere, disponível no repositório UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Ionosphere). O conjunto foi coletado pelo sistema de radar Goose Bay, no Labrador (Canadá), e contribuído por Vince Sigillito do Laboratório de Física Aplicada da Universidade Johns Hopkins. Ele contém 351 amostras de retornos de radar, cada uma descrita por 34 atributos contínuos correspondentes a valores complexos obtidos pela autocorrelação de pulsos de radar emitidos por antenas separadas em fase. O rótulo binário indica se o retorno é *good* (estrutura ionosférica detectada, classe +1) ou *bad* (sem estrutura coerente, ou seja, os raios atravessam a ionosfera, classe −1). Do total de amostras, 225 são da classe *good* e 126 da classe *bad*.

## [ATIVIDADES](/4th-project/main.ipynb)