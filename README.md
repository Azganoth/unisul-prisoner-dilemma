# unisul-prisoner-dilemma

Implementação do dilema do prisioneiro utilizando o protocolo XML-RPC para a matéria Fundamentos de Sistemas Distribuídos na UNISUL.

## 📜 Instruções

**Requerimentos:**

-   Python 3.8+

> Cada servidor deve ser iniciado em um terminal ou aba de terminal.

Primeiramente, devemos deixar o servidor "Juíz", que realizará o julgamento de dois prisioneiros por vez, disponível e aguardando os testemunhos.

Para isso, vamos iniciar o servidor "Juíz":

```sh
python judge.py
```

Com o servidor "Juíz" aguardando testemunhos, podemos começar a questionar os prisioneiros pelo seus testemunhos.

Para isso, vamos iniciar um servidor "Prisioneiro" para cada prisioneiro, onde cada um irá aguardar pelo seu julgamento após enviar seu testemunho:

```sh
python prisioner.py
```

## 🔗 Referências

- [Dilema do prisioneiro](https://pt.wikipedia.org/wiki/Dilema_do_prisioneiro)

- [O dilema do prisioneiro e a Lava-Jato](https://agcomunique.wordpress.com/2016/11/17/o-dilema-do-prisioneiro-e-a-lava-jato/)

## 🔑 Licença

Este projeto está sob a [licença MIT](LICENSE.md).
