from setuptools import setup

setup(
    name = 'API-Airtable',
    version = '1.0',
    install_requires = ['Click',],
    py_modules = ['run', 'API_airtable', 'settings', 'SQL_model'],
    entry_points = '''
    [console_scripts]
    runairtable=run:runairtable
    '''
)