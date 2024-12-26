# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'POLLUX Digital Twin'
copyright = '2024, TNO'
author = 'Ryvo Octaviano, Demetris Palochis, Paul Egberts, Dimitris, Ntagkras, Pejman Shoeibi Omrani, Laura Precupanu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinxcontrib.jquery']

templates_path = ['_templates']
exclude_patterns = []
autoclass_content = 'both'
autodoc_default_options = {

}

# Enable numref
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['']
