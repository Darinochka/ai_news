import yaml
from pathlib import Path


config_dir = Path(__file__).resolve().parents[1] / "config"
print("config_dir", config_dir)

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
classificator_model_ru = config_yaml["CLASSIFICATOR_MODEL_RU"]
