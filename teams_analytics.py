import json


def analisar_desempenho(jogos_realizados, time_analisado):
    
    # Dicionário que vai armazenar as estatísticas do time
    estatisticas = {
        "vitorias_casa": 0,
        "vitorias_fora": 0,
        "empates": 0,
        "derrotas": 0,
        "gols_marcados": 0,
        "gols_sofridos": 0
    }

    # Percorrendo todos os jogos do JSON
    for jogo in jogos_realizados.values():

        # O resultado vem no formato "2 X 1"
        # Então primeiro eu separo os gols da casa e os gols de fora
        resultado = jogo["Result"]
        gols_casa, gols_fora = resultado.split(" X ")

        # Convertendo pra inteiro porque split retorna string
        gols_casa = int(gols_casa)
        gols_fora = int(gols_fora)

        # Verificando se o time analisado jogou em casa
        if jogo["Home"] == time_analisado:
            gols_time = gols_casa
            gols_adv = gols_fora
            contexto = "casa"

        # Verificando se jogou fora
        elif jogo["Away"] == time_analisado:
            gols_time = gols_fora
            gols_adv = gols_casa
            contexto = "fora"

        # Se o time não participou do jogo, ignora
        else:
            continue

        # Incrementando os gols totais
        estatisticas["gols_marcados"] += gols_time
        estatisticas["gols_sofridos"] += gols_adv

        # Agora vem a comparação do placar
        if gols_time > gols_adv:
            # Se ganhou, preciso saber se foi em casa ou fora
            if contexto == "casa":
                estatisticas["vitorias_casa"] += 1
            else:
                estatisticas["vitorias_fora"] += 1

        elif gols_time == gols_adv:
            estatisticas["empates"] += 1

        else:
            estatisticas["derrotas"] += 1

    # Retornando o dicionário final já preenchido
    return estatisticas


# Carregando o arquivo JSON
with open("serie_A_2025_games.json", "r", encoding="utf-8") as archive:
    data = json.load(archive)


# Definindo qual time quero analisar (tem que estar exatamente igual ao JSON)
time = "Vitória / BA"

resultado = analisar_desempenho(data, time)

# Printando o resultado final
print(resultado)