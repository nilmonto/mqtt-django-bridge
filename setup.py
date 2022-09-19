import os.path
import re
from setuptools import setup, find_packages


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="django_mqtt_bridge",
    version=get_version("django_mqtt_bridge"),
    author="Nilson Oliveira",
    author_email="nilsonmont.o@gmail.com",
    url="https://github.com/nilmonto/mqtt-django-bridge",
    description="Interface MQTT ASGI compatible with Django Channels 3.",
    long_description= open("README.md").read(),
    long_description_content_type="text/markdown",
    license="GPLv3+",
    packages=find_packages(),
    install_requires=[
        "paho-mqtt",
    ],
    entry_points={
        "console_scripts": [
            "django_mqtt_bridge=django_mqtt_bridge.cli:main",
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
