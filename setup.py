from setuptools import setup, Extension

setup(
    name='wrapper',
    version='1.0',
    description='compare module linux shared object wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Darfi Sultoni',
    author_email='darfisultoni@gmail.com',
    url='https://github.com/n0tlu5/nuitka_example',
    packages=['wrapper'],
    package_data={'wrapper': ['compare_module.cpython-312-x86_64-linux-gnu.so']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
    ],
)

