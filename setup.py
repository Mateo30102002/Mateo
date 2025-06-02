from setuptools import setup, find_packages

setup(
    name="vope__cedo_ProyectoMateo",
    version="0.0.1",
    author="Mateo Romero",
    author_email="",
    description="",
    py_modules=["actividad_1","actividad_2"],
    install_requires=[
        "pandas==2.2.3",
        "openpyxl",
        "requests==2.32.3",
        "beautifulsoup4==4.13.3",
        "jupyter"
    ]
) 