from setuptools import setup

setup(name="meta_policy_search",
      version='0.1',
      description='Framework that provides multiple gradient-based Meta-RL algorithms',
      url='https://github.com/jonasrothfuss/maml-zoo',
      author='Dennis Lee, Ignasi Clavera, Jonas Rothfuss',
      author_email='jonas.rothfuss@berkeley.edu',
      license='MIT',
      packages=['meta_policy_search'],
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[
        'python_dateutil'
      ],
zip_safe=False)
