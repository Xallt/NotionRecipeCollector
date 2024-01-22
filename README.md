# Notion Recipe Collector

Project intented to eventually deploy a fancy home menu to a website.
Mini-repo with a Ruby gem intended to be imported into a Jekyll website.

- Python script that gets recipe data from the Notion API
- Ruby gem with a single class that uses the Python script to return the recipes

## Setup

Shouldn't need any &mdash; just a Python 3.8+ interpreter and the `requests` library

## Usage

```bash
NOTION_API_KEY=<your key> python print_recipes.py
```

## References

- [Notion API Reference](https://developers.notion.com/)
