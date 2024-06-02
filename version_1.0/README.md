


# Berich Web-App

### General Information Tab:
Input fields for personal and training session details.
Option to select training module numbers from a dropdown menu.

### Daily Notes Tab
Text areas for entering notes or observations for each weekday.
Inputs are designed to be captured for PDF document generation.

#### Generating Reports
The "Generate Report" button processes the entered information, updating and generating a PDF document that can be downloaded directly. CURRENTLY INACTIVE!

## Getting Started on WINDOWS 

### Prerequisites

Ensure you have Python 3.9 (or higher) and pip installed on your system.

### Setup

To set up the application locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/ColdByDefault/beRichPy.git
```
3. Navigate into the project directory:
```bash
cd version_1.0
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python run.py
```

After these steps, the web-app will be accessible at [http://127.0.0.1:5555/].

### Database Setup

To initialize and prepare the database for first-time use, run the following commands:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```


## Getting Started on macOS or Linux

### Prerequisites
Ensure you have Python 3.9 (or higher) and pip installed on your system. 
You can check your Python version by running python3 --version in your terminal.

### Setup

To set up the application locally on macOS or Linux, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/ColdByDefault/beRichPy.git
```
2. Navigate into the project directory:
```bash
cd version_1.0
```
3. Install the required dependencies:
```bash
pip3 install -r requirements.txt
```
4. Run the application:
```bash
python3 run.py
```
After these steps, the web-app will be accessible at [http://127.0.0.1:5555/].

### Database Setup

To initialize and prepare the database for first-time use, execute the following commands in the terminal:
```bash
export FLASK_APP=run.py
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Usage

After launching the app, you can navigate through the various applications provided in the platform. Ensure you register and log in to access apps that require authentication.




