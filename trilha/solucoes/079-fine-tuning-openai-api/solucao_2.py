"""Solução de referência — Exercício 2 da Lição 079.

Cria (de forma simulada) um job de fine-tuning, estimando o número de passos
de treino a partir de n_epochs, do número de exemplos e do batch_size.
"""
import math


def criar_job(file_id, modelo_base, n_exemplos, n_epochs, lr_mult, batch_size):
    passos = n_epochs * math.ceil(n_exemplos / batch_size)
    return {
        "id": "ftjob-0042",
        "model": modelo_base,
        "training_file": file_id,
        "hyperparameters": {
            "n_epochs": n_epochs,
            "learning_rate_multiplier": lr_mult,
            "batch_size": batch_size,
        },
        "passos_estimados": passos,
        "status": "validating_files",
    }


job = criar_job("file-0001", "base-mini", n_exemplos=50, n_epochs=3, lr_mult=0.2, batch_size=8)
print("job:", job["id"], "modelo base:", job["model"], "status:", job["status"])
for chave, valor in job["hyperparameters"].items():
    print(f"  {chave} = {valor}")
print("passos estimados:", job["passos_estimados"])
