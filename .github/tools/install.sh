#!/bin/bash

set -e

echo "Upgrading pip."
pip install --upgrade pip

echo "Installing kaggle."
pip install kaggle
