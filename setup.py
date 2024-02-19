from setuptools import setup

setup(
    name="xapian-binding-python",
    description="Xapian bidding compilation for python",
    # It is version of the compiled code.
    version="1.4.24",
    packages=[
        'xapian'
    ],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ]
)
