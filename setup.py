import os, glob
from setuptools import setup, find_packages


install_requires = (
    'psycopg2',
    )
description = "Migration utilties for cnx-user"

setup(
    name='cnx-user-migrations',
    version='0.1',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/cnx-user-migrations",
    license='LICENSE.txt',
    description=description,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    entry_points="""\
    [console_scripts]
    cnx-user-migrate = cnxuser_migrations.cli:main
    """,
    )
