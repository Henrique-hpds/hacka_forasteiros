import os
import sys
import argparse
from core.database import generate_terraform_script, list_database_profiles
from core.machine import generate_machine_terraform_script, list_machine_profiles
from core.disk import generate_disk_terraform_script
from core.profiles import list_profiles
from core.storage import generate_storage_terraform_script
from core.application import generate_terraform_script
from core.constants import FLAVORS_IDS, ENGINES_ID, MACHINES, SYSTEMS, DISKS, PROFILES


def main():
    # Cria o parser principal
    parser = argparse.ArgumentParser(description="Main command line interface")
    subparsers = parser.add_subparsers(dest="command")

    # Comando 'db'
    db_parser = subparsers.add_parser("db", help="Database commands")
    db_subparsers = db_parser.add_subparsers(dest="subcommand")

    db_list = db_subparsers.add_parser("list", help="List all database profiles")
    db_create = db_subparsers.add_parser("create", help="Create a new database")

    # Adicionando argumentos para o comando create
    db_create.add_argument("-f", "--flavor_id", help="ID of the database flavor")
    db_create.add_argument("-n", "--name", help="Name of the database")
    db_create.add_argument("-u", "--user", help="Database user")
    db_create.add_argument("-P", "--password", help="Database password")
    db_create.add_argument(
        "-e",
        "--engine_id",
        help="ID of the database engine",
        default=ENGINES_ID[0]["id"],
        required=False,
    )
    db_create.add_argument(
        "--volume_size",
        type=int,
        help="Size of the volume in GB",
        default=10,
        required=False,
    )

    db_delete = db_subparsers.add_parser("delete", help="Delete a database")
    db_help = db_subparsers.add_parser("help", help="Help for database commands")

    # Comando 'application'
    app_parser = subparsers.add_parser("application", help="Application commands")
    app_subparsers = app_parser.add_subparsers(dest="subcommand")

    app_list = app_subparsers.add_parser("list", help="List all applications")
    app_create = app_subparsers.add_parser("create", help="Create a new application")
    app_delete = app_subparsers.add_parser("delete", help="Delete an application")
    app_help = app_subparsers.add_parser("help", help="Help for application commands")

    app_create.add_argument(
        "-n", "--name", help="Name of the application", required=True
    )
    app_create.add_argument(
        "-u", "--user", help="User of the application", required=True
    )
    app_create.add_argument(
        "-p", "--password", help="Password of the application", required=True
    )
    app_create.add_argument(
        "-c", "--code", help="Code of the application", required=True
    )
    app_create.add_argument("-k", "--ssh_key_name", help="SSH key name", required=True)

    # storage_key_id
    app_create.add_argument(
        "-s", "--storage_key_id", help="Storage key id", required=True
    )
    # strage_key_secret
    app_create.add_argument(
        "-ss", "--storage_key_secret", help="Storage key secret", required=True
    )

    # ssh_private_key_path
    app_create.add_argument("-sp", "--ssh_private_key_path", help="SSH private key path", required=True)

    # Comando 'volume'
    volume_parser = subparsers.add_parser("volume", help="Volume commands")
    volume_subparsers = volume_parser.add_subparsers(dest="subcommand")

    volume_list = volume_subparsers.add_parser("list", help="List all volumes")
    volume_create = volume_subparsers.add_parser("create", help="Create a new volume")
    volume_delete = volume_subparsers.add_parser("delete", help="Delete a volume")
    volume_help = volume_subparsers.add_parser("help", help="Help for volume commands")

    volume_create.add_argument(
        "-n", "--volume_name", help="Name of the volume", required=True
    )
    volume_create.add_argument(
        "-s", "--volume_size", help="Size of the volume in GB", type=int, default=10
    )

    # Comando 'storage

    storage_parser = subparsers.add_parser("storage", help="Storage commands")
    storage_subparsers = storage_parser.add_subparsers(dest="subcommand")

    storage_list = storage_subparsers.add_parser(
        "list", help="List all storage profiles"
    )
    storage_create = storage_subparsers.add_parser(
        "create", help="Create a new storage"
    )

    storage_create.add_argument("-n", "--name", help="Name of the storage")
    storage_create.add_argument("-s", "--key-key", help="Secret Key of the storage")
    storage_create.add_argument("-i", "--key-id", help="Bucket of the storage")

    # Comando 'machine'
    machine_parser = subparsers.add_parser("machine", help="Machine commands")
    machine_subparsers = machine_parser.add_subparsers(dest="subcommand")

    machine_list = machine_subparsers.add_parser(
        "list", help="List all machine profiles"
    )
    machine_create = machine_subparsers.add_parser(
        "create", help="Create a new machine"
    )

    # Adicionando argumentos para o comando machine create
    machine_create.add_argument("-n", "--name", help="Name of the virtual machine")
    machine_create.add_argument(
        "-m",
        "--machine_name",
        help="Machine type name",
        default=MACHINES[0]["name"],
        required=False,
    )
    machine_create.add_argument(
        "-i",
        "--image_name",
        help="Image name",
        default=SYSTEMS[0]["name"],
        required=False,
    )
    machine_create.add_argument(
        "-k", "--ssh_key_name", help="SSH key name", required=True
    )

    # Parse os argumentos
    args = parser.parse_args()

    # Se não houver argumentos, exibe a ajuda
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    # Se o comando for fornecido, mas não o subcomando
    if args.command and not args.subcommand:
        subparser = subparsers.choices.get(args.command)
        if subparser:
            subparser.print_help()
            sys.exit(1)

    # Lógica para o comando db
    if args.command == "db":
        if args.subcommand == "list":
            profiles = list_database_profiles()
            print("Database Profiles:")
            if args.all:
                for profile in profiles:
                    print(
                        f"- {profile['label']} (ID: {profile['id']}, vCPU: {profile['vcpu']}, RAM: {profile['ram']}GB, Application: {profile['application']})"
                    )
            else:
                for profile in profiles:
                    print(
                        f"- {profile['label']} Application: {profile['application']})"
                    )
        elif args.subcommand == "create":
            print("engine_id: {}".format(args.engine_id))
            script = generate_terraform_script(
                flavor_id=args.flavor_id,
                db_name=args.name,
                user=args.user,
                password=args.password,
                engine_id=args.engine_id,
                volume_size=args.volume_size,
            )
            print("Generated Terraform Script:")
            print(script)

    # Lógica para o comando machine
    elif args.command == "machine":
        if args.subcommand == "list":
            profiles = list_machine_profiles()
            print("Machine Profiles:")
            if args.all:
                for profile in profiles:
                    print(
                        f"- {profile['name']} (RAM: {profile['ram']}GB, vCPUs: {profile['vcpus']}, Disk: {profile['disk']}GB, GPU: {profile['gpu']})"
                    )
            else:
                for profile in profiles:
                    print(
                        f"- {profile['name']} (RAM: {profile['ram']}GB, vCPUs: {profile['vcpus']})"
                    )
        elif args.subcommand == "create":
            script = generate_machine_terraform_script(
                name=args.name,
                machine_name=args.machine_name,
                image_name=args.image_name,
                ssh_key_name=args.ssh_key_name,
            )
            print("Generated Terraform Script:")
            print(script)

    elif args.command == "volume":
        if args.subcommand == "create":
            script = generate_disk_terraform_script(
                volume_name=args.volume_name, volume_size=args.volume_size
            )
            print("Generated Terraform Script:")
            print(script)

    elif args.command == "application":
        if args.subcommand == "list":
            print("Applications:")
            for profile in PROFILES:
                print(
                    f"- ID: {profile['id']}, Application: {profile['name']}, CODE: {profile['code']}"
                )
        elif args.subcommand == "create":
            script = generate_terraform_script(
                profile_code=args.code,
                user=args.user,
                name=args.name,
                password=args.password,
                ssh_key_name=args.ssh_key_name,
                storage_key_id=args.storage_key_id,
                storage_key_secret=args.storage_key_secret,
                ssh_private_key_path=args.ssh_private_key_path,
            )
            os.makedirs(f"{args.name}", exist_ok=True)
            file = open(f"{args.name}/{args.name}.tf", "w")
            file.write(script)
            file.close()
            os.chdir(f"{args.name}")
            os.system(f"terraform init")
            os.system(f"terraform apply -auto-approve")
            print("Application created successfully")

    elif args.command == "storage":
        if args.subcommand == "create":
            script = generate_storage_terraform_script(
                bucket_name=args.name,
                key_id=args.key_id,
                key_secret=args.key_secret,
            )
            print("Generated Terraform Script:")
            print(script)

    # Exibir os comandos e subcomandos
    print(f"Command: {args.command}")
    if args.subcommand:
        print(f"Subcommand: {args.subcommand}")


if __name__ == "__main__":
    main()
