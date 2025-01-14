import setuptools




__version__ = "0.0.0"

REPO_NAME = "ReBIT-Assg"
AUTHOR_USER_NAME = "Siddharth-Latthe-07"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "siddharthlatthe@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

# we setup src here as local package directory