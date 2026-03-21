# Source: https://scikit-learn.org/1.8/developers/development_setup.html#setup-development-environment

# Step 1: clone the scikit-learn repo and check out the latest release tag
git clone https://github.com/scikit-learn/scikit-learn.git

cd scikit-learn

git fetch --tags
git tag  # you can run it is see which branches are available in your terminal, exit with q

git checkout 1.8.0

git status  # expected: HEAD detached at 1.8.0

# Step 2: Create and activate a new virtual environment
# macOS instructions (see the link above for other operating systems)
xcode-select --install
brew install libomp

brew install pyenv

pyenv virtualenv 3.12 sklearn-env
pyenv activate sklearn-env

pip install wheel numpy scipy cython meson-python ninja \
  pytest pytest-cov ruff==0.11.2 mypy numpydoc \
  joblib threadpoolctl pre-commit

pip install --editable ".[examples,tests]" \
  --verbose --no-build-isolation \
  --config-settings editable-verbose=true

# Step 3: Check your installation
python -c "import sklearn; sklearn.show_versions()"

pytest
