from setuptools import find_packages, setup

setup(
    name="dlimp",
    version="0.0.2",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "tensorflow==2.19.0",
        "tensorflow_datasets>=4.9.9",
    ],
    extras_require={
        "convert": [
            "tqdm",
            "tqdm-multiprocess==0.0.11",
        ],
        "dev": [
            "pre-commit==3.3.3",
        ],
    },
)
