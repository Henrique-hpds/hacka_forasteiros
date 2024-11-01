# database.py

from constants import FLAVORS_IDS, ENGINES_ID

def generate_terraform_script(flavor_id, db_name, user, password, engine_id, volume_size):
    # Gera o script Terraform com base nos parâmetros fornecidos
    script = f"""terraform {{
  required_providers {{
    mgc = {{
      source = "magalucloud/mgc"
    }}
  }}
}}

resource "mgc_dbaas_instances" "{db_name}" {{
  flavor_id = "{flavor_id}"
  name = "{db_name}"
  user = "{user}"
  password = "{password}"
  engine_id = "{engine_id}"
  volume = {{
    size = {volume_size}
    type = "CLOUD_NVME_15K"
  }}
}}
"""
    return script

def list_database_profiles():
    # Lista todos os perfis de banco de dados
    return FLAVORS_IDS
