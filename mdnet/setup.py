from setuptools import setup, find_packages

setup(
        name = "mdnet",
        version = "0.1",
        packages = find_packages(),
        entry_points = {
            "console-scripts": [
                "mdnet = mdnet:main",
            ],
        },
        install_requires = [
            "markdown",
            "jinja2",
            "python-frontmatter",
        ],
)
