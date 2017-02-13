# /bin/bash

echo "Changing config_production.yaml to config.yaml"

mv config.yaml config_dev.yaml
mv config_production.yaml config.yaml

echo "Success"
