from setuptools import setup

setup(
        author="Adrian Toral",
        author_email="adriantoral@sertor.es",
        version="1.0.0",
        description="HackMyVM CLI tool",
        name="hackmycli",
        install_requires=["requests", "fire", "gdown", "oh-my-pickledb", "pint", "prettytable"],
        package_dir={"": "src"},
        packages=["hackmycli"],
        entry_points = {
            'console_scripts': [
                'hack=hackmycli.main:main'
                ]
            }
        )
