from setuptools import setup, find_packages

setup(
    name="SMP",
    version="0.1.0",
    description="School Management Program",
    author="Yazan-Dev9",
    author_email="yksy.dev@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
        "flet"
    ],
    zip_safe=True,
    include_package_data=True,
    package_data={
        "": ["*.json"],
        "smp": ["*.json"],
        "smp.interface.storage.data": ["*.db"],
    },
    entry_points={
        "console_scripts": [
            "smp=smp.interface.cli:main",
            "smp-gui=smp.interface.gui:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="GPL-3.0",
    keywords="school management program",
    url="https://github.com/Yazan-Dev9/Students_Manager-SMP",
    project_urls={
        "Source": "https://github.com/Yazan-Dev9/Students_Manager-SMP",
        "Bug Tracker": "https://github.com/Yazan-Dev9/Students_Manager-SMP/issues",
    },
    long_description=open("README.md").read(),
)
