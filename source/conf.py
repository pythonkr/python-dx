# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python DX for Python User Group of Korea'
copyright = '2025, Python User Group Korea'
author = 'Python User Group Korea'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'myst_parser',
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# site maps
# https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html#usage
html_baseurl = 'https://dx.python.or.kr/'
