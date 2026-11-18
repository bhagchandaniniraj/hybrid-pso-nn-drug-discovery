# import json
# import re

# notebook_path = "Impv6.ipynb"
# fixed_path = "Impv6_fixed.ipynb"

# def remove_surrogates(obj):
#     if isinstance(obj, str):
#         # Strip surrogate characters (\ud800 - \udfff)
#         return re.sub(r'[\ud800-\udfff]', '', obj)
#     elif isinstance(obj, list):
#         return [remove_surrogates(item) for item in obj]
#     elif isinstance(obj, dict):
#         return {k: remove_surrogates(v) for k, v in obj.items()}
#     return obj

# print(f"🔍 Repairing {notebook_path}...")

# try:
#     with open(notebook_path, "r", encoding="utf-8", errors="surrogateescape") as f:
#         nb_data = json.load(f)

#     clean_nb_data = remove_surrogates(nb_data)

#     with open(fixed_path, "w", encoding="utf-8") as f:
#         json.dump(clean_nb_data, f, indent=1)

#     print(f"✅ Successfully repaired! Open: {fixed_path}")
# except Exception as e:
#     print(f"❌ Error repairing file: {e}")


### Installing CUDA Graphics Card ####
# wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
# dpkg -i cuda-keyring_1.1-1_all.deb
# apt update

apt-get update && apt-get install -y libcublas-12-0