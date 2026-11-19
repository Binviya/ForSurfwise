# Demo project guide

This repo is used to test the GitHub connector.

## Structure

- `src/utils.py` — Python helpers
- `src/helpers.js` — JavaScript helpers

## JavaScript usage

`src/helpers.js` exports three helpers:

- `add(a, b)` — sum two numbers
- `greet(name)` — build a greeting string
- `slugify(text)` — convert text to a URL-friendly slug, e.g. `"Hello World"` becomes `"hello-world"`

## Notes

The connector should index both code files and markdown docs.
