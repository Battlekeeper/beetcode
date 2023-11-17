#/bin/bash
node .output/server/index.mjs & python3 backend/api.py && fg