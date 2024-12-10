import requests
from flask import Blueprint, render_template, request, redirect, url_for

# Configurações do Baserow
BASEROW_URL = "https://api.baserow.io/api/database/rows/table/{table_id}/"  # Substitua {table_id} pelo ID da tabela
API_TOKEN = "NYFQdjWKOOI7VSTUnjTiV3T6P6PiLY4r"  # Substitua pelo seu token

headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    pontuacao_url = BASEROW_URL.format(table_id=405433)
    equipes_url = BASEROW_URL.format(table_id=402978)

    pontuacao_res = requests.get(pontuacao_url, headers=headers)
    equipes_res = requests.get(equipes_url, headers=headers)

    print("Pontuações:", pontuacao_res.json())
    print("Equipes:", equipes_res.json())

    if pontuacao_res.status_code == 200 and equipes_res.status_code == 200:
        equipes = {e["id"]: e["field_3073941"] for e in equipes_res.json()["results"]}
        print("Mapeamento de equipes:", equipes)

        pontuacoes = pontuacao_res.json()["results"]
        print("Dados de pontuações:", pontuacoes)

        ranking_data = {}
        for p in pontuacoes:
            equipe_id = int(p.get("field_3094703"))
            pontos = int(p.get("field_3094705", 0))

            if equipe_id and equipe_id in equipes:
                if equipe_id not in ranking_data:
                    ranking_data[equipe_id] = {"name": equipes[equipe_id], "points": 0}

                ranking_data[equipe_id]["points"] += pontos

        print("Ranking intermediário:", ranking_data)
        ranking = sorted(ranking_data.values(), key=lambda x: x["points"], reverse=True)
        print("Ranking final:", ranking)

        return render_template("index.html", teams=ranking)
    else:
        return f"Erro ao acessar Baserow: {pontuacao_res.status_code}, {equipes_res.status_code}"


@bp.route("/update", methods=["GET", "POST"])
def update():
    equipes_url = BASEROW_URL.format(table_id=402978)
    eventos_url = BASEROW_URL.format(table_id=405375)
    pontuacao_url = BASEROW_URL.format(table_id=405433)

 

    if request.method == "POST":
        id_equipe = request.form["id_equipe"]
        id_evento = request.form["id_evento"]
        pontos = int(request.form["pontos"])

        # Enviar dados para a tabela pontuacao
        payload = {
            "field_3094703": id_equipe,
            "field_3094704": id_evento,
            "field_3094705": pontos
        }
        response = requests.post(pontuacao_url, headers=headers, json=payload)

        if response.status_code == 200:
            return redirect(url_for("main.index"))
        else:
            return f"Erro ao atualizar pontuação: {response.status_code}"

    # Busca dados de equipes e eventos para preencher o formulário
    equipes_res = requests.get(equipes_url, headers=headers)
    eventos_res = requests.get(eventos_url, headers=headers)

    if equipes_res.status_code == 200 and eventos_res.status_code == 200:
        equipes = [{"id": e["id"], "name": e["field_3073941"]} for e in equipes_res.json()["results"]]
        eventos = [{"id": e["id"], "name": e["field_3094181"]} for e in eventos_res.json()["results"]]
        return render_template("update.html", equipes=equipes, eventos=eventos)
    else:
        return f"Erro ao acessar Baserow: {equipes_res.status_code}, {eventos_res.status_code}"
