from portfolio.models import *
import json


UC.objects.all().delete()
Docente.objects.all().delete

with open("portfolio/data/ULHT260-PT.json") as f:
    json_info = json.load(f)

    for teacher in json_info["teachers"]:
        Docente.objects.create(
            nome=teacher.get("fullName"),
            email=teacher.get("email"),
            card_code=teacher.get("cardCode"),
            employee_code=teacher.get("employeeCode"),
            degree=teacher.get("degree"),
            regime=teacher.get("regimen")
        )

    for uc in json_info["courseFlatPlan"]:
        uc_code_file = uc["curricularIUnitReadableCode"] + "-PT" + ".json" #vai buscar o ficheiro json referente ao código da uc atual

        

        with open(f"portfolio/data/ucs/{uc_code_file}") as g:
            uc_json = json.load(g)

            
            UC.objects.create(
                nome = uc["curricularUnitName"],
                ano = uc["curricularYear"],
                semestre = uc["semester"],
                ects = uc["ects"],

                descricao = uc_json["presentation"],
                objetivo = uc_json["objectives"],
                programa = uc_json["programme"]
            )



