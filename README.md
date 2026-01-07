# 🛒 Products API

API REST simples para gerenciamento de produtos, desenvolvida em **Python + Flask + SQLite**, com operações completas de **CRUD**.

Este projeto foi criado com foco em aprendizado prático de CRUD, backend, HTTP, REST e testes via Postman.

---

## 🚀 Tecnologias utilizadas

* Python 3
* Flask
* SQLite
* Postman (para testes)

---

## 📁 Estrutura do projeto

```text
CRUD_products/
│
├── app.py        # API REST (Flask)
├── main.py       # Interface CLI (terminal)
├── crud.py       # Regras de negócio / banco
├── database.db   # Banco de dados SQLite
└── README.md
```

---

## ▶️ Como rodar o projeto

### 1️⃣ Clonar o repositório

```bash
https://github.com/Vitor985-hub/CRUD_products.git
```

### 2️⃣ Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install flask
```

### 4️⃣ Rodar a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

## 🖥️ Uso via terminal (CLI)

O arquivo `main.py` permite executar operações CRUD diretamente pelo terminal,
sem utilizar a API HTTP.

Exemplo:
```bash
python main.py
```

---

## 📌 Endpoints disponíveis

### 🔹 Listar todos os produtos

**GET** `/products`

**Resposta:** `200 OK`

```json
[
  {
    "id": 1,
    "nome": "condicionador",
    "preco": 34.9,
    "quantidade": 15,
    "categoria": "higiene pessoal",
    "data_criacao": "2026-01-06 20:54:24"
  }
]
```

---

### 🔹 Buscar produto por ID

**GET** `/products/{id}`

**Resposta:**

* `200 OK` → produto encontrado
* `404 Not Found` → produto não existe

---

### 🔹 Criar produto

**POST** `/products`

**Headers:**

```
Content-Type: application/json
```

**Body (JSON):**

```json
{
  "nome": "shampoo",
  "preco": 29.90,
  "quantidade": 10,
  "categoria": "higiene pessoal"
}
```

**Resposta:**

* `201 Created` ou `200 OK`

---

### 🔹 Atualizar produto

**PUT** `/products/{id}`

**Body (JSON):**

```json
{
  "preco": 39.90,
  "quantidade": 20
}
```

**Resposta:**

* `200 OK`

---

### 🔹 Deletar produto

**DELETE** `/products/{id}`

**Resposta:**

* `200 OK`

---

## 🧪 Testes

Os testes foram realizados utilizando o **Postman**, validando:

* Métodos HTTP (GET, POST, PUT, DELETE)
* Status codes
* Envio de JSON no body
* Headers (`Content-Type: application/json`)

---

## 🧠 Conceitos praticados

* HTTP e métodos REST
* CRUD completo
* Leitura e interpretação de erros (400, 404, 405, 415, 500)
* Organização de backend
* SQL básico com SQLite

---

## 📌 Observações

* A rota raiz (`/`) retorna `404` por se tratar de uma API pura
* Não há frontend neste projeto

---

## ✍️ Autor
Vitor Eiji
GitHub: https://github.com/Vitor985-hub

Projeto desenvolvido para fins educacionais e portfólio backend.
