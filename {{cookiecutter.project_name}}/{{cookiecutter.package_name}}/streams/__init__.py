{#- TODO Figure out a better way to convert snake_case to CamelCase in Jinja -#}
{#- TODO Handle trimming -#}
{%- set endpoints = cookiecutter.endpoints_csv.split(',') | sort() -%}
{%- for endpoint in endpoints %}
from {{ cookiecutter.package_name }}.streams.{{ endpoint }} import {{ endpoint.replace('_', ' ').title().replace(' ', '') }}Stream
{%- endfor %}

AVAILABLE_STREAMS = [
{%- for endpoint in endpoints %}
    {{ endpoint.replace('_', ' ').title().replace(' ', '') }}Stream,
{%- endfor %}
]

__all__ = [
{%- for endpoint in endpoints %}
    "{{ endpoint.replace('_', ' ').title().replace(' ', '') }}Stream",
{%- endfor %}
]
