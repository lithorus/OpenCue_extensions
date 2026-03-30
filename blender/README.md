
## Environment setup 

The `OpenCueBlender` directory needs to be added to the `BLENDER_SYSTEM_SCRIPTS` environment variable.

The addon expects to be run in an environment python environment that already has `outline` installed with it's depencies.

### Example Startup Script
```bash
#!/bin/bash

OPENCUE_BLENDER_DIR="<Absolute Path Of the blender Directory>"

export BLENDER_SYSTEM_SCRIPTS="${OPENCUE_BLENDER_DIR}/OpenCueBlender"
export PYTHONPATH="${OPENCUE_BLENDER_DIR}:${PYTHONPATH}"

# --python-use-system-env is used for blender to pick up PYTHONPATH
blender --python-use-system-env "$@"
```
