# E-Ink Display QR Code Project

## Overview
This project enables displaying QR codes on a 2.9-inch E-Ink display using Jetson GPIO and the EPD (E-Paper Display) driver. It's designed to work on Jetson-based systems and provides a complete solution for rendering images on e-ink displays.

## Project Structure
- **epd2in9bc.py** - Driver module for the 2.9" B/C color e-ink display
- **epdconfig.py** - Configuration file for display settings and GPIO pin mappings
- **image_script.py** - Main script to load and display QR code images on the e-ink display
- **requirements.txt** - Python package dependencies

## Requirements
- Python 3.7+
- 2.9" E-Ink B/C display (epd2in9bc)
- GPIO library support

## Installation

### 1. Set up Virtual Environment
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Dependencies include:
- **Pillow** - For image processing and QR code rendering
- **Jetson.GPIO** - GPIO control for Jetson devices
- **gpiozero** - GPIO abstraction layer
- **spidev** - SPI device interface for display communication

## Usage

### Running the Display Script
To display a QR code on the e-ink display:

```bash
source myvenv/bin/activate
python3 image_script.py
```

The script will:
1. Initialize the e-ink display
2. Clear any existing content
3. Load the QR code image from "qr.png"
4. Display the QR code on the e-ink display

### Prerequisites for Running
- Ensure you have a file named **qr.png** in the project directory (or modify image_script.py to load a different image)
- Verify GPIO pins are properly connected to your e-ink display
- Run with appropriate permissions (may require `sudo` depending on GPIO settings)

## Display Specifications
- **Model**: epd2in9bc (2.9-inch B/C color)
- **Resolution**: 296×128 pixels
- **Colors**: Black, White, and one additional color (typically Red)
- **Interface**: SPI

## Configuration
To modify display settings or GPIO pin mappings, edit **epdconfig.py**. The configuration includes:
- SPI bus settings
- GPIO pin assignments
- Display initialization parameters

## Troubleshooting
- If the display doesn't initialize, verify GPIO pin connections
- Check that all dependencies are installed: `pip list`
- Ensure the QR code image file exists and is readable
- Review GPIO permissions if running into permission errors



