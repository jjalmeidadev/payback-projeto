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
O setor financeiro avança com o fortalecimento do **Open Finance**, que amplia o acesso e compartilhamento seguro de dados, e com o uso crescente do **Pix** para agilizar transações empresariais. A adoção da **inteligência artificial (IA)** para análise preditiva tem aprimorado a gestão de riscos e a tomada de decisões. Paralelamente, as novas regulamentações do Banco Central estimulam empresas a investirem em governança sólida e em sistemas integrados que se conectam de forma eficiente ao ambiente bancário.

Diante desse cenário, as empresas buscam cada vez mais soluções seguras, integradas e inteligentes, visando melhorar a previsibilidade financeira, reduzir a inadimplência e otimizar a eficiência dos seus serviços, acompanhando as demandas do mercado e a evolução tecnológica.

---

## 5 Forças de Porter

As 5 forças de Porter são um framework estratégico utilizado para analisar o setor em que a empresa atua, permitindo uma compreensão aprofundada do ambiente competitivo. Essa ferramenta oferece uma visão detalhada dos fatores que influenciam a rentabilidade e a dinâmica do mercado, proporcionando uma imersão mais completa no contexto em que a empresa está inserida.

### Ameaça de novos entrantes
**Média** – Embora o setor seja atraente para startups, a entrada de novos concorrentes enfrenta barreiras significativas, como exigências regulatórias rigorosas, incluindo a necessidade de autorização como Instituição de Transação de Pagamento (ITP), a demanda por integração bancária sólida e investimentos substanciais em cibersegurança. Essas condições elevam o nível de complexidade e custo para novos entrantes, protegendo as empresas já estabelecidas.

### Poder de negociação dos fornecedores
**Baixo** – A Finnet desenvolve suas soluções com base em tecnologia própria, incorporando recursos como APIs para integração ágil entre sistemas, EDI para a troca eletrônica estruturada de dados e RPA para a automação de processos repetitivos. Essa abordagem interna reduz significativamente a necessidade de recorrer a fornecedores externos, o que diminui seu poder de barganha e garante maior controle sobre prazos, custos e qualidade das entregas.

### Poder de negociação dos compradores
**Alto** – Os clientes da Finnet são, em sua maioria, empresas que realizam um elevado volume de transações financeiras diariamente. Esse perfil lhes confere maior poder de negociação, permitindo discutir de forma mais favorável aspectos como políticas de preços, prazos e níveis de serviço (SLA), além de exigir um grau elevado de personalização das soluções para atender necessidades específicas de integração, automação e segurança.

### Ameaça de produtos substitutos
**Média** – Algumas empresas ainda recorrem ao uso de planilhas ou ERPs generalistas para gerir suas operações financeiras. No entanto, essas ferramentas costumam apresentar limitações significativas, como a baixa capacidade de automação de processos, integração bancária restrita e mecanismos de controle de risco pouco robustos. Por conta dessas deficiências, sua substituição por soluções mais completas tende a ocorrer apenas em cenários de menor complexidade operacional, nos quais o volume de transações e a necessidade de conformidade regulatória são reduzidos.

### Rivalidade entre concorrentes existentes
**Alta** - No segmento financeiro, a concorrência é acirrada, com inúmeras fintechs disputando espaço e oferecendo soluções semelhantes. Apesar desse cenário competitivo, a Finnet se diferencia por entregar um alto nível de automação, capaz de otimizar processos e reduzir custos operacionais para seus clientes. Além disso, mantém parcerias estratégicas que ampliam seu alcance e fortalecem seu portfólio de serviços, ao mesmo tempo em que garante uma integração sólida e eficiente com o ecossistema bancário, assegurando conformidade regulatória, agilidade nas transações e maior segurança nas operações.

#### 4.1.2. Análise SWOT 

# Introdução à Análise SWOT

A realização de uma análise SWOT identificando Forças, Fraquezas, Oportunidades e Ameaças é essencial para estruturar com eficácia o 
desenvolvimento de um modelo preditivo em parceria com a Finnet Tecnologias. Essa metodologia estratégica oferece um panorama claro do
posicionamento da empresa, permitindo o alinhamento do projeto aos seus pontos fortes, desafios internos e ao contexto competitivo do mercado financeiro.



<img width="1920" height="1080" alt="Visual Chart Page Iteration 6" src="https://github.com/user-attachments/assets/db5bcd72-7b5c-4c38-9d5c-44a3b9669f0a" />



