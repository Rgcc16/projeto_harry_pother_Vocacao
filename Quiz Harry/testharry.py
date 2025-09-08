def quiz_hogwarts():
    print("✨ Quiz de Harry Potter - Descubra sua casa em Hogwarts! ✨\n")

    pontos = {"Grifinória": 0, "Sonserina": 0, "Lufa-Lufa": 0, "Corvinal": 0}

    perguntas = [
        {
            "pergunta": "1) O que você mais valoriza?",
            "opcoes": {
                "a": ("Coragem", "Grifinória"),
                "b": ("Ambição", "Sonserina"),
                "c": ("Lealdade", "Lufa-Lufa"),
                "d": ("Inteligência", "Corvinal")
            }
        },
        {
            "pergunta": "2) Qual animal você escolheria como mascote?",
            "opcoes": {
                "a": ("Leão", "Grifinória"),
                "b": ("Cobra", "Sonserina"),
                "c": ("Texugo", "Lufa-Lufa"),
                "d": ("Corvo", "Corvinal")
            }
        },
        {
            "pergunta": "3) Qual qualidade você mais admira em si mesmo?",
            "opcoes": {
                "a": ("Corajoso", "Grifinória"),
                "b": ("Astuto", "Sonserina"),
                "c": ("Trabalhador", "Lufa-Lufa"),
                "d": ("Sábio", "Corvinal")
            }
        },
        {
            "pergunta": "4) Qual feitiço você usaria primeiro?",
            "opcoes": {
                "a": ("Expelliarmus (desarmar inimigos)", "Grifinória"),
                "b": ("Avada Kedavra (poder supremo)", "Sonserina"),
                "c": ("Alohomora (abrir portas)", "Lufa-Lufa"),
                "d": ("Legilimens (ler mentes)", "Corvinal")
            }
        },
        {
            "pergunta": "5) Se tivesse que escolher, preferiria ser lembrado como:",
            "opcoes": {
                "a": ("O Bravo", "Grifinória"),
                "b": ("O Grande", "Sonserina"),
                "c": ("O Bondoso", "Lufa-Lufa"),
                "d": ("O Sábio", "Corvinal")
            }
        }
    ]

    for p in perguntas:
        print(p["pergunta"])
        for chave, valor in p["opcoes"].items():
            print(f" {chave}) {valor[0]}")
        resposta = ""
        while resposta not in ["a", "b", "c", "d"]:
            resposta = input("Escolha (a/b/c/d): ").lower()
        casa = p["opcoes"][resposta][1]
        pontos[casa] += 1
        print()

    resultado = max(pontos, key=pontos.get)
    print("🏰 O Chapéu Seletor pensou bastante...")
    print(f"Você ficaria na casa **{resultado}**! 🪄")


# Executa o quiz
if __name__ == "__main__":
    quiz_hogwarts()

