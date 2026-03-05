# b3-yml

Reusable YAML blade configurations, airfoils and polars for the b3m wind-turbine blade framework.

## Installation
```bash
uv pip install -e ".[dev]"
```

## Usage
```python
from b3_yml import prepare_dataset, load_yaml, get_path

# Recommended for tests/examples
yml_path = prepare_dataset("blade_test")
config = load_yaml("blade_test")
```

## Testing
```bash
uv run pytest -v
# with coverage
uv run pytest --cov
```