Com essa base, a análise SWOT pode orientar o projeto de modelo preditivo ao explorar:

Forças: expertise consolidada em integração com ERPs, robustez das soluções multibanco/multiempresas e pioneirismo em produtos como Bolepix e Open Finance.

Fraquezas: possíveis pontos de fragilidade podem incluir dependência de infraestrutura legada dos clientes, ciclos de adoção de inovações e a necessidade de customização intensa para diferentes ERPs e setores.

Oportunidades: o crescente ambiente regulatório e de inovação em pagamentos digitais, expansão do ecossistema Open Finance e potencial de uso de dados para previsão de inadimplência, comportamento de pagamentos ou risco na cadeia de fornecedores.

Ameaças: concorrência crescente de fintechs e grandes provedores de serviços financeiros, mudanças regulatórias rápidas e riscos relacionados à segurança da informação e conformidade com LGPD.

# Conclusão da Análise SWOT

Ao analisar essas dimensões, torna-se possível estruturar um modelo preditivo direcionado a maximizar os benefícios para a Finnet, como o aprimoramento na tomada de decisões financeiras, a antecipação de possíveis riscos e o incremento na personalização das soluções oferecidas. Dessa forma, garante-se que o projeto não apenas esteja alinhado às diretrizes estratégicas da Finnet, mas também promova um impacto substancial e sustentável em longo prazo.

#### 4.1.3. Planejamento Geral da Solução

A solução é baseada em uma base de dados de pagadores, contendo histórico de boletos, status de liquidação, datas de vencimento, bancos emissores, endereços dos devedores, dados dos recebedores e registros de interações anteriores entre pagadores e a instituição, como número e data dos contatos realizados.

A partir dessa base, será desenvolvido um modelo preditivo que fornecerá aos clientes da Finnet insights como: score de risco de inadimplência, tendência de pagamento, previsão de recebimentos no período e a melhor janela provável de pagamento. Esses dados preditivos visam apoiar decisões estratégicas em processos de cobrança e gestão financeira.

Inicialmente, a solução será disponibilizada como uma **Prova de Conceito (POC)** para integração na plataforma Luna, utilizada para emissão de cobranças e gestão de recebíveis por instituições financeiras ou empresas com alto volume de transações. O produto será entregue por meio de um script em Python, possibilitando que gestores financeiros acessem os insights preditivos diretamente em seu fluxo de trabalho.
Em fases futuras, a solução será incorporada de forma nativa na plataforma, permitindo automações com base nas predições e visualizações em tempo real.

##### Benefício esperados da solução:
- **Redução do risco de inadimplência**, garantindo uma maior previsibilidade de comportamento dos pagadores.
- **Aumento da eficiência operacional**, ao priorizar estratégias de cobranças e renegociações.
- **Melhor previsibilidade de fluxo de caixa**, com projeções de recebimentos mais assertivas.
- **Aprimoramento da comunicação com o cliente final**, baseada em dados históricos e interações anteriores.
- **Valor agregado à plataforma da parceira**, posicionando a empresa como fornecedora de soluções financeiras com inteligência preditiva.

##### O sucesso da solução será medido por meio dos seguintes critérios:
- **Acurácia das predições**: Porcentagem de assertividade nas projeções de inadimplência satisfatória, conforme métricas definidas durante o desenvolvimento.
- **Usabilidade e aderência**: validação positiva por parte dos stakeholders e usuários-chave (gerentes financeiros e coordenadores de contas a receber) durante testes e apresentações.
- **Relevância dos insights**: feedback qualitativo dos usuários demonstrando utilidade prática para tomadas de decisões reais.
- **Viabilidade de escalabilidade**: capacidade técnica de aplicar o modelo a diferentes clientes e setores com necessidade mínima de customização.
- **Níveis de segurança compatíveis com a LGPD**: o tratamento de dados pessoais deverá respeitar os princípios da Lei Geral de Proteção de Dados (LGPD)


#### 4.1.4. Value Proposition Canvas
```
Posicione aqui seu canvas.

Remova este bloco ao final
```

#### 4.1.5. Matriz de Riscos

## introdução

