from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='0.6.6.6',
    author='IlliaSamoilov',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean-folder = clean_folder.clean:my_main_script']})
    # include_package_data=True,
    # install_requires=[        'file_parser',    ])