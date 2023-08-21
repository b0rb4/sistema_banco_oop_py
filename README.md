# Sistema Bancario em Python.

O código apresentado é uma simulação simples de um sistema bancário que permite a criação e acesso a contas. A seguir, uma descrição geral do que o código faz:

Classes e Funções Auxiliares:

* Conta: Representa uma conta bancária e contém métodos para sacar, depositar, ver extrato, fazer empréstimo, solicitar cartão de crédito, comprar e pagar com o cartão de crédito.
* hash_senha: Transforma uma senha em um hash usando SHA-256.
* input_float: Obtém um input do usuário, garantindo que é um valor decimal.
* input_int: Obtém um input do usuário, garantindo que é um valor inteiro.
* checar_senha: Verifica se a senha digitada pelo usuário corresponde à senha da conta.
* imprimir_extrato_animacao: Simula a impressão de um extrato.

Função Main:

* Mantém uma lista de contas e um loop principal que permite ao usuário criar uma conta, acessar uma conta existente ou sair do programa.
* Quando uma conta é acessada, um novo menu é apresentado ao usuário com opções como sacar, depositar, entre outras ações relacionadas à conta.

Fluxo Principal:

* O programa inicia e entra no loop principal.
* O usuário tem a opção de criar uma nova conta inserindo nome e senha. A senha é convertida em hash e armazenada dessa forma.
* O usuário pode acessar uma conta existente inserindo o nome. Se a conta for encontrada, será solicitada a senha.
* Uma vez logado, o usuário pode realizar várias operações bancárias. Essas operações modificam o saldo da conta, o extrato e os detalhes do cartão de crédito, conforme o caso.
* O usuário pode sair do menu da conta e voltar ao menu principal ou encerrar o programa.

Pontos de Atenção:

* O código utiliza animações com atrasos (usando time.sleep) para simular processamento ou impressão.
* A senha é convertida em hash antes de ser armazenada e comparada, o que é uma boa prática em termos de segurança.
* O código não possui tratamentos para muitos cenários possíveis em um sistema bancário real, como juros, multas ou datas de vencimento.
* Não há persistência de dados. Ao encerrar o programa, todas as contas e transações são perdidas.
* A função imprimir_extrato_animacao sempre retorna um erro, simulando que a impressora não está conectada, independentemente da situação real.
Melhorias Possíveis:
* Adicionar tratamento de erros e validações adicionais.
* Implementar persistência de dados usando, por exemplo, arquivos ou bancos de dados.
* Adicionar mais características e complexidade ao sistema, como juros, taxas e multas.
* Melhorar a segurança, utilizando melhores práticas para armazenamento de senhas.
* Permitir que várias contas possam ter o mesmo titular. Atualmente, o titular é usado para localizar contas, o que pode causar conflitos.
