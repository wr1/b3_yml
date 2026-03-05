# b3-yml

Reusable YAML blade configurations, airfoils and polars for the b3m wind-turbine blade framework.

## Installation
```bash
uv pip install -e ".[dev]"
```

## Usage
```python
from b3_yml import prepare_dataset, load_yaml, get_path

yml_path = prepare_dataset("blade_test")
config = load_yaml("blade_test")
```

## Testing
```bash
uv run pytest          # clean run (uses pythonpath + src-layout fix)
uv run pytest -v
uv run pytest --cov
```

**Note**: The `pythonpath = ["src"]` + `sources = ["src"]` config fixes the common `ModuleNotFoundError: No module named 'b3_yml'` when running tests with `uv run pytest` in src-layout packages.