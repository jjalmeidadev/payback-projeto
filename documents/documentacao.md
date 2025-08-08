# Documentação Modelo Preditivo - Inteli

```
INSTRUÇÕES GERAIS (remova este trecho ao final)

Você deve editar este documento utilizando notação markdown - siga as convenções neste link 
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
```

## Nome da Solução
### Nome do grupo
#### (preencha aqui os nomes dos integrantes, em ordem alfabética, separados por vírgula)

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)


## <a name="c1"></a>1. Introdução

  A Finnet é uma empresa brasileira de médio porte, com um quadro de 201 a 500 colaboradores, que se destaca no mercado de tecnologia financeira pela sua capacidade de oferecer soluções inovadoras e adaptáveis às necessidades do ambiente corporativo. Com o slogan “Somos tecnologia. Multibanco. Integração.”, a companhia atua no desenvolvimento de tecnologias que simplificam e automatizam processos financeiros, promovendo maior eficiência operacional para seus clientes. Sua atuação concentra-se em áreas como Gestão Financeira e Conciliação Bancária, Cobranças, Boletos e Meios de Pagamento, além de Conectividade Financeira por meio de EDI e RPA. Com base nesses segmentos, a Finnet se posiciona como uma TechFin B2B, especializada em soluções que promovem a automação, a integração e a digitalização das rotinas financeiras de empresas de médio e grande porte.

  Nesse contexto, um dos principais desafios enfrentados por seus clientes, e que impacta diretamente o trabalho da própria Finnet, é o aumento da inadimplência no mercado nacional. Esse fenômeno compromete a saúde financeira e a previsibilidade de receita de médias e grandes empresas, dificultando o planejamento estratégico e a tomada de decisões. Além disso, a ausência de dados estruturados, como o histórico de pagamentos e o impacto da inadimplência no fluxo de caixa, prejudica o monitoramento de riscos e a definição de ações corretivas. Para a Finnet, esse cenário representa uma limitação relevante, já que a fragmentação e a complexidade das informações restringem a capacidade de fornecer análises mais aprofundadas, dificultando o apoio efetivo à gestão financeira de seus clientes.

## <a name="c2"></a>2. Objetivos e Justificativa
### 2.1 Objetivos
```
Descreva resumidamente os objetivos gerais e específicos do seu parceiro de negócios.

Remova este bloco ao final
```

### 2.2 Proposta de solução
```
Descreva resumidamente sua proposta de modelo preditivo e como esse modelo pretende resolver o problema, atendendo os objetivos.

Remova este bloco ao final
```

### 2.3 Justificativa
```
Faça uma breve defesa de sua proposta de solução, escreva sobre seus potenciais, seus benefícios e como ela se diferencia.

Remova este bloco ao final
```

## <a name="c3"></a>3. Metodologia
```
Descreva a metodologia CRISP-DM e suas etapas de desenvolvimento, citando o referencial teórico. Você deve apenas enunciar os métodos, sem dizer ainda como eles foram aplicados, nem quais resultados foram obtidos.

Remova este bloco ao final
```

## <a name="c4"></a>4. Desenvolvimento e Resultados
### 4.1. Compreensão do Problema
#### 4.1.1. Contexto da indústria 
## Concorrentes
A Finnet disputa mercado com empresas como **Vindi**, focada em cobrança recorrente; **CobreBemX**, especializada em gestão de boletos e integrações bancárias; e **Celero**, que automatiza rotinas como contas a pagar e conciliação. Também enfrenta concorrência de plataformas como **Asaas** e **Iugu**, que oferecem soluções SaaS voltadas à gestão financeira e integração bancária. No entanto, a Finnet se diferencia por oferecer um portfólio mais amplo e técnico, voltado a empresas de médio e grande porte com alto volume de transações.

---

## Modelo de Negócio
  A Finnet desenvolve soluções **SaaS** (Software as a Service) para automatizar e integrar processos financeiros empresariais, como:
  
- Cobrança de clientes
- Pagamento de contas
- Conciliação bancária
- Antecipação de recebíveis  

Tudo isso funciona integrado aos bancos por meio de tecnologia própria (**API, EDI e RPA**).

---

## Tendências do Setor
O setor avança com o fortalecimento do **Open Finance**, uso **Pix** para transações empresariais e adoção de **IA** para análise preditiva. Além disso, o avanço da regulação do **Banco Central** impulsiona empresas com forte governança e capacidade de integração com sistemas bancários. 
Assim, as empresas buscam soluções seguras, integradas e inteligentes para melhorar a previsibilidade financeira, reduzir inadimplência e aumentar a eficiência de seus serviços.

---

