from portfolio.models import *
import json


UC.objects.all().delete()

with open("portfolio/data/ULHT260-PT.json") as f:
    uc_info = json.load(f)

    for uc in uc_info["courseFlatPlan"]:
        uc_code_file = uc["curricularIUnitReadableCode"] + "-PT" + ".json" #vai buscar o ficheiro json referente ao código da uc atual

        

        with open(f"portfolio/data/ucs/{uc_code_file}") as g:
            uc_json = json.load(g)

            
            UC.objects.create(
                descricao = uc_json["presentation"],
                objetivo = uc_json["objectives"],
                programa = uc_json["programme"],
                avaliacao = uc_json["avaliacao"],
                nome = uc["curricularUnitName"],
                ano = uc["curricularYear"],
                semestre = uc["semester"],
                ects = uc["ects"]
            )


