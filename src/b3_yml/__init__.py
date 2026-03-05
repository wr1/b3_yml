from importlib.resources import files
from pathlib import Path
import shutil
import yaml
from typing import Any

__version__ = "0.1.0"


def get_data_dir() -> Path:
    """Return root path to the installed data directory."""
    return files("b3_yml") / "data"


def get_path(*parts: str) -> Path:
    """Return path to any file or folder inside data/."""
    return get_data_dir().joinpath(*parts)


def load_yaml(name: str) -> dict[str, Any]:
    """Load a YAML dataset (name without .yml)."""
    path = get_path(f"{name}.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def prepare_dataset(name: str, target_dir: Path | None = None) -> Path:
    """Copy complete dataset (YAML + airfoils/ + polars/) to target_dir for tests/examples."""
    if target_dir is None:
        target_dir = Path.cwd() / f"temp_{name}"
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy main YAML
    yml_src = get_path(f"{name}.yml")
    yml_dest = target_dir / f"{name}.yml"
    shutil.copy2(yml_src, yml_dest)

    # Copy supporting directories
    for sub in ("airfoils", "polars"):
        src = get_path(sub)
        if src.exists():
            dest = target_dir / sub
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)

    # Update workdir key in the copied YAML (if present)
    config = load_yaml(name)
    if "workdir" in config:
        config["workdir"] = str(target_dir)
        with open(yml_dest, "w", encoding="utf-8") as f:
            yaml.dump(config, f, sort_keys=False)

    return yml_dest