A matriz de risco é uma ferramenta visual utilizada para identificar, classificar e priorizar riscos ou oportunidades com base na probabilidade de ocorrência e no impacto que podem causar no projeto ou na organização. Ela permite que as equipes tomem decisões mais assertivas, direcionando esforços para lidar primeiro com os pontos mais críticos.
No caso do nosso projeto, a matriz foi aplicada para mapear oportunidades relacionadas à previsão de inadimplência e à melhoria da gestão de recebíveis da Finnet. Os riscos e oportunidades foram posicionados nos quadrantes de acordo com sua probabilidade (Alta, Média ou Baixa) e impacto (Alto, Médio ou Baixo).
Uma das oportunidades identificadas como Alta probabilidade / Alto impacto foi a melhoria na previsão de inadimplência para reduzir perdas, já que isso afeta diretamente a eficiência na cobrança e os resultados financeiros.

![Matriz de riscos](../assets/Matriz_de_risco.png)

## Conclusão

A implementação da matriz de risco no projeto desempenhou um papel fundamental ao possibilitar a priorização das ações consideradas mais relevantes para o alcance dos objetivos propostos. Além disso, o uso dessa ferramenta se mostrou eficaz para promover um alinhamento claro dentro da equipe, facilitando a identificação das oportunidades que demandam ações mais urgentes, bem como dos possíveis riscos que exigem monitoramento contínuo e estratégias adequadas de mitigação.

### Ameaças

1. **Previsão imprecisa do fluxo de recebimentos**:

A projeção incorreta do fluxo de caixa pode comprometer diretamente a saúde financeira dos clientes da Finnet, afetando decisões como pagamentos de fornecedores, funcionários, dívidas e investimentos. Uma previsão mal calibrada pode levar a déficits operacionais ou má alocação de recursos.

2. **Erro significativo no score de inadimplência**:

O score de risco de inadimplência orienta decisões cruciais, como concessão de crédito ou prazos de pagamento. Altas taxas de erro neste indicador podem gerar perdas financeiras relevantes, sobretudo em setores onde o risco de crédito é fator-chave, como instituições financeiras, empresas de cobrança e consórcios.

3. **Janela de pagamento subótima**

Indicar uma janela de pagamento que não considera o comportamento real ou a rotina financeira do devedor (como a data de recebimento de salário) pode reduzir as chances de recebimento, comprometendo a eficácia da cobrança.

4. **Tendência de pagamento classificada incorretamente**

Uma categorização equivocada do pagador como “em dia”, “com atraso” ou “inadimplente” pode distorcer o perfil de risco atribuído, gerando decisões inadequadas de cobrança ou concessão de crédito.

5. **Dependência excessiva de dados históricos**

Modelos preditivos baseados unicamente em dados históricos podem falhar diante de mudanças no contexto econômico, comportamental ou regulatório. Essa limitação afeta a capacidade de adaptação do sistema a novos padrões de comportamento dos pagadores.

6. **Baixa aceitação ou adoção da funcionalidade**

Mesmo que os modelos estejam tecnicamente corretos, a falta de transparência, explicabilidade ou integração com os fluxos do cliente pode gerar desconfiança e baixa adoção. Isso limita o valor percebido da funcionalidade e reduz o impacto do projeto.

7. **Qualidade e atualização insuficiente da base de dados**:

Informações desatualizadas, incompletas ou fora da distribuição esperada comprometem a qualidade das análises geradas. A confiabilidade dos insights depende diretamente da integridade e frescor dos dados utilizados.

###  Oportunidades

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

Ao oferecer uma solução robusta e inovadora, há um grande potencial para criar novas oportunidades de negócios, principalmente junto a empresas que priorizam a utilização estratégica de inteligência de dados.

#### 4.1.6. Personas

#### Pessoa Jurídica 

<div align="center">
<sub align="center">Figure 3 – Persona - Pessoa Jurídica</sub>
</div>

<div align="center">
<img src="../assets/Persona_Jurídica.png" alt="Value Proposition Canvas" border="0" width=100% height=100%>
</div>

<div align="center">
<sup>Fonte: Produzido pelo grupo, 2025.</sup>
</div>

Carlos Almeida representa o perfil do decisor financeiro que busca soluções tecnológicas para otimizar a gestão de crédito e reduzir riscos de inadimplência. Como Chief Financial Officer de uma empresa de grande porte, lida diariamente com o desafio de manter a saúde financeira da organização, equilibrando previsibilidade de caixa, controle de recebimentos e mitigação de perdas. Sua atuação exige acesso rápido a informações confiáveis e ferramentas que apoiem decisões estratégicas baseadas em dados.

#### Gerente Finnet

<div align="center">
<sub align="center">Figura 4 – Persona - Gerente Finnet</sub>
</div>

<div align="center">
<img src="../assets/persona_finnet.png" alt="Persona Finnet" border="0" width=100% height=100%>
</div>

