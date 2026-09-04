## Configuration

Sift-testbed reads configuration from `config.yaml` in the project root.
The `timeout` value is in seconds and defaults to 30. To change it, edit
the file directly — there is no environment variable override, and this is
deliberate. See issue #4 for the reasoning.

## Why Flask is pinned

Flask is pinned to 0.12. The 1.0 upgrade changed how blueprints handle
before_request hooks, which broke our auth middleware. Do not bump it
without rewriting `app/auth.py` first.
