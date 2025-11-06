# 🥦 GreenLink

**GreenLink** é uma aplicação desenvolvida em **Python** por 

**Paulo Campello @kampello**

**Ricardo Cunha @ricardo6927**

**Gonçalo Maia @DrunkTurkey**

**David Vieira @a44120-droid**

 com o objetivo de otimizar a gestão e comercialização de vegetais.  
O sistema integra três níveis de utilizadores — **Administrador**, **Cliente** e **Fornecedor** — permitindo uma comunicação eficiente e uma gestão transparente de produtos, pedidos e stocks.

---

## Funcionalidades


### Tools ⚒️ 
Ficheiro de funcionalidades de Utilizador
-Fornecedor_Tools
-Cliente_Tools
-Fornecedor_Tools
### Administrador 👨‍💼👩‍💼
- Gere contas de utilizadores (clientes e fornecedores)  
- Adiciona, remove e atualiza produtos e stocks  
- Supervisiona pedidos e o seu estado  

### Cliente 🥦
- Regista-se e realiza login  
- Efetua pedidos de vegetais  
- Acompanha o estado de cada pedido (feito, pago, enviado, entregue)  
- Comunica com o fornecedor  

### Fornecedor
- Atualiza o stock dos produtos  
- Consulta e gere pedidos recebidos  
- Comunica com clientes e confirma entregas  

---
- [x] Login
- [ ] Dashboard Cliente Fornecedor
- [ ] Add: funcionalidade de chat com Cliente x Forncedor
---
> [!NOTE]
> Esta estrotura ainda pode sofrer algumas mudanças...
```
GreenLink/
│
├── classes/
│   ├── admin.py
│   ├── cliente.py
│   └── fornecedor.py
│
├── tools/
│   ├── admin_tools/
│   ├── cliente_tools/
│   └── fornecedor_tools/
|   └── Toolbox.py
│
├── data/
│   └── greenlink.db
│
├── main.py
├── README.md
└── .gitignore

```