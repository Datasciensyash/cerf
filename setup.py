from distutils.core import setup

setup(
    name="cerfblackisort",
    packages=["cerfblackisort"],
    version="0.1",
    license="MIT",
    description="Just run black & isort for me!",
    author="Datasciensyash",
    author_email="idontwannasay@somewhere.com",
    url="https://github.com/datasciensyash/cerf",
    download_url="https://github.com/datasciensyash/cerf/archive/v_01.tar.gz",
    keywords=[
        "BLACK",
        "ISORT",
    ],
    entry_points={
        "console_scripts": [
            "cerf=cerfblackisort.main:main",
        ],
    },
    install_requires=["black", "isort"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
