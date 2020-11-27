from setuptools import setup, find_packages

setup(
    name='ClarkePark',
    version='0.1.2',
    url='https://jacometoss.github.io/ClarkePark/',
    license='GPL-3.0',
    author='Marco Polo Jacome Toss',
    author_email='jacometoss@outlook.com',
    description='Clarke and Park Transforms',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['Clarke and Park Transforms', 'Inverse Park transform', 'transforms', 'Clark', 'Park'],
    packages=find_packages(include=["ClarkePark"]),
    include_package_data=True,
    install_requires=['numpy==1.19.1','matplotlib==3.3.2'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
)

