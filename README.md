# HTML Forms with Flask and SMTP

This repository is a practice project for handling HTML form submissions using Flask. It uses a Bootstrap-based blog template to provide a visually appealing interface for users to contact you. The submitted form data is then sent via email using SMTP.

## Features

- Blog-style template for a contact form (Bootstrap-based).
- Flask server handles HTTP requests for form submission.
- Form data is captured and sent via email using the SMTP protocol.

## Getting Started

### Prerequisites

To run this project, you'll need the following:

- Python 3.x
- Flask
- SMTP email server credentials
- dotenv (to manage environment variables)

### Usage

1. Start the Flask server

   ```sh
   python app.py
  

2. Open your web browser and navigate to http://127.0.0.1:5001 to access the blog and contact form.
3. Fill out the contact form and submit it. If successful, you should see a success message, and an email will be sent to the recipient specified in your .env file.

### Project Structure
- **app.py**: The main Flask application file
- **templates/**: HTML files for rendering the pages, including the blog and contact form.
- **static/**: Static assets such as CSS, JavaScript, and images.

## Acknowledgments

The HTML blog template used in this project was downloaded online and is styled using Bootstrap.

## Disclaimer

This project is for educational purposes only. Ensure you do not share your SMTP credentials publicly, and be mindful of email security.

