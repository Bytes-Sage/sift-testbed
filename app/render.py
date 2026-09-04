"""Template rendering for outbound email."""

from jinja2 import Template


def render_welcome(name: str) -> str:
    template = Template("Hello {{ name }}, welcome aboard.")
    return template.render(name=name)
