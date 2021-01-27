from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tickets',
    version='0.1.0',
    author='Robert Graf',
    author_email='ragraf@juno.com',
    description='A utility for tracking work tickets,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/grafbob/tickets',
    packages=find_packages('src')
)

