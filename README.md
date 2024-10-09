Automação de Cadastro de Produtos 🛒
Descrição
Este projeto é uma automação para cadastro de produtos em um sistema web usando Python e a biblioteca pyautogui. Ele facilita o processo de inserção de dados, como código do produto, marca, tipo, categoria, preço unitário, custo e observações, diretamente a partir de uma planilha CSV. Essa automação é especialmente útil para empresas que precisam inserir uma grande quantidade de produtos em seu sistema de forma rápida e precisa, economizando tempo e evitando erros manuais.

Funcionalidades
Automação de Login: O script realiza login no sistema, inserindo o e-mail e a senha automaticamente.
Preenchimento Automático de Formulários: Lê os dados de um arquivo CSV contendo informações dos produtos e preenche os campos do formulário no sistema de forma automatizada.
Scroll Automático: Ajusta a visualização da página conforme necessário para garantir que todos os campos estejam visíveis.
Cadastro em Lote: Processa cada linha do CSV como um novo produto a ser cadastrado, agilizando o processo de inserção de dados em massa.
Tecnologias Utilizadas
Python: Linguagem de programação utilizada para desenvolvimento do script.
PyAutoGUI: Biblioteca que permite a automação de movimentos do mouse, cliques e digitação de texto.
Pandas: Usado para leitura e manipulação dos dados da planilha CSV.
Pré-requisitos
Python 3.x instalado
Bibliotecas pyautogui e pandas (instale com pip install pyautogui pandas)
Navegador Firefox instalado (ajuste no código caso use outro navegador)
Arquivo produtos.csv no mesmo diretório do script, contendo os campos: codigo, marca, tipo, categoria, preco_unitario, custo, obs.
Como Utilizar
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/automacao-cadastro-produtos.git
Navegue até a pasta do projeto:
bash
Copiar código
cd automacao-cadastro-produtos
Certifique-se de que o arquivo produtos.csv está no mesmo diretório do script.
Execute o script:
bash
Copiar código
python automacao_cadastro_produtos.py
A automação abrirá o navegador, realizará o login e iniciará o processo de cadastro de produtos.
