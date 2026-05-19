<div align="center">

# 5º PROJETO

| Disciplina | Semestre | Docente | Horário |
| :---: | :---: | :---: | :---: |
| PAM0466 - SISTEMAS INTELIGENTES | 2026.1 | PEDRO THIAGO VALÉRIO DE SOUZA | 3M23 4M45 |

| Discente | Matrícula |
| :---: | :---: |
| ELTON CAIO VIEIRA DE LIMA | 2020010673 |
| LUCAS VIERES ARAÚJO FARIAS | 2025022531 |

</div>

## INTRODUÇÃO E CONTEXTO

A segurança de redes de computadores é um dos desafios centrais da infraestrutura digital moderna. Ataques como negação de serviço (*DoS*), varredura de portas (*Probe*) e acesso remoto não autorizado (*R2L*) causam prejuízos bilionários anualmente e comprometem desde sistemas corporativos até infraestruturas críticas de energia, saúde e comunicações. Sistemas de Detecção de Intrusão (*IDS — Intrusion Detection Systems*) são a principal linha de defesa ativa contra essas ameaças, e a automação dessa detecção por meio de aprendizado de máquina representa a fronteira atual da área.

As características de um ataque *DoS* se misturam às do tráfego legítimo em regiões do espaço de atributos que nenhuma linha reta consegue separar adequadamente. Assim sendo, uma rede Perceptron não é capaz de solucionar esse problema. Assim sendo, o Perceptron Multicamadas (*MLP — Multilayer Perceptron*), com suas camadas ocultas e funções de ativação não-lineares, supera essa limitação, tornando-se uma escolha natural para este tipo de problema.

Neste projeto, você é convidado a construir e treinar uma rede MLP utilizando o PyTorch para classificar conexões de rede como normais ou ataques, a partir de atributos extraídos de pacotes de rede.

## CONJUNTO DE DADOS

O projeto utiliza o *dataset* NSL-KDD (https://www.kaggle.com/datasets/hassan06/nslkdd), disponibilizado pelo Canadian Institute for Cybersecurity da Universidade de New Brunswick. O NSL-KDD é uma versão refinada do histórico KDD Cup 1999.

O conjunto disponibiliza dois arquivos: KDDTrain+.txt (125.973 amostras) e KDDTest+.txt (22.544 amostras). Cada registro representa uma conexão de rede e possui 41 atributos divididos em três grupos: (i) básicos — duração, protocolo (`protocol type`), serviço (`service`), *flag* de estado da conexão (`flag`), bytes transferidos etc.; (ii) de conteúdo — número de tentativas de *login* com falha, acesso a arquivos sensíveis, comandos executados em sessões shell etc.; (iii) de tráfego — estatísticas das últimas conexões ao mesmo host e ao mesmo serviço, como taxa de erros SYN e taxa de conexões rejeitadas. Dos 41 atributos, 38 são numéricos e 3 são categóricos (`protocol type`, `service` e `flag`).

O rótulo original possui 23 tipos de ataque agrupados em 4 categorias (*DoS*, *Probe*, *R2L*, *U2R*) além da classe *normal*; neste projeto, o problema será tratado como classificação binária: 0 para conexão normal e 1 para qualquer tipo de ataque.

## [ATIVIDADES](/5th-project/notebooks/main.ipynb)