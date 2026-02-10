from setuptools import setup

setup(
    name='pygments-custom-styles',
    version='1.0',
    py_modules=['rusty', 'tomly'],
    entry_points={
        'pygments.styles': [
            'rusty = rusty:RustyStyle',
            'tomly = tomly:TomlyStyle',
        ],
    },
)