## Forças de Porter

### Ameaça de novos entrantes
**Média** – Embora o setor atraia startups, a entrada de novos concorrentes é dificultada por barreiras como exigência regulatória (autorização como ITP), integração bancária robusta e investimentos em cibersegurança.

### Poder de negociação dos fornecedores
**Baixo** – A Finnet desenvolve suas soluções utilizando tecnologia própria (API, EDI, RPA) e depende pouco de fornecedores externos, reduzindo o poder de barganha deles.

### Poder de negociação dos compradores
**Alto** – Os clientes da Finnet são empresas com grande volume de transações, o que lhes dá força para negociar preços, SLA de atendimento e personalização de serviços.

### Ameaça de produtos substitutos
**Média** –Algumas empresas ainda utilizam planilhas ou ERPs generalistas, mas estes não oferecem o mesmo nível de automação, integração bancária ou controle de risco, o que torna a substituição limitada a casos de baixa complexidade.

### Rivalidade entre concorrentes existentes
**Média** – A Finnet enfrenta concorrência de empresas que oferecem soluções financeiras específicas com propostas de valor enxutas e escaláveis. Ainda assim, sua abordagem mais completa e técnica reduz a sobreposição direta com muitos concorrentes.

#### 4.1.2. Análise SWOT 

<img width="707" height="383" alt="Análise SWOT" src="https://github.com/user-attachments/assets/5f10062d-b64e-4e66-b27d-83cd5ecb03f3" />

#### 4.1.3. Planejamento Geral da Solução
```
a) quais os dados disponíveis (fonte e conteúdo - exemplo: dados da área de Compras da empresa descrevendo seus fornecedores).
b) qual a solução proposta (pode ser um resumo do texto da Seção 2.2).
c) como a solução proposta deverá ser utilizada.
d) quais os benefícios trazidos pela solução proposta.
e) qual será o critério de sucesso.

Remova este bloco ao final
```

#### 4.1.4. Value Proposition Canvas

&nbsp;&nbsp;&nbsp;&nbsp; Com objetivo de alinhar a oferta do produto ou serviço com as necessidades e expectativas da Finnet, foi desenvolvido o Canva Proposta de Valor da solução. Ele visa assegurar que a equipe entregue valor genuíno, compreendendo profundamente o perfil do cliente e como a proposta resolve suas dores e proporciona ganhos reais para a empresa parceira.

<div align="center">
<sub>Figura 1: Canva Proposta de Valor.</sub>
</div>
<div align="center">
<img src="../assets/CanvaValue.png">
</div>

<div align="center">
<sub>Fonte: Material produzido pela equipe, 2025.</sub>
</div>

Através da análise realizada pela equipe, identificamos que a solução deve entregar como:

#### Solução

##### Produtos e Serviços

Uma POC integrada à plataforma de cobranças Finnet que fornece, com base em dados fornecidos pelo parceiro:

- Score de risco de inadimplência.

- Projeção de inadimplência (% e valores) por período

- Tendência de pagamento (em dia, atraso, inadimplente).

- Melhor data de vencimento para cada pagador.

- Projeção de recebimentos no período analisado.

Essas informações devem ser geradas por meio de uma Inteligência Artificial preditiva, capaz de analisar os dados dos clientes da Finnet, identificar padrões comportamentais e entregar as estatísticas solicitadas pelo parceiro.


##### Aliviadores de Dores

- Automatização da análise de risco, comportamento de pagamento.
- Redução do tempo e esforço necessários para análise de inadimplência e dados recebidos.
- Melhora nas decisões e estratégias de cobrança.
- Apoio na negociação de prazos e decisões financeiras baseadas em dados reais.

##### Criadores de Ganhos

- Melhora nas datas de vencimento.
- Maior autonomia e assertividade do time financeiro na tomada de decisões.
- Melhora na projeção de recebimentos.
- Otimização das estratégias de cobrança.

#### Empresa

##### Dores

- Dificuldade na tomada de decisões em relação a inadimplência, um  problema crescente no mercado nacional.
- Falta de informações sobre tendência de pagamento causam impacto no fluxo de recebimentos das instituições parceira.
- Decisões pouco embasadas sobre prazos e estratégias de cobrança.
- Alto tempo gasto para analisar dados de recebíveis.

##### Ganhos

- Maior estabilidade e previsibilidade financeira.
- Melhor janela para vencimento e cobrança.
- Redução de inadimplência.
- Proporcionar autonomia na tomada de decisões ao gestor da área financeira.
- Adicionar valor ao produto oferecido ao mercado.
- Aumento dos pagamentos em dia.

##### Tarefas do Cliente

