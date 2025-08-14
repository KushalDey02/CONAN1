# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
from os.path import basename, dirname, realpath

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "CONAN1"
copyright = "KushalDey02"
author = "Kushal Dey"
github_user = "KushalDey02"
github_repo_name = "CONAN1"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/content/"  # with leading and trailing slash

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinx_coderefinery_branding",
    "sphinx.ext.mathjax",
]

# Enable MyST math extensions only if MyST is already loaded from other extensions
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]

nb_execution_mode = "cache"

exclude_patterns = [
    "examples",
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
    "img/README.md",
]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_context = {
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

# Add Plausible analytics only on the main branch
if os.environ.get('GITHUB_REF', '') == 'refs/heads/' + github_version:
    html_js_files = [
        ('https://plausible.cs.aalto.fi/js/script.js', {
            "data-domain": "coderefinery.github.io",
            "defer": "defer"
        }),
    ]
