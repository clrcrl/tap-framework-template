{%- set endpoints = cookiecutter.endpoints_csv.split(',') | sort() -%}
{%- for endpoint in endpoints %}
from {{ cookiecutter.package_name }}.streams.{{ endpoint }} import {{ endpoint.title() }}Stream
{%- endfor %}

AVAILABLE_STREAMS = [
{%- for endpoint in endpoints %}
    {{ endpoint.title() }}Stream,
{%- endfor %}
]

__all__ = [
{%- for endpoint in endpoints %}
    "{{ endpoint.title() }}Stream",
{%- endfor %}
]