- Melhorar a projeção de recebimentos.
- Ajustar datas de vencimento com base em dados.
- Prever inadimplência de clientes/pagadores.
- Estar informado sobre a tendência de pagamento, para evitar impacto no fluxo de recebimentos.







#### 4.1.5. Matriz de Riscos
```
Posicione aqui sua matriz.

Remova este bloco ao final
```

#### 4.1.6. Personas
```
Posicione aqui suas Personas (indique se são personas que utilizam o modelo e/ou se são afetadas pelo modelo).

Remova este bloco ao final
```

#### 4.1.7. Jornadas do Usuário
```
Posicione aqui seus mapas de jornadas do usuário que utiliza o modelo.

Remova este bloco ao final
```

#### 4.1.8 Política de Privacidade
```
Posicione aqui sua política de privacidade em acordo com a LGPD

Remova este bloco ao final
```

### 4.2. Compreensão dos Dados

#### 4.2.1. Exploração de dados
```
Apresentar a estatística descritiva básica de cada coluna, identificar se a coluna é numérica ou categórica e pelo menos 3 gráficos para visualizar a relação entre colunas escolhidas pelo grupo.

Remova este bloco ao final
```

#### 4.2.2. Pré-processamento dos dados
```
Apresentar quais foram as ações realizadas de limpeza (tratamento de missing values e remoção de outliers) e transformação (normalização e codificação) das colunas. Se houverem outliers, cite quais são e qual(is) correção(ões) será(ão) aplicada(s).

Remova este bloco ao final
```

#### 4.2.3. Hipóteses
```
Descreva três hipóteses sobre a relação dos dados e o problema. Justifique cada uma delas. 

Remova este bloco ao final
```

### 4.3. Preparação dos Dados e Modelagem
```
Caso seu projeto seja Modelo Supervisionado, apresentar: 
a) Organização dos dados (conjunto de treinamento, validação e testes)
b) Modelagem para o problema (proposta de features com a explicação completa da linha de raciocínio).
c) Métricas relacionadas ao modelo (pelo menos 3).
d) Apresentar o primeiro modelo candidato, e uma discussão sobre os resultados deste modelo (discussão sobre as métricas para esse modelo candidato).

Caso seu projeto seja Modelo Não-Supervisionado, apresentar:
a) Modelagem para o problema (proposta de features com a explicação completa da linha de raciocínio).
b) Primeiro modelo candidato para o problema.
c) Justificativa para a definição do K do modelo.
d) Escolha de um tipo de sistema de recomendação e a justificativa para essa escolha.

Remova este bloco ao final
```

### 4.4. Comparação de Modelos
```
- Descrever e justificar a escolha da métrica de avaliação dos modelos com base no que é mais importante para o problema ao 
  se medir a qualidade desses modelos;
- Descrever ao menos três modelos candidatos, seus respectivos algoritmos, seus tunings de hiperparâmetros e suas métricas 
  alcançadas;

Remova este bloco ao final
```

### 4.5. Avaliação
```
- Descreva a solução final de modelo preditivo e justifique a escolha. Alinhe sua justificativa com a Seção 4.1, resgatando o entendimento 
  do negócio e das personas, explicando de que formas seu modelo atende os requisitos e definições. 
- Descreva também um plano de contingência para os casos em que o modelo falhar em suas predições.
- Além disso, discuta sobre a explicabilidade do modelo (se aplicável) e realize a verificação de aceitação ou refutação das hipóteses.
- Se aplicável, utilize equações, tabelas e gráficos de visualização de dados para melhor ilustrar seus argumentos. 

Remova este bloco ao final
```

## <a name="c5"></a>5. Conclusões e Recomendações
```
Escreva, de forma resumida, sobre os principais resultados do seu projeto e faça recomendações formais ao seu parceiro de negócios em relação ao uso desse modelo. Você pode aproveitar este espaço para comentar sobre possíveis materiais extras, como um manual de usuário mais detalhado na seção “Anexos”. Não se esqueça também das pessoas que serão potencialmente afetadas pelas decisões do modelo preditivo e elabore recomendações que ajudem seu parceiro a tratá-las de maneira estratégica e ética. 

Remova este bloco ao final
```

## <a name="c6"></a>6. Referências
```
Incluir as principais referências de seu projeto, para que seu parceiro possa consultar caso ele se interessar em aprofundar. Não se esqueça de formatar as referências conforme a ABNT.

Remova este bloco ao final
```

## <a name="attachments"></a>Anexos
```
Utilize esta seção para anexar materiais como manuais de usuário, documentos complementares que ficaram grandes e não couberam no corpo do texto etc.

Remova este bloco ao final
```
