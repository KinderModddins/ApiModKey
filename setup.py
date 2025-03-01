from setuptools import setup, find_packages

setup(
    name="ApiModkey",
    version="0.1.9",
    author="MAKCNMOB",
    author_email="support@gmail.com",
    description="Библиотека для использования апи от Modkey.space",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://modkey.space/",  # Замени на свою ссылку
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
