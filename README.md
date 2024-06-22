# Animal Prediction Deployment

This repository contains the code and resources for deploying an animal prediction model using Flask and TensorFlow.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project deploys a machine learning model that predicts animal species from images. The deployment is done using Flask, making the model accessible via a web interface.

## Features

- **Image Upload**: Upload an image to get the animal species prediction.
- **Real-time Prediction**: Get predictions instantly after uploading the image.
- **Pre-trained Model**: Utilizes a pre-trained VGG16 model for animal classification.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mthanhlm/animal_predict_deloy.git
   cd animal_predict_deloy
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

## Usage

1. **Start the Flask server**:
   After running `python app.py`, the server will start at `http://127.0.0.1:3000/`.

2. **Upload an Image**:
   Open your web browser and go to `http://127.0.0.1:3000/`. You can upload an image and get the predicted animal species.

## File Structure

```plaintext
.
├── __pycache__/
├── static/
│   └── uploads/
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── README.md
├── requirements
```

- **`__pycache__/`**: Directory containing Python bytecode files.
- **`static/uploads/`**: Directory for storing uploaded images.
- **`templates/`**: Directory for HTML templates.
- **`.gitignore`**: Git ignore file.
- **`app.py`**: Main application file.
- **`requirements`**: Contains the list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
