import json


# Aqui eu faço a extração dos dados do arquivo JSON e o transformo em um dicionário py.
with open("serie_A_2025_games.json", "r") as archive:
    data = json.load(archive)
    
    #  A função aqui foi criada com um dicionário de forma abstrata para generalizar consultas. Ela verifica os jogos realizados do time requisitado.
    def analisar_desempenho(jogos_realizados, time_analisado):
       estatisticas = {
            "vitorias_casa": 0,
            "vitorias_fora": 0,
            "empates": 0,
            "derrotas": 0,
            "gols_marcados": 0,
            "gols_sofridos": 0
        }
       
       for jogo in jogos_realizados:
        #    Analisa se o time jogou em casa 
           if jogo["Home"] == time_analisado:
               gols_time = jogo["Gols_Home"]
               gols_adv = jogo["Gols_Away"]
               contexto = "casa"

        #    Analisa se o time jogou fora 
           elif jogo["Away"] == time_analisado:
               gols_time = jogo["Gols_Away"]
               gols_adv = jogo["Gols_Home"]
               contexto = "fora"
            #  Se ao percorrer a lista de jogos, não condizer com o nome do time analisado, pula pro próximo.
           else:
               continue
               
            
           