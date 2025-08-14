# Configuration file for the Sphinx documentation builder.

import os
import sys
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
    # GitHub pages
    "sphinx.ext.githubpages",
    # CodeRefinery lesson structure
    "sphinx_lesson",
    # Theme accessibility fixes
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinx_coderefinery_branding",
    # Math support
    "sphinx.ext.mathjax",
    # MyST Markdown parser
    "myst_parser",
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

# Enable MyST extensions (including LaTeX math support)
myst_enable_extensions = [
    "amsmath",    # AMS LaTeX math environments
    "dollarmath", # Inline and block math with $...$ and $$...$$
]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

# HTML context
from os.path import basename, dirname, realpath

html_context = {
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

if os.environ.get('GITHUB_REF', '') == 'refs/heads/' + github_version:
    html_js_files = [
        (
            'https://plausible.cs.aalto.fi/js/script.js',
            {"data-domain": "coderefinery.github.io", "defer": "defer"}
        ),
    ]
