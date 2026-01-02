<img src="static/images/logo.svg" alt="InovaTech Systems Logo" width="200"/>

# InovaTech Systems

Projeto de uma landing page para uma empresa fictícia com a finalidade de executar o teste prático para a vaga de Estágio para Desenvolvedor Full Stack na Mupi Systems.

---

## 🎯 Funcionalidades Principais

- **Landing Page**
- **Formulário de Contato**
- **Página de Login**
- **Painel Administrativo para Visualização das Mensagens**
- **Recursos como Exclusão, Busca e Filtro de Mensagens Lidas, Não Lidas e Todas**

---

## 🛠️ Tecnologias

- **Django 6**
- **TailwindCSS v4.1**
- **HTMX**

---

## 🚀 Como Rodar a Aplicação

### Passo a Passo

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/joserodrigues27/projeto_estagio_2026_1.git
cd projeto_estagio_2026_1
```

#### 2️⃣ Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5️⃣ Crie um superusuário (para acessar a área admin)
```bash
python manage.py createsuperuser
```

#### 6️⃣ Execute o servidor
```bash
python manage.py runserver
```

#### 7️⃣ Acesse a aplicação

- **Landpage:** `http://localhost:8000`
- **Login:** `http://localhost:8000/login`
- **Painel Administrativo:** `http://localhost:8000/painel` (requer login)
