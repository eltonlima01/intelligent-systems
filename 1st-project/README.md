<div align="center">

# 1º PROJETO

| Disciplina | Semestre | Docente | Horário |
| :---: | :---: | :---: | :---: |
| PAM0466 - SISTEMAS INTELIGENTES | 2026.1 | PEDRO THIAGO VALÉRIO DE SOUZA | 3M23 4M45 |

| Discente | Matrícula |
| :---: | :---: |
| ELTON CAIO VIEIRA DE LIMA | 2020010673 |
| LUCAS VIERES ARAÚJO FARIAS | 2025022531 |
</div>

## INTRODUÇÃO E CONTEXTO

Uma usina termoelétrica de ciclo combinado (UTCC) é uma instalacão de alta eficiência que combina turbinas a gás e a vapor para gerar eletricidade. Ela reaproveita o calor dos gases de exaustão da turbina a gás (ciclo Brayton) para produzir vapor em uma caldeira, acionando uma segunda turbina (ciclo Rankine), aumentando significativamente o rendimento. A principal vantagem é a eficiência energética, que pode chegar a 60%,
reduzindo as emissões de gases de efeito estufa.

Embora apresente alta eficiência, o principal desafio técnico no uso de uma usina UTCC reside na integracão, sincronizacão e operacão conjunta de dois ciclos termodinâmicos distintos (ciclo Brayton e ciclo Rankine) para funcionar de forma eficiente. Assim sendo, a potência elétrica de saída (PE) é altamente sensível às condicões ambientais.

Neste projeto, você deve construir um modelo matemático de regressão linear múltipla para prever a producão de energia baseando-se em sensores ambientais, permitindo a otimizacão do despacho energético.

## CONJUNTO DE DADOS

Para realizar o treinamento do nosso modelo, utilizamos o dataset UCI CCPP (disponível em https://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant). O dataset contém 9.568 amostras coletadas ao longo de 6 anos. Cada amostra possui as seguintes variáveis:

- AT (*Ambient Temperature*): Temperatura em °C. Afeta a densidade do ar e a eficiência da combustão.
- V (*Exhaust Vacuum*): Vácuo de escape em cm Hg. Relacionado à pressão na turbina a vapor.
- AP (*Ambient Pressure*): Pressão atmosférica em mbar.
- RH (*Relative Humidity*): Umidade relativa em percentagem.
- PE (*Net Hourly Electrical Energy Output*): A variável alvo em MW (MegaWatts).

## [ATIVIDADES](/1st-project/main.ipynb)