# Ranking de Times com Flask e Baserow

Este projeto é uma aplicação web desenvolvida em Flask que utiliza a API do [Baserow](https://baserow.io) para gerenciar e exibir um ranking de times baseado em suas pontuações. A aplicação permite visualizar os rankings e atualizar os pontos através de um formulário simples.

---

## **Funcionalidades**

- Visualização do ranking de times ordenado pela pontuação.
- Atualização de pontuações diretamente pela interface web.
- Integração com a API do Baserow para manipulação de dados.

---

## **Requisitos**

- Python 3.10 ou superior
- Flask
- Bibliotecas Python:
  - `requests`
- Conta ativa no Baserow com acesso às tabelas de equipes, pontuações e eventos.

---

## Estrutura do projeto:
```
project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── update.html
│   └── models.py
│
├── app.db
├── config.py
├── run.py
└── requirements.txt
```

## **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2.Crie um ambiente virtual e ative-o:
  
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3.Instale as dependências:
```bash
pip install -r requirements.txt
```

4.Configure o projeto:
* Edite o arquivo routes.py com seu token de API do Baserow e os IDs das tabelas:
```python
BASEROW_URL = "https://api.baserow.io/api/database/rows/table/{table_id}/"
API_TOKEN = "SEU_TOKEN_AQUI"
```
* Substitua {table_id} pelos IDs corretos das tabelas de equipes, eventos e pontuações.

5. Execute o servidor Flask:
```bash
python run.py
```
