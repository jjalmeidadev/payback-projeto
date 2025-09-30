# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# PayBack

## The Seven

## Integrantes: 
- <a href="https://www.linkedin.com/in/christian-de-carvalho-lawrence">Christian de Carvalho Lawrence</a>
- <a href="https://www.linkedin.com/in/isaac-souza-santos/">Isaac Souza Santos</a>
- <a href="https://www.linkedin.com/in/jaime-andrade-de-almeida-0777ba2a5/">Jaime Andrade de Almeida</a>
- <a href="https://www.linkedin.com/in/jo%C3%A3o-pedro-gon%C3%A7alves-corr%C3%AAa-araujo/">João Pedro Gonçalves Corrêa Araujo</a>
- <a href="">Mike Buchsenspaner</a> 
- <a href="https://www.linkedin.com/in/vin%C3%ADcius-rangel-marques/">Vinícius Rangel Marques</a> 
- <a href="https://www.linkedin.com/in/yan-de-oliveira-ribeiro-0a55a3356/">Yan de Oliveira Ribeiro</a>

## Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/fabiana-martins-de-oliveira-8993b0b2/">Fabiana Martins de Oliveira</a>
### Instrutores
- <a href="https://www.linkedin.com/in/rafaelwill/">Rafael Will Macedo de Araujo</a>
- <a href="https://www.linkedin.com/in/luciano-galdino-26191b36/">Luciano Galdino</a> 
- <a href="https://www.linkedin.com/in/gui-cestari/">Guilherme Henrique de Oliveira Cestari</a>
- <a href="https://www.linkedin.com/in/profclaudioandre/">Claudio Fernando André</a>
- <a href="https://www.linkedin.com/in/victorbarq/">Natalia Varela da Rocha Kloeckner</a> 


## 📝 Descrição
<br>
A solução proposta busca mitigar o desafio representado pelo aumento da inadimplência, fator que compromete tanto o fluxo de caixa quanto a previsibilidade de receitas das empresas clientes da Finnet. Para tal, foram desenvolvidos modelos preditivos fundamentados em dados históricos de boletos, status de liquidação, prazos, bancos emissores e interações anteriores com os respectivos pagadores. A partir dessa base analítica, o sistema disponibiliza indicadores como score do pagador, tendência de pagamento e previsão de recebimentos, subsidiando decisões estratégicas em processos de cobrança e gestão financeira. Inicialmente concebida como uma Prova de Conceito (POC) integrada à plataforma Luna por meio de script em Python, a solução apresenta potencial para integração nativa, o que possibilitará maior nível de automação e a disponibilização de visualizações em tempo real. Dessa forma, almeja-se minimizar riscos de inadimplência, otimizar a eficiência operacional e elevar a assertividade do planejamento financeiro, reforçando, simultaneamente, o posicionamento da Finnet como referência em soluções financeiras inteligentes e orientadas por dados.
<br>

<b>Link para vídeo demonstrativo:</b> <a href="https://inteli.edu.br">Coloque seu link aqui</a>

## 📁 Estrutura de pastas

<br>
├── assets/
├── documents/
        ├── extras/
        ├── matematica/
├── notebooks/
├── .gitattributes
├── .gitignore
├── CanvaValue.png
├── README.md
├── Arquivo A.csv
├── Arquivo B.csv
├── Arquivo C.csv
├── Arquivo D.csv
├── Arquivo E.csv
├── Arquivo F.csv
└── Arquivo G.csv
<br>
### Descrição das pastas por escrito:
<br>
README.md: arquivo principal de documentação do repositório, serve como guia inicial explicando os objetivos, organização e instruções de uso do projeto.
<br>
assets: pasta destinada a imagens, ícones e outros recursos visuais utilizados no projeto e na documentação.
<br>
documents: pasta reservada para armazenar documentos relacionados ao projeto, como relatórios, especificações ou arquivos de apoio.
<br>
notebooks: pasta onde ficam armazenados os Jupyter Notebooks utilizados para análises, prototipação de código e experimentos do projeto.
<br>
.gitattributes: arquivo de configuração do Git, utilizado para definir atributos de arquivos (como normalização de fim de linha ou regras específicas de merge).
<br>
.gitignore: arquivo de configuração do Git que lista os arquivos e pastas a serem ignorados no versionamento (ex: arquivos temporários, cache, etc.).
<br>
CanvaValue.png: imagem armazenada na raiz do projeto, provavelmente um recurso gráfico utilizado na documentação ou análise.
<br>
Arquivos.csv: arquivos que contêm os dados de treinamento e teste do modelo preditivo desenvolvido no projeto.
<br>

## 💻 Execução do projeto

🚀 Requisitos

**VS Code**

Ter o Visual Studio Code instalado.

Python
Versão compatível — normalmente versões 3.8, 3.9, 3.10 ou superior. Confirmar se o repositório tem requirements.txt ou pyproject.toml com versão alvo.

**Extensões no VS Code**

Python

Jupyter

**Dependências do projeto**

Numpy

Pandas

Scikit-learn

Matplotlib

Seaborn

Light gradient boosting machine

**Git**

Para clonar o repositório.

Versões de pacotes compatíveis.

Configurações ambientais (por exemplo, variáveis de ambiente).

Permissões para leitura/escrita de diretórios.

🛠 Passos para configurar e rodar os notebooks localmente:

1. Clonar o repositório
<br>

```bash
git clone https://github.com/Inteli-College/2025-2A-T18-IN03-G04.git
cd 2025-2A-T18-IN03-G04
```
<br>
2. Criar e ativar um ambiente virtual

<br>
No Linux/macOS:
<br>

```bash
python3 -m venv venv
source venv/bin/activate
```
<br>
No Windows:
<br>

```bash
python -m venv venv
.\venv\Scripts\activate
```
<br>

3. Instalar Denpendências:
<br>

```bash
pip install pandas numpy scikit-learn seaborn matplotlib lightgbm
```
<br>

**Colab**

No uso de ferramentas como o Google Colab, é necessário salvar uma cópia do notebook no Google Drive do usuário. Caso contrário, as alterações realizadas no arquivo não serão preservadas.

## 🗃 Histórico de lançamentos

* 0.1.3 - 16/08/2024
    * [sprint 1] Documentação de entendimento do negócio
* 0.2.7 - 30/08/2024
    * [sprint 2] Análise exploratória e levantamento de hipóteses
* 0.3.1 - 13/09/2024
    * [sprint 3] Preparação de dados e modelo preditivo preliminar
* 0.6.0 - 27/09/2024
    * [sprint 4] Comparação de modelos preditivos
* 1.0.0 - 11/10/2024
    * [sprint 5] Lançamento da primeira versão do modelo preditivo com documentação.

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.dev/Intelihub/Template_M3">MODELO GIT INTELI</a> by Inteli is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
