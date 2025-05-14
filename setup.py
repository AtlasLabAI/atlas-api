from setuptools import find_packages, setup

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="atlas-api",
    version="0.1.0",
    description="A Python wrapper for the Atlas API with synchronous and asynchronous support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Atlas-zk",
    author_email="verscherrer19806@hotmail.com",
    url="https://github.com/AtlasLabAI/atlas-api",
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,  # Include files specified in MANIFEST.in
    install_requires=[
        "requests>=2.25.1",
        "aiohttp>=3.8.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-asyncio>=0.20",
            "black>=23.0",
            "mypy>=1.0",
            "sphinx>=4.5.0",
        ],
        "docs": [
            "sphinx>=4.5.0",
            "sphinx_rtd_theme>=1.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    keywords="Atlas API wrapper, blockchain, AI, Solana",
    project_urls={
        "Documentation": "https://docs.atlaslab.io/",
        "Source": "https://github.com/AtlasLabAI/atlas-api.git",
        "Tracker": "https://github.com/AtlasLabAI/atlas-api/issues",
    },
)
