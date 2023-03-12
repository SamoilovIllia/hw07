from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='0.6.6.6',
    entry_points={'console_skripts':['clean-folder = clean_folder.clean:my_main_script']},
    include_package_data=True)