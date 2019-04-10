from setuptools import setup, find_packages


setup(
    name='jangl-webleads-inbound',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django',
        'djangorestframework',
    ],

    author='Jangl',
    author_email='tech@jangl.com',
    description='Jangl Platform API - Webleads Ping Post Serializers',
    url='https://github.com/jangl-platform/jangl-webleads-inbound',
    license="MIT license",

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
