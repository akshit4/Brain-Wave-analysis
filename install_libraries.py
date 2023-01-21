import subprocess

def install(package):
    subprocess.check_call([f'pip install {package}'], shell=True)

# List of libraries to be installed
libraries = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'scipy', 'mne', 'gradio ', 'keras']

# Loop through the list and install each library
for library in libraries:
    install(library)
