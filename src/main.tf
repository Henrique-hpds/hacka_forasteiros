terraform {
  required_providers {
    mgc = {
      source = "magalucloud/mgc"
    }
  }
}

resource "mgc_virtual_machine_instances" "forasteiros_teste_29" {
  name = "forasteiros_teste_29"
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

resource "mgc_dbaas_instances" "forasteiros_teste_db_29" {
  flavor_id = "784b7041-3e27-41f5-b31c-0a147d6e98e1"
  name = "forasteiros_teste_db_29"
  user = "admin"
  password = "admin129"
  engine_id = "063f3994-b6c2-4c37-96c9-bab8d82d36f7"
  volume = {
    size = 10
    type = "CLOUD_NVME_15K"
  }
}

resource "mgc_object_storage_buckets" "bucket-29" {
  provider = mgc.sudeste
  bucket = "bucket-29"
  enable_versioning = true
  recursive = true # If true, any configuration or operation specified in the resource will be applied not only to the bucket itself but also to all the objects contained within that bucket.
  bucket_is_prefix = false # Indicates whether the bucket name will be used as a prefix for objects.
}

provider "mgc" {
  alias = "sudeste"
  region = "br-se1"
  object_storage = {
    # To use with Object Storage, there is a difference. Since we use the S3 protocol, it is necessary to use key pairs (Key Pairs). To generate key pairs, follow the instructions here https://docs.magalu.cloud/docs/api-keys/how-to/create-api-keys
    key_pair = { 
      key_id = "998bf02f-4b4a-4d6a-86f4-f3ac9a239691"
      key_secret = "8bd3ef46-f045-46d2-9e37-9a98565123fa"
    }
  }
}