Uma versão melhorada do nosso sistema Bancário Python Bank v1 

<h3>Visão Geral</h3>
<ul>Esse é um sistema bancário simples que permite ao usuário realizar operações como:
  <li>✅ Depósito</li>
  <li>✅ Saque</li>
  <li>✅ Visualizar extrato</li>
  <li>✅ Criar usuário</li>
  <li>✅ Criar conta corrente</li>
  <li>✅ Listar contas</li>
</ul>


<p>O sistema usa funções para modularizar o código e segue regras específicas de passagem de argumentos.</p>


<h3>📌 Principais Funções e Como Funcionam</h3>

- <h4><strong>menu()<strong></h4>

Exibe as opções disponíveis e recebe a escolha do usuário.
depositar(saldo, valor, extrato, /)

Só aceita argumentos por posição (/ no final da definição).
Se o valor for maior que 0, ele adiciona o valor ao saldo e ao extrato.
Retorna o novo saldo e extrato.
sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)

Só aceita argumentos por nome (* no início).
Faz várias verificações:
Se há saldo suficiente.
Se o valor ultrapassa o limite.
Se o número de saques foi excedido.
Atualiza saldo, extrato e número de saques.
exibir_extrato(saldo, /, *, extrato)

Aceita saldo por posição e extrato por nome.
Exibe o extrato e o saldo disponível.<br><br>

- <strong>criar_usuario(usuarios)<strong>

Pede os dados do usuário (CPF, nome, data de nascimento e endereço).
Verifica se o CPF já existe na lista usuarios (evita duplicatas).
Adiciona o usuário à lista se não existir.<br><br>

- <h4><strong>filtrar_usuario(cpf, usuarios)<strong></h4>

Busca um usuário pelo CPF na lista usuarios.<br><br>


- <h4><strong>criar_conta(agencia, numero_conta, usuarios)<strong></h4>

Pede o CPF do usuário para vincular à conta.
Se o CPF existir, cria uma conta com agência fixa (0001) e número sequencial.<br><br>


- <h4><strong>listar_contas(contas)<strong></h4>

Exibe todas as contas cadastradas.<br><br>

- <h4><strong>main()<strong></h4>

Inicializa variáveis (saldo, limite, usuarios, contas, etc.).
Usa um while True para manter o sistema rodando até o usuário sair (q).
Chama as funções certas conforme a escolha do usuário.
