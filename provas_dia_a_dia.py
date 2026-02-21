from dataclasses import dataclass


@dataclass
class Questao:
    enunciado: str
    opcoes: list[str]
    resposta_correta: str


@dataclass
class Prova:
    nome: str
    questoes: list[Questao]


def aplicar_prova(prova: Prova) -> None:
    print(f"\n=== {prova.nome} ===")
    acertos = 0

    for i, questao in enumerate(prova.questoes, start=1):
        print(f"\nQuestão {i}: {questao.enunciado}")
        for letra, opcao in zip(["A", "B", "C", "D"], questao.opcoes):
            print(f"  {letra}) {opcao}")

        resposta = input("Sua resposta (A/B/C/D): ").strip().upper()
        while resposta not in {"A", "B", "C", "D"}:
            resposta = input("Resposta inválida. Digite A, B, C ou D: ").strip().upper()

        if resposta == questao.resposta_correta:
            acertos += 1

    print(f"\nResultado: {acertos}/{len(prova.questoes)} acertos")


def main() -> None:
    prova_eq_nivel_1 = Prova(
        nome="EQ Nível 1 — Equilíbrio de Nash no dia a dia",
        questoes=[
            Questao(
                enunciado=(
                    "Dois colegas escolhem entre levar guarda-chuva ou não. "
                    "Se os dois levarem, ambos ficam seguros; se só um levar, "
                    "quem não levou pode se molhar. Qual cenário tende a ser estável "
                    "(ninguém quer mudar sozinho)?"
                ),
                opcoes=[
                    "Ambos levam guarda-chuva.",
                    "Nenhum leva guarda-chuva.",
                    "Só o colega 1 leva guarda-chuva.",
                    "Só o colega 2 leva guarda-chuva.",
                ],
                resposta_correta="A",
            ),
            Questao(
                enunciado=(
                    "Dois vizinhos decidem se limpam a calçada. Se os dois limpam, "
                    "a rua fica ótima para ambos. Se um só limpa, o outro aproveita sem esforço. "
                    "Qual opção representa um possível equilíbrio em cooperação?"
                ),
                opcoes=[
                    "Os dois limpam a calçada.",
                    "Só um limpa e o outro nunca ajuda.",
                    "Nenhum limpa, mesmo achando ruim.",
                    "Cada um espera o outro para sempre.",
                ],
                resposta_correta="A",
            ),
            Questao(
                enunciado=(
                    "Dois amigos escolhem restaurante: A (barato) ou B (caro). "
                    "Eles preferem ficar juntos no mesmo lugar a ir separados. "
                    "Qual ideia descreve melhor o equilíbrio de Nash?"
                ),
                opcoes=[
                    "Cada um vai para um restaurante diferente.",
                    "Um escolhe por sorte e o outro ignora.",
                    "Ambos escolhem o mesmo restaurante e ninguém melhora mudando sozinho.",
                    "Eles deixam para decidir depois de comer.",
                ],
                resposta_correta="C",
            ),
        ],
    )

    prova_mda = Prova(
        nome="MdA no dia a dia — Nível 1",
        questoes=[
            Questao(
                enunciado=(
                    "No contexto de tomada de decisão (MdA), você precisa escolher "
                    "o melhor meio de transporte para o trabalho. Qual atitude usa "
                    "melhor critérios objetivos?"
                ),
                opcoes=[
                    "Escolher o primeiro que aparece, sem comparar.",
                    "Comparar tempo, custo e conforto antes de decidir.",
                    "Escolher sempre o mais caro.",
                    "Perguntar para uma pessoa aleatória e seguir sem pensar.",
                ],
                resposta_correta="B",
            ),
            Questao(
                enunciado=(
                    "Você vai comprar um celular para estudo e trabalho. Em MdA, qual "
                    "é uma boa prática?"
                ),
                opcoes=[
                    "Definir critérios (bateria, memória, preço) e dar pesos.",
                    "Comprar o mais bonito, apenas.",
                    "Comprar o primeiro anúncio da internet.",
                    "Decidir sem olhar especificações.",
                ],
                resposta_correta="A",
            ),
            Questao(
                enunciado=(
                    "Para organizar a rotina diária, qual ação combina com MdA?"
                ),
                opcoes=[
                    "Fazer tarefas por impulso, sem prioridade.",
                    "Priorizar tarefas por urgência e impacto.",
                    "Evitar qualquer planejamento.",
                    "Executar apenas tarefas fáceis.",
                ],
                resposta_correta="B",
            ),
        ],
    )

    print("Escolha a prova:")
    print("1) EQ Nível 1 — Equilíbrio de Nash no dia a dia")
    print("2) MdA no dia a dia — Nível 1")
    opcao = input("Digite 1 ou 2: ").strip()

    if opcao == "1":
        aplicar_prova(prova_eq_nivel_1)
    elif opcao == "2":
        aplicar_prova(prova_mda)
    else:
        print("Opção inválida. Execute novamente e escolha 1 ou 2.")


if __name__ == "__main__":
    main()
