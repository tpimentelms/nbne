from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='nbne',
      version='0.81',
      description='Method to create representations for nodes in a graph, using Neighbor Based Node Embeddings (NBNE) method.',
      long_description=readme(),
      keywords='graphs node embeddings machine learning link prediction',
      url='https://github.com/tiagopms/nbne',
      author='Tiago Pimentel',
      author_email='tpimentelms@gmail.com',
      license='MIT',
      packages=['nbne'],
      # scripts=['nbne'],
      entry_points={
          'console_scripts': [
              'nbne=nbne.get_embeddings:main',
          ],
      },
      install_requires=[
          'networkx',
          'gensim'
      ],
      zip_safe=False)