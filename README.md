# 🛒 FeiraDoMês - Gerenciador de Compras Inteligente

**Aplicação Web Full-Stack** - Shopping List Manager  
**Tecnologia**: Django 4.2 + SQLite + Bootstrap 5  
**Ambiente**: Python 3.14 | Totalmente Responsivo

## Desenvolvedor

- **André Kuniscki Monteiro de Albuquerque Junior** - 01406148

---

## Sobre o Projeto

**FeiraDoMês** é uma aplicação web moderna e eficiente para organizar, categorizar e monitorar suas compras no dia a dia. Com um design limpo e intuitivo, o app permite que você nunca mais esqueça de um item na sua lista de compras.

A plataforma utiliza **autenticação segura**, **categorização automática de produtos**, **cálculo de totais em tempo real** e **dashboard com estatísticas** para proporcionar uma experiência completa de gerenciamento de compras.

---

## Funcionalidades Principais

### **Dashboard Inteligente**
- Resumo de compras do mês (total geral, itens pendentes, comprados)
- Estatísticas de gastos e média de despesas
- Produtos mais frequentemente comprados
- Visualização rápida do progresso de compras

### **Gerenciador de Itens**
- Adicionar, editar e remover itens da lista
- Campo de quantidade e unidade customizável
- Preço unitário com cálculo automático de total
- Notas personalizadas para cada produto
- Marcação de itens como "Comprado" ou "Pendente"
- Sistema de favoritos para itens recorrentes

### **Sistema de Categorias**
- 8 categorias pré-configuradas:
  - Hortifruti
  - Limpeza
  - Carnes
  - Padaria
  - Bebidas
  - Lácteos
  - Grãos
  - Outros
- Filtrar itens por categoria
- Filtrar por status (Pendentes, Comprados, Favoritos)

### **Totalizador Automático**
- Cálculo em tempo real de:
  - Total Geral (todos os itens)
  - Total Pendente (ainda não comprado)
  - Total Comprado (já adquirido)
  - Quantidade total de itens
- Visualização clara com cards destacados

### **Perfil Personalizado**
- Criação de conta com autenticação segura
- Configurações de preferências:
  - Supermercado favorito
  - Moeda de preferência
  - Dark Mode (preparado para implementação)

### **Histórico de Compras**
- Modelo preparado para arquivamento de listas
- Rastreamento de padrões de compra
- Base para análise de gastos futuros

---

## Como Executar

### Pré-requisitos
- Python 3.10+
- pip (gerenciador de pacotes Python)
- Django 4.2 ou superior

### Instalação Passo a Passo

```bash
# 1. Clonar ou extrair o projeto
cd feira_project

# 2. Criar ambiente virtual (opcional, mas recomendado)
python -m venv .venv

# 3. Ativar ambiente virtual
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar migrações do banco de dados
python manage.py migrate

# 6. Criar superusuário (admin)
python manage.py createsuperuser

# 7. Executar servidor de desenvolvimento
python manage.py runserver

# 8. Acessar no navegador
# http://127.0.0.1:8000/
```

---

## Estrutura do Projeto

```
feira_project/
├── manage.py                    # Gerenciador Django
├── requirements.txt             # Dependências Python
├── db.sqlite3                   # Banco de dados
│
├── feira_site/                  # Configurações Django
│   ├── settings.py             # Variáveis de ambiente
│   ├── urls.py                 # Roteamento principal
│   └── wsgi.py                 # Interface WSGI
│
├── market/                      # App principal (Marketplace de compras)
│   ├── models.py               # Modelos: Item, Category, UserProfile, ShoppingHistory
│   ├── views.py                # Views: Home, ItemList, ItemDetail, ItemForm
│   ├── forms.py                # Formulários customizados
│   ├── urls.py                 # Rotas internas
│   ├── signals.py              # Sinais: auto-criação de perfil e categorias
│   ├── admin.py                # Admin Django
│   └── migrations/             # Migrações de banco
│
├── accounts/                    # App autenticação
│   ├── models.py               # User (Django built-in)
│   ├── views.py                # Login, Register, Profile, Logout
│   ├── forms.py                # Login e Register forms
│   ├── urls.py                 # Rotas de autenticação
│   ├── admin.py                # Admin Django
│   └── migrations/             # Migrações de banco
│
├── static/
│   └── css/
│       └── global.css          # Estilos globais (331 linhas)
│
└── templates/
    ├── accounts/
    │   ├── login.html          # Página de login
    │   ├── register.html       # Página de registro
    │   └── profile.html        # Perfil do usuário
    │
    └── market/
        ├── base.html           # Template base (navbar + footer)
        ├── home.html           # Dashboard inicial
        ├── about.html          # Página sobre
        ├── item_list.html      # Lista de compras
        ├── item_form.html      # Formulário adicionar/editar
        └── item_detail.html    # Detalhes do item
```

---

## Autenticação & Segurança

- Sistema de login e registro funcional
- Proteção com LoginRequiredMixin em rotas críticas
- Senhas hashed com algoritmo Django padrão
- CSRF protection habilitada
- XFrame options para proteger clickjacking

---

## Banco de Dados

**Engine**: SQLite3  
**ORM**: Django ORM

### Modelos Principais

```python
# Item - Produtos da lista
- name (CharField)
- quantity (PositiveIntegerField)
- unit (CharField)
- price (DecimalField)
- category (ForeignKey → Category)
- is_favorite (BooleanField)
- bought (BooleanField)
- notes (TextField)
- owner (ForeignKey → User)
- created_at (DateTimeField)

# Category - Categorias de produtos
- name (CharField)
- icon (CharField)

# UserProfile - Preferências do usuário
- user (OneToOneField → User)
- profile_picture_url (URLField)
- favorite_market (CharField)
- currency (CharField)
- dark_mode (BooleanField)

# ShoppingHistory - Histórico de compras
- owner (ForeignKey → User)
- total_price (DecimalField)
- total_items (PositiveIntegerField)
- completed_at (DateTimeField)
- notes (TextField)
```

## Notas Finais

- Projeto desenvolvido com foco em **organização** e **boas práticas**
- Código limpo e comentado para facilitar manutenção
- Estrutura escalável para futuras expansões
- Totalmente responsivo e pronto para produção

---

**Desenvolvido usando Python, Django, SQlite e Bootstrap**
**Instituição**: Uninassau - Ciência da Computação  
**Disciplina**: Back-End e Frameworks  
**Professor**: Mauricio Braga
**Aluno**: Andre Kuniscki Monteiro de Albuquerque Junior - 01406148