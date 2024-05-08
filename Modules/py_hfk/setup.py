from setuptools import setup, Extension

setup (
    ext_modules=[
        Extension(
            name = 'py_hfk',
            version = '1.0',
            description = 'Computes Heegaard Floer homology for links',
            sources = ['py_hfkmodule.cpp'],
        ),
    ]
)
