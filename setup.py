#!/usr/bin/env python3

from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(name="vcmgmt",
      version="0.0.1",
      description="vCenter administration tool.",
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
          "Development Status :: 5 - Production/stable",
          "License :: OSI Approved :: MIT Locense",
          "Promgramming Language :: Python :: 3",
          "Operating System :: OS Independant"
      ],
      url="https://github.com",
      author="Collin Leishman",
      author_email="collinleishman@gmail.com",
      keywords="core package",
      licence="MIT",
      packages=["vc_manager"],
      install_requires=[
          "certifi==2020.12.5",
          "chardet==4.0.0",
          "idna==2.10",
          "requests==2.25.1",
          "urllib3==1.26.4"
      ],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          "console_scripts": [
              'vcmgmt = vc_manager.vcmgmt:main'
          ]
      }
      )
