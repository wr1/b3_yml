from pathlib import Path
import yaml
from b3_yml import get_data_dir, load_yaml, prepare_dataset


def test_package_can_be_imported():
    """Basic import sanity."""
    assert get_data_dir is not None


def test_data_structure():
    """All expected YAMLs and support directories are present."""
    data_dir = get_data_dir()
    assert data_dir.exists()
    assert (data_dir / "blade_test.yml").exists()
    assert (data_dir / "blade_test_ribbon.yml").exists()
    assert (data_dir / "airfoils").is_dir()
    assert (data_dir / "polars").is_dir()


def test_load_yaml_blade_test():
    """Load blade_test.yml and verify structure."""
    config = load_yaml("blade_test")
    assert isinstance(config, dict)
    assert config.get("workdir") == "temp_blade"
    assert "geometry" in config
    assert "bem" in config
    assert config["bem"]["B"] == 3
    assert "structure" in config


def test_load_yaml_ribbon():
    """Load blade_test_ribbon.yml and verify ribbon web."""
    config = load_yaml("blade_test_ribbon")
    assert isinstance(config, dict)
    assert config.get("workdir") == "temp_ribbon"
    webs = [w.get("name") for w in config.get("structure", {}).get("webs", [])]
    assert "ribbon1" in webs


def test_prepare_dataset(tmp_path: Path):
    """prepare_dataset creates clean working dir with updated workdir and copied support files."""
    target = tmp_path / "test_blade"
    yml_path = prepare_dataset("blade_test", target_dir=target)

    assert yml_path.exists()
    assert yml_path.name == "blade_test.yml"
    assert (target / "airfoils").is_dir()
    assert (target / "polars").is_dir()

    # workdir key was updated
    with open(yml_path, encoding="utf-8") as f:
        updated = yaml.safe_load(f)
    assert updated["workdir"] == str(target)
