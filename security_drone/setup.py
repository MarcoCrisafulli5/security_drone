from setuptools import setup

package_name = 'security_drone'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name, package_name + '.sim.nodes'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['sim/launch/factory.launch.py']),
        ('share/' + package_name + '/worlds', ['sim/worlds/factory.world']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Marco Crisafulli',
    maintainer_email='51f9ioi9p@mozmail.com',
    description='Mesh + drone security',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = security_drone.sim.nodes.camera_node:main',
            'yolo_node = security_drone.sim.nodes.yolo_node:main',
        ],
    },
)