#!/bin/bash

# Setup script for SMP (Students Manager Project Software)
echo "Setting up SMP (Students Manager Project Software)..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Installing Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get install -y python3-pip
fi

if ! command -v pyinstaller &> /dev/null; then
    echo " is pyinstallernot installed. Installing pip3..."
    sudo pip3 install pyinstaller
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install the package in development mode
echo "Installing SMP package..."
#pip3 install -e .

# Initialize the database
echo "Initializing database..."
echo "Initializing app..."
pyinstaller ./src/smp/__main__.py -F
cd ./dist
mkdir bin
mv __main__ ./bin/smp
chmod u+x smp

echo "Setup completed successfully!"
echo "You can now run SMP using the following commands:"
echo "- Command line interface: dist/bin/smp"
echo "- Graphical user interface: smp-gui"