def generate_storage_terraform_script(bucket_name, api_key, key_id, key_secret):
    script = f"""
terraform {{
  required_providers {{
    mgc = {{
      source = "magalucloud/mgc"
    }}
  }}
}}

resource "mgc_object_storage_buckets" "my-bucket" {{
  provider = mgc.sudeste
  bucket = "{bucket_name}"
  enable_versioning = true
  recursive = true # If true, any configuration or operation specified in the resource will be applied not only to the bucket itself but also to all the objects contained within that bucket.
  bucket_is_prefix = false # Indicates whether the bucket name will be used as a prefix for objects.
}}

provider "mgc" {{
  alias = "sudeste"
  region = "br-se1"
  api_key = "{api_key}"
  object_storage = {{
    key_pair = {{ 
      key_id = "{key_id}"
      key_secret = "{key_secret}"
    }}
  }}
}}
"""
    return script