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

<img width="1920" height="1080" alt="Visual Chart Page Iteration 6" src="https://github.com/user-attachments/assets/db5bcd72-7b5c-4c38-9d5c-44a3b9669f0a" />


#### 4.1.3. Planejamento Geral da Solução

O modelo é alimentado por uma base de dados de pagadores com vencimentos em maio, contendo informações históricas de boletos, status de liquidação, datas de vencimento, bancos emissores, endereços dos devedores, dados dos recebedores, além do histórico de interações entre pagadores e a instituição, como número e data dos contactações.
Com essa base de dados estabelecida o modelo propõe fornecer ao cliente utilizador do serviço, dados de predição que auxiliem na tomada de ações sobre inadimplência, como o score de risco de inadimplência, tendência de pagamento das cobranças, previsão de valores de recebimento dentro do período e a melhor janela de pagamento provável.
A solução será oferecida inicialmente como uma **POC (Prova de Conceito)** para integração em plataformas de emissão de cobranças e gestão de recebíveis de instituições financeiras ou com alto volume de pagadores . O produto será disponibilizado por um script em python, para que gestores financeiros possam acessar os insights preditivos diretamente em seu fluxo de trabalho. Futuramente, o objetivo é incorporar a solução de forma nativa dentro do ecossistema digital da empresa, permitindo automações baseadas nas predições e visualizações em tempo real.

Benefício esperados da solução:
- **Redução do risco de inadimplência**, permitindo aos gestores anteverem possíveis atrasos ou não pagamentos.
- **Aumento da eficiência operacional**, ao permitir uma priorização mais estratégica de cobranças e renegociações.
- **Melhor previsibilidade de fluxo de caixa**, com projeções de recebimentos mais assertivas.
- **Aprimoramento da comunicação com o cliente final**, com base na análise de histórico de pagamentos e interações.
- **Valor agregado à plataforma da parceira, destacando a empresa como fornecedora de soluções financeiras com inteligência preditiva de ponta.

O sucesso da solução será medido por meio dos seguintes critérios:
- **Acurácia das predições**: Porcentagem de assertividade nas projeções de inadimplência satisfatória, conforme métricas definidas durante o desenvolvimento.
- **Usabilidade e aderência**: validação positiva por parte dos stakeholders e usuários-chave (gerentes financeiros e coordenadores de contas a receber) durante testes e apresentações.
- **Relevância dos insights**: feedback qualitativo dos usuários demonstrando utilidade prática para tomadas de decisão reais.
- **Viabilidade de escalabilidade**: capacidade técnica de aplicar o modelo a diferentes clientes e setores com níveis mínimos de customização.
- **Níveis de segurança compatíveis com a LGPD**: o tratamento de dados pessoais deverá respeitar os princípios da Lei Geral de Proteção de Dados (LGPD)


#### 4.1.4. Value Proposition Canvas
```
Posicione aqui seu canvas.

Remova este bloco ao final
```

#### 4.1.5. Matriz de Riscos

![Matriz de riscos](../assets/Matriz_de_risco.png)

##### **Ameaças**:

1. **Previsão imprecisa do fluxo de recebimentos**:

A projeção incorreta do fluxo de caixa pode comprometer diretamente a saúde financeira dos clientes da Finnet, afetando decisões como pagamentos de fornecedores, funcionários, dívidas e investimentos. Uma previsão mal calibrada pode levar a déficits operacionais ou má alocação de recursos.

2. **Erro significativo no score de inadimplência**:

O score de risco de inadimplência orienta decisões cruciais, como concessão de crédito ou prazos de pagamento. Altas taxas de erro neste indicador podem gerar perdas financeiras relevantes, sobretudo em setores onde o risco de crédito é fator-chave, como instituições financeiras, empresas de cobrança e consórcios.

3. **Janela de pagamento subótima**:

Indicar uma janela de pagamento que não considera o comportamento real ou a rotina financeira do devedor (como a data de recebimento de salário) pode reduzir as chances de recebimento, comprometendo a eficácia da cobrança.

4. **Tendência de pagamento classificada incorretamente**:

Uma categorização equivocada do pagador como “em dia”, “com atraso” ou “inadimplente” pode distorcer o perfil de risco atribuído, gerando decisões inadequadas de cobrança ou concessão de crédito.

5. **Dependência excessiva de dados históricos**:

Modelos preditivos baseados unicamente em dados históricos podem falhar diante de mudanças no contexto econômico, comportamental ou regulatório. Essa limitação afeta a capacidade de adaptação do sistema a novos padrões de comportamento dos pagadores.

6. **Baixa aceitação ou adoção da funcionalidade**:

Mesmo que os modelos estejam tecnicamente corretos, a falta de transparência, explicabilidade ou integração com os fluxos do cliente pode gerar desconfiança e baixa adoção. Isso limita o valor percebido da funcionalidade e reduz o impacto do projeto.

7. **Qualidade e atualização insuficiente da base de dados**:

Informações desatualizadas, incompletas ou fora da distribuição esperada comprometem a qualidade das análises geradas. A confiabilidade dos insights depende diretamente da integridade e frescor dos dados utilizados.

##  Oportunidades

1. **Melhorar a previsão de inadimplência para reduzir perdas**  
É o objetivo central da POC. Com bons dados, a previsão de inadimplência evita perdas financeiras diretas para os clientes, agregando valor imediato à solução.

2. **Aumentar a eficiência na cobrança (agindo no momento certo)**  
Com uma boa previsão, é possível antecipar ações de cobrança no momento ideal, o que aumenta a taxa de sucesso no recebimento.

3. **Facilitar a tomada de decisão dos gestores financeiros**  
Um dashboard simples com insights preditivos já melhora significativamente a rotina e o desempenho dos gestores financeiros.



4. **Melhorar a satisfação dos clientes por oferecer informações mais úteis**  
Entregar dados preditivos relevantes aumenta o valor percebido da solução e contribui para uma melhor experiência de uso.

5. **Melhoria de processos internos**  
A própria Finnet pode aplicar os resultados da POC para otimizar seus produtos e processos. A aplicação é simples, mas o impacto é mais localizado.


6. **Diferenciação competitiva no mercado de gestão de recebíveis**  
Caso a solução final seja bem posicionada e entregue resultados sólidos, a Finnet pode se destacar no mercado por oferecer recursos preditivos avançados.

7. **Atrair novos clientes interessados em ferramentas preditivas**  
Com a entrega de uma solução robusta e inovadora, existe potencial para gerar novas oportunidades comerciais, especialmente com empresas que valorizam inteligência de dados.


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
