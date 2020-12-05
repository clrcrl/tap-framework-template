discover:
	{{ cookiecutter.project_name }} -c config.json --discover > catalog.json

discover_and_select:
	{{ cookiecutter.project_name }} -c config.json --discover | jq '.streams[].metadata[0].metadata.selected = true' > catalog.json
