# SportShoeWorld

## Introduction

SportShoeWorld is a Django-based web application designed to showcase and manage a catalog of sports shoes.
The project demonstrates modular Django architecture, database modeling, and structured application design.

## Features

*   **Shoe Catalog:** Browse a wide variety of sports shoes with detailed information for each model.
*   **Categories:** Filter shoes by sport categories like Basketball, Volleyball, Handball, and Football.
*   **Gender-Specific Filtering:** View shoes available for Men, Women, or Unisex.
*   **Detailed Shoe View:** Get more information about a specific shoe, including its price, size, and description.
*   **Admin Interface:** A dedicated admin panel for managing the shoe inventory, reviews, and more.

## Project Structure

SportShoeWorld/

├── accounts/          # Non-authenticated user accounts

├── shoes/          # Shoe catalog app

├── reviews/        # Reviews functionality

├── common/         # Shared utilities

├── templates/      # Global templates

├── static/         # Static files

├── media/          # Uploaded images

└── manage.py

## Technologies Used

*   **Python:** The core programming language for the backend.
*   **Django:** A high-level Python web framework for rapid development.
*   **PostgreSQL:** A powerful, open-source object-relational database system.
*   **HTML/CSS:** For structuring and styling the frontend.
*   **Pillow:** A Python Imaging Library for handling image uploads.
*   **django-unfold:** For a modern and responsive admin interface.

## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)
*   PostgreSQL

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/KaloyanEnchev/sportshoeworld.git
    cd SportShoeWorld
    ```

2.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    *   Create a PostgreSQL database for the project.
    *   Create a `.env` file in the project root and add your database credentials, following the example in `.env.template`.

5.  **Run the database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Start the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the application by navigating to `http://127.0.0.1:8000` in your web browser. From there, you can browse the shoe catalog, by creating a user.
