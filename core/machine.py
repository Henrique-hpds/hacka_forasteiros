# machine_profiles.py
from core.constants import MACHINES, SYSTEMS


def generate_machine_terraform_script(name, machine_name, image_name, ssh_key_name):
    """
    Gera um script Terraform para uma máquina virtual com as especificações fornecidas.
    """
    machine = next((m for m in MACHINES if m["name"] == machine_name), MACHINES[0])
    image = next((s for s in SYSTEMS if s["name"] == image_name), SYSTEMS[0])

    script = f"""
terraform {{
  required_providers {{
    mgc = {{
      source = "magalucloud/mgc"
    }}
  }}
}}

provider mgc {{}}

resource "mgc_virtual_machine_instances" "basic_instance" {{
  name = "{name}"
  machine_type = {{
    name = "{machine['name']}"
  }}
  image = {{
    name = "{image['name']}"
  }}
  network = {{
    associate_public_ip = true
  }}
  ssh_key_name = "{ssh_key_name}"
}}
    """
    return script


def list_machine_profiles():
    """
    Retorna uma lista de perfis de máquina disponíveis.
    """
    return MACHINES
