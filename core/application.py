from core.constants import FLAVORS_IDS, ENGINES_ID, MACHINES, SYSTEMS, DISKS, PROFILES

def generate_terraform_script(
    profile_code: str,
    user: str,
    name: str,
    password: str,
    ssh_key_name: str,
    storage_key_id: str,
    storage_key_secret: str,
    ssh_private_key_path: str,
) -> str:
    i = 0
    r = 0
    while i < len(PROFILES):
        if PROFILES[i]["code"] == profile_code:
            r = i
            break
        i += 1

    machine = next(
        (m for m in MACHINES if m["name"] == PROFILES[r]["machine_id"]), MACHINES[0]
    )
    image = next(
        (s for s in SYSTEMS if s["name"] == PROFILES[r]["system_id"]), SYSTEMS[0]
    )

    engine_id = ENGINES_ID[0]["id"]
    flavor_id = PROFILES[r]["database_id"]
    database_volume_size = 100

    bucket_name = f"{name}-bucket"
    database_name = f"{name}-db"
    machine_name = f"{name}-machine"

    terraform_script = f"""
terraform {{
  required_providers {{
    mgc = {{
      source = "magalucloud/mgc"
    }}
  }}
}}

resource "mgc_virtual_machine_instances" "{machine_name}" {{
  name = "{machine_name}"
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

resource "mgc_dbaas_instances" "{database_name}" {{
  flavor_id = "{flavor_id}"
  name = "{database_name}"
  user = "{user}"
  password = "{password}"
  engine_id = "{engine_id}"
  volume = {{
    size = {database_volume_size}
    type = "CLOUD_NVME_15K"
  }}
}}

resource "null_resource" "docker_container" {{
  depends_on = [mgc_virtual_machine_instances.{name}-machine]

  provisioner "remote-exec" {{
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y docker.io",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",
      "sudo docker run --name docker-nginx -d -p 80:80 nginx"  # Altere para o seu container desejado
    ]

    connection {{
      type        = "ssh"
      host        = mgc_virtual_machine_instances.{name}-machine.network.public_address
      user        = "ubuntu"  # Use o usuário correto para a imagem Ubuntu
      private_key = file("{ssh_private_key_path}")  # O caminho para sua chave SSH
    }}
  }}
}}

resource "mgc_object_storage_buckets" "{bucket_name}" {{
  provider = mgc.sudeste
  bucket = "{bucket_name}"
  enable_versioning = true
  recursive = true # If true, any configuration or operation specified in the resource will be applied not only to the bucket itself but also to all the objects contained within that bucket.
  bucket_is_prefix = false # Indicates whether the bucket name will be used as a prefix for objects.
}}

provider "mgc" {{
  alias = "sudeste"
  region = "br-se1"
  object_storage = {{
    key_pair = {{ 
      key_id = "{storage_key_id}"
      key_secret = "{storage_key_secret}"
    }}
  }}
}}
"""
    return terraform_script

# Exemplo de uso da função
# A função pode ser chamada com parâmetros específicos para gerar o script Terraform
