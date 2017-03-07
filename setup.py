from setuptools import setup

setup(
    name="pycparserlibc",
    description="pycparser extension that includes fake_libc_include",
    license='MIT',
    version='0.1',
    author='Sungkwang Lee',
    maintainer='Sungkwang Lee',
    author_email='gwangyi.kr@gmail.com',
    url='https://github.com/gwangyi/pycparserlibc',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',],
    install_requires=['pycparser>=2.17'],
    packages=['pycparserlibc'],
)
