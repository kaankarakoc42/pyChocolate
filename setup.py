from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyChocolate',
  version='0.0.2',
  project_urls = {
  'Github': 'https://www.github.com/kaankarakoc42/pyChocolate'
  },
  description='debugger and logger for python',
  long_description="github source for more details.",
  url='',  
  author='Mevlüt Kaan Karakoç',
  author_email='karakockaan326@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='debugger-logger', 
  packages=find_packages(),
  install_requires=['colorama'] 
)
