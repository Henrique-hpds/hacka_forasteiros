FLAVORS_IDS = [
    {"id": "784b7041-3e27-41f5-b31c-0a147d6e98e1", "label": "cloud-dbaas-gp1.xlarge", "vcpu": 16, "ram": 32, "application": "Banco de Dados para Aplicações de Alta Performance em Ciência de Dados"},
    {"id": "c460d5c1-883d-4fea-afc3-1a208e982084", "label": "cloud-dbaas-bs1.medium", "vcpu": 2, "ram": 4, "application": "Banco de Dados de Análise para Aplicativos Leves"},
    {"id": "650154ba-87a4-45b1-9ce6-f0b591603366", "label": "cloud-dbaas-bs1.large", "vcpu": 4, "ram": 8, "application": "Banco de Dados de Aplicação Móvel"},
    {"id": "8bbe8e01-40c8-4d2b-80e8-189debc44b1c", "label": "cloud-dbaas-bs1.small", "vcpu": 1, "ram": 4, "application": "Banco de Dados de Aplicação Web de Pequeno Porte"},
    {"id": "a31e3ac5-845a-4fef-b2c3-e101ae25acb5", "label": "cloud-dbaas-gp1.small", "vcpu": 2, "ram": 8, "application": "Banco de Dados para Aplicações de E-commerce"},
    {"id": "8916323b-458f-4acf-92bf-5734b92bba61", "label": "cloud-dbaas-gp1.medium", "vcpu": 4, "ram": 16, "application": "Banco de Dados para ERP de Pequenas Empresas"},
    {"id": "481aac7d-dd67-4054-bad2-dff712f4c77f", "label": "cloud-dbaas-gp1.large", "vcpu": 8, "ram": 32, "application": "Banco de Dados para Aplicações de BI e Análise de Dados"},
    {"id": "c29c2a8f-6d31-4c3d-9f7c-90bbf9a71e60", "label": "cloud-dbaas-hm1.medium", "vcpu": 16, "ram": 64, "application": "Banco de Dados de Alta Performance para Aplicações Corporativas"},
    {"id": "897bc067-2cd2-4bf3-838c-9702a7b52b2c", "label": "cloud-dbaas-hm1.large", "vcpu": 32, "ram": 128, "application": "Banco de Dados para Aplicações de Big Data e IA em Empresas"},
    {"id": "09106b02-5cfc-4d9b-afa2-2433d3458b61", "label": "cloud-dbaas-hm1.small", "vcpu": 8, "ram": 64, "application": "Banco de Dados para Grande Plataforma de Streaming"},
]


ENGINES_ID = [
    {"id": "063f3994-b6c2-4c37-96c9-bab8d82d36f7", "name": "mysql", "version": "8.0"},
]

MACHINES = [
    {"name": "BV1-4-20", "ram": 4, "vcpus": 1, "disk": 20, "gpu": 0},
    {"name": "BV2-8-40", "ram": 8, "vcpus": 2, "disk": 40, "gpu": 0},
    {"name": "BV4-16-100", "ram": 16, "vcpus": 4, "disk": 100, "gpu": 0},
    {"name": "BV1-1-10", "ram": 1, "vcpus": 1, "disk": 10, "gpu": 0},
    {"name": "BV2-4-40", "ram": 4, "vcpus": 2, "disk": 40, "gpu": 0},
    {"name": "BV8-16-100", "ram": 16, "vcpus": 8, "disk": 100, "gpu": 0},
    {"name": "BV8-32-100", "ram": 32, "vcpus": 8, "disk": 100, "gpu": 0},
    {"name": "BV1-2-20", "ram": 2, "vcpus": 1, "disk": 20, "gpu": 0},
    {"name": "BV4-8-100", "ram": 8, "vcpus": 4, "disk": 100, "gpu": 0},
    {"name": "BV2-2-40", "ram": 2, "vcpus": 2, "disk": 40, "gpu": 0},
]

SYSTEMS = [
    {"name": "cloud-ubuntu-24.04 LTS", "version": "24.04.1 LTS", "distro": "ubuntu", "platform": "linux"},
    {"name": "cloud-ubuntu-22.04 LTS", "version": "22.04.5 LTS", "distro": "ubuntu", "platform": "linux"},
    {"name": "cloud-oraclelinux-9", "version": "9.4", "distro": "oraclelinux", "platform": "linux"},
    {"name": "cloud-rocky-09", "version": "9.4", "distro": "rocky", "platform": "linux"},
    {"name": "cloud-ubuntu-20.04 LTS", "version": "20.04.6 LTS", "distro": "ubuntu", "platform": "linux"},
    {"name": "cloud-oraclelinux-8", "version": "8.10", "distro": "oraclelinux", "platform": "linux"},
    {"name": "cloud-debian-12 LTS", "version": "12.7", "distro": "debian", "platform": "linux"},
    {"name": "cloud-opensuse-15.6", "version": "15.6", "distro": "opensuse", "platform": "linux"},
    {"name": "cloud-fedora-40", "version": "40", "distro": "fedora", "platform": "linux"},
    {"name": "cloud-opensuse-15.5", "version": "15.5", "distro": "opensuse", "platform": "linux"},
    {"name": "cloud-fedora-39", "version": "39", "distro": "fedora", "platform": "linux"},
    {"name": "windows-server-2022", "version": "2022.1", "distro": "", "platform": "windows"},
]

DISKS = [
    {"id": "cd99ea02-45fc-4f4a-9c50-d75706f39174", "name": "App_NVME1K", "disk_type": "nvme", "availability_zone": "br-se1-a", "iops": {"read": 1000, "write": 1000, "total": 1000}, "status": "active", "description": "Application for NVME storage with 1k IOPS"}, 
    {"id": "55bd5b41-52ee-4fac-8ae9-7d48c9bd92cc", "name": "App_NVME15K", "disk_type": "nvme", "availability_zone": "br-se1-a", "iops": {"read": 15000, "write": 15000, "total": 15000}, "status": "active", "description": "Application for NVME storage with 15k IOPS"}, 
    {"id": "e05791b9-77f4-4e4a-a67c-a9a84ddd38cc", "name": "App_NVME5K", "disk_type": "nvme", "availability_zone": "br-se1-a", "iops": {"read": 5000, "write": 5000, "total": 5000}, "status": "active", "description": "Application for NVME storage with 5k IOPS"}, 
    {"id": "b74d1968-dd43-4136-ab63-193fcc71097e", "name": "App_NVME10K", "disk_type": "nvme", "availability_zone": "br-se1-a", "iops": {"read": 10000, "write": 10000, "total": 10000}, "status": "active", "description": "Application for NVME storage with 10k IOPS"}, 
    {"id": "cd031307-f387-4f2a-bf1c-d70b1698d433", "name": "App_NVME20K", "disk_type": "nvme", "availability_zone": "br-se1-a", "iops": {"read": 20000, "write": 20000, "total": 20000}, "status": "active", "description": "Application for NVME storage with 20k IOPS"}
]
