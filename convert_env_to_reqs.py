import yaml

def convert_environment_yml_to_requirements(env_file, output_file):
    with open(env_file, "r") as f:
        env_data = yaml.safe_load(f)

    pip_packages = env_data.get("dependencies", [])
    pip_list = []
    for dep in pip_packages:
        if isinstance(dep, str):  # Non-pip package
            pip_list.append(dep)
        elif isinstance(dep, dict) and "pip" in dep:
            pip_list.extend(dep["pip"])

    with open(output_file, "w") as f:
        f.write("\n".join(pip_list))

convert_environment_yml_to_requirements("environment.yml", "requirements.txt")
