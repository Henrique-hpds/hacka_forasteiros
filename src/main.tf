terraform {
  required_providers {
    mgc = {
      source = "magalucloud/mgc"
    }
  }
}

provider mgc {

}

resource "mgc_virtual_machine_instances" "basic_instance" {
  name = "forasteiros_teste_17"
  machine_type = {
    name = "BV1-4-20"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true
  }
  ssh_key_name = "julio_avelar"
}