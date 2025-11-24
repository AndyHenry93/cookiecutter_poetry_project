project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.author_name }}"
version = "0.1.0"
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",      # Google/NumPy docstrings
    "sphinx.ext.viewcode",      # Add "View Source" links
    "sphinx.ext.autodoc.typehints",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

# You can write docs in either .rst or .md (if using MyST parser)
# Uncomment if you want Markdown support:
# extensions.append("myst_parser")
# source_suffix = {
#     ".rst": "restructuredtext",
#     ".md": "markdown",
# }

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"  # You can change the theme here
html_static_path = ["_static"]

# -- Autodoc settings --------------------------------------------------------

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

autodoc_typehints = "description"  # Cleaner function signatures

# -- Path Setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath("../src"))
# This allows Sphinx to import your project modules from "src/"