import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = "CONAN1"
copyright = "KushalDey02"
author = "Kushal Dey"
github_user = "KushalDey02"
github_repo_name = "CONAN1"
github_version = "main"
conf_py_path = "/content/"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinx_coderefinery_branding",
    "sphinx.ext.mathjax",   # MathJax for LaTeX in HTML
    "myst_parser",          # MyST Markdown parser with math support
]

# MyST configuration for math
myst_enable_extensions = [
    "amsmath",     # Allow LaTeX amsmath
    "dollarmath",  # Support $...$ and $$...$$
]

# Don't redefine .md if already set
# Sphinx will detect `.rst` and `.md` automatically via myst_parser
# No need for: source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}

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

# HTML context
from os.path import basename, dirname, realpath
html_context = {
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

if os.environ.get('GITHUB_REF', '') == 'refs/heads/' + github_
