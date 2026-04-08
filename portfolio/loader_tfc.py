from portfolio.models import *
import json


Tfc.objects.all().delete()

with open("portfolio/data/tfc.json") as f:
    tfcs = json.load(f)

    for tfc in tfcs:
        Tfc.objects.create(
            titulo = tfc["Título"],
            aluno = tfc["Aluno"],
            orientador = tfc["Orientador"],
            licenciatura = tfc["Lincenciatura"],
            pdf = tfc["PDF"],
            mail = tfc["Mail"],
            resumo = tfc["Resumo"],
            palavras_chave = tfc["Palavras chave"],
            area = tfc["Áreas"],
            tecnologias = tfc["Tecnologias usadas"],
            rating = tfc["Rating"]
        )