# web-scraping-python
Projeto de web scraping em Python com geração de PDF.

Este projeto foi desenvolvido com o objetivo de praticar Python, utilizando conceitos básicos de web scraping e geração de arquivos PDF.
O programa acessa o site da Nike SNKRS, coleta os nomes dos tênis disponíveis no calendário e gera um arquivo PDF com essas informações.


🎯 Objetivo do projeto

Aprender como acessar páginas da internet com Python

Entender como funciona o web scraping

Praticar listas, laços de repetição e bibliotecas externas

Gerar um arquivo PDF automaticamente

Este projeto tem finalidade educacional.

🧠 O que o código faz

Acessa uma página da Nike

Lê o conteúdo HTML da página

Procura os nomes dos tênis

Guarda os nomes em uma lista

Cria um arquivo PDF com os tênis encontrados

🛠️ Tecnologias utilizadas

Python 3 

Requests – usado para acessar o site

BeautifulSoup (bs4) – usado para ler o HTML

ReportLab – usado para criar o PDF

📂 Estrutura do projeto
webscraping/
│
├── webscraping.py
├── tenis_disponiveis.pdf
├── venv/
└── README.md

▶️ Como executar o projeto

1️⃣ Clone o repositório
git clone https://github.com/natanael-alves/web-scraping-python.git

2️⃣ Entre na pasta do projeto
cd web-scraping-python

3️⃣ Ative o ambiente virtual

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

4️⃣ Instale as bibliotecas
pip install requests beautifulsoup4 reportlab

5️⃣ Execute o programa
python webscraping.py


Após executar, será criado o arquivo:

tenis_disponiveis.pdf

📄 Resultado

O programa gera um PDF contendo:

Um título

Uma lista com os nomes dos tênis disponíveis no site

⚠️ Observação

O site pode mudar sua estrutura HTML.
Se isso acontecer, o código pode parar de funcionar, pois as classes usadas no scraping podem mudar.

Esse projeto foi criado apenas para estudo e aprendizado.

📚 Aprendizados

. Com este projeto aprendi:

. Como fazer requisição para um site

. Como extrair informações do HTML

. Como usar listas em Python

. Como gerar arquivos PDF

. Como organizar um projeto simples

👨‍💻 Autor

Natanael Alves da Silva
GitHub: https://github.com/natanael-alves

LinkedIn: https://www.linkedin.com/in/natanaelalves/
