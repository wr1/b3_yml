# Blade Configuration Project

This project contains configuration files for blade design, particularly for wind turbine blades.

## blade_test.yml

The `data/blade_test.yml` file defines the parameters for a blade test configuration.

### Sections:

- **workdir**: Working directory for the simulation.

- **geometry**: Defines the blade's geometric properties.
  - **planform**: Includes npchord, npspan, pre_rotation, dx, dy, z, chord, thickness, twist.
  - **airfoils**: List of airfoils with path, name, thickness.

- **bem**: Blade Element Momentum parameters like rated_power, polars, B, rho, etc.

- **structure**: Structural elements like webs.

- **mesh**: Meshing parameters.

- **matdb**: Material database.

- **laminates**: Laminate definitions.
