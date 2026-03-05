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
uv run pytest          # runs with coverage + logfire plugin disabled (fixes common env issues)
uv run pytest -v       # verbose output
uv run pytest --cov    # coverage only
```

The `-p no:logfire` flag in the config automatically disables any stray `logfire` pytest plugin (common when mixing conda + uv).