<div align="center">
<sup>Fonte: Produzido pelo grupo, 2025.</sup>
</div>

Rogério Silveira é o perfil de cliente principal do projeto e atua como Gerente Financeiro na Finnet. Ele é responsável por monitorar transações e elaborar relatórios financeiros para empresas parceiras, garantindo que estas tenham uma visão clara e atualizada do seu fluxo de caixa. Com alta afinidade com tecnologia, busca automatizar processos de coleta e análise de dados, reduzindo o trabalho manual e aumentando a precisão das informações. Entre suas principais necessidades está prever a inadimplência e identificar tendências de pagamento, permitindo agir de forma proativa. Atualmente, Rogério deseja agregar valor ao serviço prestado pela Finnet implementando recursos como score de risco de inadimplência, melhor janela provável de pagamento e análise do impacto da inadimplência no fluxo de recebimentos, fortalecendo a tomada de decisão dos clientes e da própria empresa.

#### 4.1.7. Jornadas do Usuário
```
Posicione aqui seus mapas de jornadas do usuário que utiliza o modelo.

Remova este bloco ao final
```

#### 4.1.8 Política de Privacidade

##### Modelo de Política de Privacidade:
Projeto [NOME DO PROJETO]

##### Informações Gerais 


Esta política de privacidade informa como o projeto **[NOME DO PROJETO]**, desenvolvido pelo grupo The Seven, trata os dados pessoais coletados durante o uso da solução. Está em conformidade com a Lei nº 13.709/2018 – LGPD.

##### Dados Coletados

A Finnet forneceu os seguintes dados pessoais:
 
- Id do grupo. 
- Id do beneficiário. 
- Data de inclusão do pagamento. 
- Status do boleto 
- Data de vencimento da fatura
- Valor a ser pago pelo beneficiário 
- Data de pagamento 
- Nome do banco emissor 
- Id do pagador
- CEP do pagador.

Não foram fornecidos dados sensíveis sobre os titulares.

##### Dados coletados automaticamente: 

- Quantidade de acessos do pagador
- Última data de acesso.

##### Finalidade do Tratamento

Os dados pessoais coletados serão tratados com as seguintes finalidades:

- Garantia do funcionamento da plataforma, permitindo a análise do comportamento de pagamento e a geração de insights preditivos sobre inadimplência;
  
- Elaboração de estatísticas e projeções, tais como, score de risco de inadimplência, tendência de pagamento (em dia, com
atraso, inadimplente) e previsão de recebimentos, para apoiar a tomada de decisões da área financeira da empresa parceira.

A utilização desses dados é permitida de acordo com o artigo 7 da LGPD:

- I - mediante o fornecimento de consentimento pelo titular (cliente do parceiro);
- II - para o cumprimento de obrigação legal ou regulatória pelo controlador;
- V - quando necessário para a execução de contrato ou de procedimentos preliminares relacionados a contrato do qual seja parte o titular, a pedido do titular dos dados;
- IX - quando necessário para atender aos interesses legítimos do controlador ou de terceiro, exceto no caso de prevalecerem direitos e liberdades fundamentais do titular que exijam a proteção dos dados pessoais.

Além disso, os dados fornecidos não são identificados como sensíveis ou referentes a menores de idade, portanto, não infringem, de qualquer forma, o artigo 11 da Lei Geral de Proteção de Dados Nº 13.709.

##### Armazenamento e Retenção

Os dados utilizados no projeto serão armazenados em um documento no Drive e repositório no Github para facilitar seu uso.

##### Prazo

O acesso aos dados fornecidos é válido por dois meses e meio, tempo referente a duração do projeto.

##### Compartilhamento de Dados 

Os dados e resultados gerados a partir da solução podem ser compartilhados somente com a empresa parceira do projeto.


##### Segurança dos Dados

Para garantir a segurança dos dados, é realizado o controle do acesso, de modo que apenas os envolvidos no projeto têm acesso pleno a eles.

##### Direitos dos Titulares

Os titulares dos dados podem solicitar:

- Acesso aos seus dados;
- Correção de informações incorretas;
- Exclusão de dados;
- Portabilidade de dados;
- Oposição ao tratamento e revogação de consentimento.

Para exercer esses direitos, envie uma solicitação para: govcorp@finnet.com.br.

##### Encarregado de Dados (DPO)

Nome: Marília Nascimbeni Buchala
E-mail: mbuchala@gmail.com 


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
