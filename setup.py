from distutils.core import setup
setup(
  name='omega_index',
  packages=['omega_index'],  # this must be the same as the name above
  version='0.3',
  description='Omega Index for evaluation of overlapping community structure',
  author ='Ilias Sarantopoulos',
  author_email ='sarantopoulos.ilias@gmail.com',
  url='https://github.com/isaranto/omega-index',  # use the URL to the github repo
  download_url='https://github.com/isaranto/omega_index/archive/master.zip',  # I'll explain this in a second
  keywords=['evaluation', 'clustering', 'community-detection'],  # arbitrary keywords
  classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: BSD License',

    "Operating System :: OS Independent",

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ],
)
