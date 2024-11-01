import sys
import argparse
from database import generate_terraform_script, list_database_profiles
from machine import generate_machine_terraform_script, list_machine_profiles
from constants import FLAVORS_IDS, ENGINES_ID, MACHINES, SYSTEMS, DISKS


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

    # Comando 'vm'
    vm_parser = subparsers.add_parser("vm", help="Virtual Machine commands")
    vm_subparsers = vm_parser.add_subparsers(dest="subcommand")

    vm_list = vm_subparsers.add_parser("list", help="List all virtual machines")
    vm_create = vm_subparsers.add_parser("create", help="Create a new virtual machine")
    vm_delete = vm_subparsers.add_parser("delete", help="Delete a virtual machine")
    vm_help = vm_subparsers.add_parser("help", help="Help for virtual machine commands")

    # Comando 'volume'
    volume_parser = subparsers.add_parser("volume", help="Volume commands")
    volume_subparsers = volume_parser.add_subparsers(dest="subcommand")

    volume_list = volume_subparsers.add_parser("list", help="List all volumes")
    volume_create = volume_subparsers.add_parser("create", help="Create a new volume")
    volume_delete = volume_subparsers.add_parser("delete", help="Delete a volume")
    volume_help = volume_subparsers.add_parser("help", help="Help for volume commands")

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
            for profile in profiles:
                print(
                    f"- {profile['label']} (ID: {profile['id']}, vCPU: {profile['vcpu']}, RAM: {profile['ram']}GB, Application: {profile['application']})"
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
            for profile in profiles:
                print(
                    f"- {profile['name']} (RAM: {profile['ram']}GB, vCPUs: {profile['vcpus']}, Disk: {profile['disk']}GB, GPU: {profile['gpu']})"
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

    # Exibir os comandos e subcomandos
    print(f"Command: {args.command}")
    if args.subcommand:
        print(f"Subcommand: {args.subcommand}")


if __name__ == "__main__":
    main()
