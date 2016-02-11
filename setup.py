from setuptools import setup, find_packages

entry_points = '''
[console_scripts]
run_script = project_rename.script:main
'''

required = '''
setuptools
requests
python-dateutil
'''


setup(
    name = 'project-rename',
    version = '0.0',
    description = 'Unknown',
    author = 'Author name',
    packages = find_packages('project_rename'),
    package_dir = {'': '.'},
    install_requires = [x.strip() for x in required.split('\n') if x != ''],
    entry_points=entry_points,
)

