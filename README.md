# 🥦 GreenLink

**GreenLink** é uma aplicação desenvolvida em **Python** por 
**Paulo Campello**
**Ricardo Cunha**
**Gonçalo Maia**
**David Vieira**
 com o objetivo de otimizar a gestão e comercialização de vegetais.  
O sistema integra três níveis de utilizadores — **Administrador**, **Cliente** e **Fornecedor** — permitindo uma comunicação eficiente e uma gestão transparente de produtos, pedidos e stocks.

---

## Funcionalidades

### Administrador
- Gere contas de utilizadores (clientes e fornecedores)  
- Adiciona, remove e atualiza produtos e stocks  
- Supervisiona pedidos e o seu estado  

### Cliente
- Regista-se e realiza login  
- Efetua pedidos de vegetais  
- Acompanha o estado de cada pedido (feito, pago, enviado, entregue)  
- Comunica com o fornecedor  

### Fornecedor
- Atualiza o stock dos produtos  
- Consulta e gere pedidos recebidos  
- Comunica com clientes e confirma entregas  

---

## Estrutura do Projeto
GreenLink/
│
├── main.py
├── classes/
│ ├── admin.py
│ ├── cliente.py
│ ├── fornecedor.py
│ └── produto.py
│
├── data/
│ ├── utilizadores.json
│ ├── produtos.json
│ └── pedidos.json
│
└── README.md
