from setuptools import setup

from frida_push import __version__

setup(
    name='frida-push',
    version=__version__,
    packages=['frida_push'],
    url='https://github.com/AndroidTamer/frida-push',
    license='GPLv3',
    author='AndroidTamer',
    author_email='github@androidtamer.com',
    description='Wrapper tool to identify the remote device and push device specific frida-server binary.',
    install_requires=['requests', 'frida', 'backports.lzma', 'future'],
    entry_points={
        'console_scripts': [
            'frida-push = frida_push.command:main'
        ]
    }
)
