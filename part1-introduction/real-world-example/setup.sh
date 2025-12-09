git clone https://github.com/scikit-learn/scikit-learn.git

cd scikit-learn
git tag
git fetch --tags
git checkout 1.6.1
git status  # expected: HEAD detached at 1.6.1

# > from https://scikit-learn.org/1.6/developers/advanced_installation.html:
# (make sure to start from a clean python env!)

brew install pyenv-virtualenv

pyenv virtualenv 3.12.3 sklearn-env
pyenv activate sklearn-env

pip install wheel numpy scipy cython meson-python ninja

# > Install a compiler with OpenMP support for your platform - see scikit-learn documentation link

# cd scikit-learn if not already there!
make clean
pip install --editable ".[examples,tests]" \
   --verbose --no-build-isolation \
   --config-settings editable-verbose=true

python -c "import sklearn; sklearn.show_versions()"
