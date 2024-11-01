from core.constants import PROFILES, DISKS, MACHINES, SYSTEMS, FLAVORS_IDS, ENGINES_ID


def list_profiles():
    """
    Retorna uma lista de perfis disponíveis.
    """
    return [
        f"- ID: {profile["id"]}, Application: {profile["application"]}, CODE: {profile["code"]}"
        for profile in PROFILES
    ]
