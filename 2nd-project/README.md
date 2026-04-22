<div align="center">

# 2º PROJETO

| Disciplina | Semestre | Docente | Horário |
| :---: | :---: | :---: | :---: |
| PAM0466 - SISTEMAS INTELIGENTES | 2026.1 | PEDRO THIAGO VALÉRIO DE SOUZA | 3M23 4M45 |

| Discente | Matrícula |
| :---: | :---: |
| ELTON CAIO VIEIRA DE LIMA | 2020010673 |
| LUCAS VIERES ARAÚJO FARIAS | 2025022531 |
</div>

## INTRODUÇÃO E CONTEXTO

Doenças cardiovasculares são a principal causa de morte no mundo, responsáveis por cerca de 18 milhões de óbitos por ano segundo a OMS. O diagnóstico precoce é determinante para o sucesso do tratamento. Existe, portanto, uma necessidade real de ferramentas capazes de estimar o risco de um paciente com base em dados clínicos simples, coletados em consulta de rotina. É nesse contexto que o aprendizado de máquina pode contribuir. Um modelo de classificação treinado com dados históricos de pacientes diagnosticados é capaz de aprender quais combinações de variáveis clínicas estão associadas à presença de doença cardíaca e aplicar esse aprendizado a novos pacientes.

Neste projeto, você é convidado a construir um modelo utilizando regressão logística para prever a presença de doença cardíaca com base em um conjunto de dados clínicos.

## CONJUNTO DE DADOS

O projeto utiliza o dataset Heart Disease Cleveland (UCI Machine Learning Repository – disponı́vel em https://archive.ics.uci.edu/dataset/45/heart+disease), com registros de 303 pacientes e 13 variáveis clínicas. Os diagnósticos foram confirmados por cateterismo cardíaco, o que garante rótulos confiáveis. As variáveis incluem:

- age — idade do paciente em anos;
- sex — sexo biológico (1 = masculino, 0 = feminino);
- cp — tipo de dor no peito: angina tı́pica (1), atı́pica (2), não anginosa (3) ou assintomático (4);
- trestbps — pressão arterial em repouso em mmHg;
- chol — colesterol sérico total em mg/dl;
- fbs — glicemia em jejum acima de 120 mg/dl (1 = sim, 0 = não);
- restecg — resultado do ECG em repouso: normal (0), alteração na onda ST-T (1) ou hipertrofia ventricular (2);
- thalach — frequência cardı́aca máxima atingida no teste de esforço;
- exang — angina induzida por exercı́cio (1 = sim, 0 = não);
- oldpeak — depressão do segmento ST durante o esforço, indicador de isquemia;
- slope — inclinação do segmento ST no pico do esforço: ascendente (1), plano (2) ou descendente (3);
- ca — número de artérias coronárias com obstrução visı́vel na fluoroscopia (0 a 3);
- thal — cintilografia de tálio: normal (3), defeito fixo / infarto prévio (6) ou defeito reversı́vel / isquemia
ativa (7);

A saı́da é a variável target, que indica o diagnóstico original de 0 a 4, binarizado para 0 (sem doença) e 1
(com doença) antes do treinamento.

## [ATIVIDADES](/2nd-project/main.ipynb)