NetOpsChat - Parte 1 - Protocolo de Mensagens com Sockets

## Arquivos

- `servidor.py` - Servidor central (NOC) que aceita múltiplos clientes
- `cliente.py` - Cliente interativo para operadores
- `protocolo.md` - Especificação do protocolo

## Execução Rápida

### 1. Iniciar o servidor

```bash
python servidor.py
```

Saída esperada:
```
Servidor ouvindo em 0.0.0.0:5000
```

### 2. Conectar cliente(s)

Em outro terminal (ou múltiplos):

```bash
python cliente.py
```

Se quiser conectar a um host/porta diferente:

```bash
python cliente.py 192.168.1.100 5000
```

### 3. Enviar mensagens

No terminal do cliente, digite uma mensagem qualquer e pressione Enter:

```
> Olá a todos
Olá a todos
> Está tudo bem?
Está tudo bem?
```

As mensagens serão transmitidas para **todos os outros clientes** conectados.

### 4. Desconectar

Digite `/exit` ou pressione `Ctrl+C`.

## Exemplo de Uso com 2 Clientes

**Terminal 1:**
```bash
$ python servidor.py
Servidor ouvindo em 0.0.0.0:5000
```

**Terminal 2:**
```bash
$ python cliente.py
> Oi pessoal!
```

**Terminal 3:**
```bash
$ python cliente.py
> Oi pessoal!
> Como estão?
```

Os clientes recebem as mensagens uns dos outros automaticamente via broadcast.

## Requisitos

- Python 3.6+
- Bibliotecas padrão: `socket`, `threading`

## Estrutura do Protocolo

Mensagens simples de texto, uma por linha, terminadas em `\n`.
O servidor faz broadcast (retransmissão) para todos os clientes conectados, exceto o remetente.
