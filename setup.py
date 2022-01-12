from setuptools import setup

package_name = 'natural_number_pubsub_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsc',
    maintainer_email='chulslee20@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'natural_number_generator = natural_number_pubsub_python.natural_number_generator:main',
            'sum_calculator = natural_number_pubsub_python.sum_calculator:main',
            'factorial_calculator = natural_number_pubsub_python.factorial_calculator:main',

        ],
    },
)
