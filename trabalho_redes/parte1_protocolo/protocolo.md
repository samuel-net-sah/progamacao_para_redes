# Protocolo NetOpsChat

Protocolo simples de troca de mensagens via TCP.

## Funcionamento

- **Servidor**: Escuta na porta 5000 (configurável), aceita múltiplas conexões e faz broadcast de mensagens.
- **Cliente**: Conecta ao servidor e envia/recebe mensagens.

## Formato de Mensagens

Cada mensagem é uma linha de texto terminada em `\n`:

```
MENSAGEM_QUALQUER
```

Exemplos de uso no cliente:
- Enviar texto: `Olá a todos`
- Desconectar: `/exit` (ou Ctrl+C)

## Funcionamento do Servidor

1. Aceita conexão TCP de um cliente.
2. Adiciona o cliente à lista de clientes conectados.
3. Recebe mensagens do cliente.
4. Faz broadcast: retransmite cada mensagem para todos os outros clientes conectados (exceto o remetente).
5. Quando um cliente desconecta, remove da lista.

## Funcionamento do Cliente

1. Conecta ao servidor em `HOST:PORT` (padrão: `127.0.0.1:5000`).
2. Loop interativo: lê linhas do terminal e envia ao servidor.
3. Recebe mensagens de outros clientes e exibe no terminal.
4. Digitar `/exit` encerra a conexão.

## Exemplos de Execução

**Terminal 1 - Servidor:**
```bash
python servidor.py
```

**Terminal 2 - Cliente 1:**
```bash
python cliente.py
```
(Digita: `Oi pessoal`)

**Terminal 3 - Cliente 2:**
```bash
python cliente.py
```
(Receberá: `Oi pessoal`)

## Notas

- Protocolo textual simples para facilitar depuração.
- Sem autenticação ou encriptação.
- Broadcast para todos, exceto remetente.
- Pode ser estendido com protocolo estruturado (campos | delimitados) para operações mais complexas.
