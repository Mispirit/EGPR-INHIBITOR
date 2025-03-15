import os
import subprocess

# For my project paths
receptor_path = "receptor/3poz.pdbqt" 
ligand_folder = "ligands"
output_folder = "results"
vina_path = "vina"

# Create or direct result folder
os.makedirs(output_folder, exist_ok=True)

# Ligands List
ligands = [f for f in os.listdir(ligand_folder) if f.endswith(".pdbqt")]

# Dock each ligand
for ligand in ligands:
    ligand_path = os.path.join(ligand_folder, ligand)
    ligand_name = os.path.splitext(ligand)[0]  # To Remove .pdbqt extension

    # Creation of unique config file for each ligand
    config_content = f"""
receptor = {receptor_path}
ligand = {ligand_path}
out = {output_folder}/{ligand_name}_out.pdbqt

center_x = 19.543
center_y = 24.708
center_z = 15.191

size_x = 62.0
size_y = 66.0
size_z = 66.0

exhaustiveness = 8
num_modes = 9
energy_range = 3
"""
    config_path = "config.txt"
    with open(config_path, "w") as f:
        f.write(config_content)

    # Run AutoDock Vina
    cmd = f'{vina_path} --config {config_path} --log {output_folder}/{ligand_name}_log.txt'
    subprocess.run(cmd, shell=True)

    print(f"Docking completed for {ligand}")

print("My docking for all ligand is complete")
