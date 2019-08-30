from setuptools import setup, find_packages

setup(
    name             = 'aws-s3-kms-parameter',
    version          = '1.0',
    description      = 'use parameter in S3 with kms',
    author           = 'Kyung Won Na',
    author_email     = 'songew@gmail.com',
    url              = 'https://github.com/rampart81/pyquibase',
    download_url     = 'https://githur.com/rampart81/pyquibase/archive/1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['liquibase', 'db migration'],
    python_requires  = '>=3',
    package_data     =  {
        'pyquibase' : [
            'db-connectors/sqlite-jdbc-3.18.0.jar',
            'db-connectors/mysql-connector-java-5.1.42-bin.jar',
            'liquibase/liquibase.jar'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)