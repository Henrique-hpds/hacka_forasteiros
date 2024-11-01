# Criando o arquivo para gerar um script Terraform baseado nas constantes fornecidas


def generate_disk_terraform_script(volume_name, volume_size):
    """
    Função para gerar um script Terraform para a criação de um banco de dados.

    Args:
        flavor_id (str): ID do sabor do banco de dados.
        db_name (str): Nome do banco de dados.
        user (str): Usuário do banco de dados.
        password (str): Senha do banco de dados.
        engine_id (str): ID do motor de banco de dados.
        volume_size (int): Tamanho do volume em GB.

    Returns:
        str: Script Terraform gerado.
    """
    return f"""
# volume.tf
terraform {{
  required_providers {{
    mgc = {{
      source = "magalucloud/mgc"
    }}
  }}
}}

# Criação de volume
resource "mgc_block_storage_volumes" "{volume_name}_volume" {{
  name = "{volume_name}-volume"
  size = {volume_size}
  type = {{
    name = "cloud_nvme"
  }}
}}

output "{volume_name}_volume_id" {{
  value = mgc_block_storage_volumes.{volume_name}_volume.id
}}
"""
