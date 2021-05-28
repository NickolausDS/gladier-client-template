import os
from setuptools import setup, find_packages

# single source of truth for package version
version_ns = {}
with open(os.path.join('gladier-client', 'version.py')) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)

setup(
    name='gladier-client',
    description='The Gladier Client Template',
    url='https://github.com/globus-gladier/gladier-client-template',
    maintainer='The Gladier Team',
    maintainer_email='',
    version=version,
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/gladier_*'],
    install_requires=install_requires,
    dependency_links=[],
    license='Apache 2.0',
    classifiers=[]
)
