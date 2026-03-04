from setuptools import find_packages, setup


setup(
    name="lang-seg",
    packages=find_packages(include=["lang_seg"]),
    install_requires=[
        "pytorch-lightning",
        "openai-clip",
        "torch-encoding @ git+https://github.com/zhanghang1989/PyTorch-Encoding",
        "pandas"
    ]
)