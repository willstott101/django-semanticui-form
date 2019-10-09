from setuptools import setup, find_packages
from semanticuiform.meta import VERSION

setup(
    name='django-semanticui-form-2.0',
    version=str(VERSION),
    description="django-semanticui-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='SemanticUI,django,Semantic,Fomantic',
    author='Maxim Harder',
    author_email='maxim_harder@jas.de',
    url='https://github.com/Gokujo/django-semanticui-form',
    license='BSD',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=2.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
