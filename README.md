# Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web utilizando PyAutoGUI e dados de um arquivo CSV.

## Descrição

O script principal (`automacao.py`) abre o navegador Chrome, acessa um site de treinamento, faz login e cadastra produtos automaticamente lendo os dados do arquivo `produtos.csv`. O script `posicao.py` é um auxiliar para obter as posições do mouse na tela para ajustar as coordenadas do PyAutoGUI.

**Atenção:** Este script utiliza coordenadas fixas do mouse e credenciais hardcoded. Ele pode não funcionar em diferentes resoluções de tela ou se o layout do site mudar. Use com cautela e apenas em ambientes de teste.

## Requisitos

- Python 3.x
- Bibliotecas: pandas, pyautogui

## Instalação

1. Clone ou baixe o repositório.

## Uso

1. Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório.
2. Execute o script principal:

   ```bash
   python automacao.py
   ```

   O script irá:
   - Abrir o Chrome.
   - Acessar o site de login.
   - Fazer login com as credenciais hardcoded.
   - Cadastrar cada produto da tabela CSV.

3. Para ajustar posições do mouse (se necessário), execute:

   ```bash
   python posicao.py
   ```

   Aguarde 5 segundos e mova o mouse para a posição desejada. O script imprimirá as coordenadas.

## Arquivos

- `automacao.py`: Script principal de automação.
- `posicao.py`: Script auxiliar para obter posições do mouse.
- `produtos.csv`: Arquivo CSV com os dados dos produtos a serem cadastrados.

## Estrutura do CSV

O arquivo `produtos.csv` deve ter as seguintes colunas:

- `codigo`: Código do produto
- `marca`: Marca do produto
- `tipo`: Tipo do produto
- `categoria`: Categoria (número)
- `preco_unitario`: Preço unitário
- `custo`: Custo
- `obs`: Observações (opcional)

## Troubleshooting

- **Erro de coordenadas:** As posições do mouse são fixas. Se a resolução da tela ou o layout do site mudar, ajuste as coordenadas em `automacao.py` usando `posicao.py`.
- **Login falha:** Verifique as credenciais hardcoded no script.
- **Chrome não abre:** Certifique-se de que o Chrome está instalado e acessível via comando "chrome".

## Segurança

Este script contém credenciais hardcoded e simula ações do usuário. Não use em produção sem modificações para segurança (ex: usar variáveis de ambiente para credenciais).
