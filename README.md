# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# Nome do projeto

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
- <a href="https://www.linkedin.com/in/victorbarq/">Nome do instrutor 1</a>
- <a href="https://www.linkedin.com/in/victorbarq/">Nome do instrutor 2</a> 
- <a href="https://www.linkedin.com/in/victorbarq/">Nome do instrutor 3</a> 
- <a href="https://www.linkedin.com/in/victorbarq/">Nome do instrutor 4</a>
- <a href="https://www.linkedin.com/in/victorbarq/">Nome do instrutor 5</a> 


## 📝 Descrição
<br>
Nossa solução busca enfrentar o desafio da inadimplência crescente que compromete o fluxo de caixa e a previsibilidade de receita de empresas clientes da Finnet. Para isso, desenvolvemos um modelo preditivo baseado em dados históricos de boletos, status de liquidação, prazos, bancos emissores e interações anteriores com pagadores. A partir dessa base, o sistema gera insights como score de risco, tendência de pagamento, previsão de recebimentos e melhor janela provável de quitação, permitindo decisões mais estratégicas em cobranças e gestão financeira. Inicialmente entregue como uma Prova de Conceito (POC) integrada à plataforma Luna via script em Python, a solução será futuramente incorporada de forma nativa, possibilitando automações e visualizações em tempo real. Com isso, buscamos reduzir riscos de inadimplência, otimizar operações, aumentar a assertividade no planejamento financeiro e fortalecer o posicionamento da Finnet como referência em soluções financeiras inteligentes e orientadas por dados.
<br>
Escreva uma curta descrição sobre o seu projeto (problema a ser resolvido e solução proposta). (minímo 150 palavras, máximo 600 palavras)

<b>Link para vídeo demonstrativo:</b> <a href="https://inteli.edu.br">Coloque seu link aqui</a>

Caso tenha publicado seu modelo preditivo em uma aplicação web, não deixe de colocar o link de acesso aqui.

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

## 💻 Execução dos projetos

🚀 Requisitos

VS Code
Ter o Visual Studio Code instalado.

Python
Versão compatível — normalmente versões 3.8, 3.9, 3.10 ou superior. Confirmar se o repositório tem requirements.txt ou pyproject.toml com versão alvo.

Extensões no VS Code

Python (oficial da Microsoft)

Jupyter

(Opcional) Pylance ou outra para auxílio de tipagem / linting.

Gerenciador de pacotes
pip, possivelmente conda, dependendo do projeto.

Ambiente virtual
Para isolar dependências (virtualenv, venv, conda, pyenv, etc.).

Dependências do projeto
Qualquer biblioteca especificada nos arquivos de dependência: requirements.txt, environment.yml, setup.py, etc.

Git
Para clonar o repositório.

Outros requisitos específicos

Dados ou arquivos de entrada que estejam fora do repositório (se existirem).

Versões de pacotes compatíveis.

Configurações ambientais (por exemplo, variáveis de ambiente).

Permissões para leitura/escrita de alguns diretórios, se for o caso.

🛠 Passos para configurar e rodar os notebooks localmente:

Clonar o repositório
<br>

```bash
git clone https://github.com/Inteli-College/2025-2A-T18-IN03-G04.git
cd 2025-2A-T18-IN03-G04
```
<br>
Criar e ativar um ambiente virtual
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
pip install pandas numpy scikit.learn seaborn matplotlib 
```
<br>

Descreva aqui os requisitos e os passos necessários para execução dos notebooks localmente (VS Code com instalação de Python) e no ambiente Google Colab

> Não deixe de informar para o caso do Colab que, se o utilizador não salvar uma cópia do notebook no seu Google Drive próprio, não será possível salvar as alterações realizadas no arquivo.

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