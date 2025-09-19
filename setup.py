from setuptools import setup, find_packages

setup(
    name='vehicle-cv-adas',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.22.1',
        'opencv-python>=4.5.4',
        'onnx>=1.12.0',
        'onnxruntime>=1.12.0',
        'torch>=1.11.0',
        'torchvision>=0.12.0',
        'scipy',
        'addict',
        'numba',
        'lap',
        'torchsummary',
    ],
    python_requires='>=3.8',
)