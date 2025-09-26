# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based bilingual landing page for AVOCTECHS, a technology consulting company. The application features:

- **Flask Web Application**: Simple single-file Flask app with internationalization support
- **Bilingual Support**: Spanish (default) and English language switching
- **Landing Page**: Company services showcase with contact form
- **Responsive Design**: Bootstrap 5 with custom CSS animations

## Architecture

### Core Components

- `app.py`: Main Flask application with all routes, translations, and business logic
- `templates/index.html`: Single Jinja2 template for the entire landing page
- `static/style.css`: Custom CSS with CSS variables, animations, and responsive design
- `static/hero-background.webp.png`: Hero section background image

### Key Architecture Patterns

- **Internationalization**: Uses Flask-Babel with inline translations dictionary in `app.py` (lines 24-78)
- **Language Routing**: Dynamic routes support language codes (`/` defaults to Spanish, `/en` for English)
- **Translation System**: Text content stored in nested dictionaries by language in `app.py`
- **Contact Form**: Simple POST endpoint that prints form data to console (no database)

## Development Commands

### Running the Application
```bash
python3 app.py
```
This starts the Flask development server with debug mode enabled on default port 5000.

### Dependencies
The project requires:
- Flask 2.2.5+
- Flask-Babel (for internationalization)

Install dependencies with:
```bash
pip3 install flask flask-babel
```

## File Structure

```
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Single page template
└── static/
    ├── style.css         # Custom styles and animations
    └── hero-background.webp.png  # Hero background image
```

## Key Features

### Language Support
- Language switching via URL routes (`/` for Spanish, `/en` for English)
- Translations stored in `texts` dictionary in `app.py`
- Language selector dropdown in navigation

### Contact Form
- Form submissions handled by `/contact` POST route
- Form data is printed to console (no email/database integration)
- Returns success message in user's selected language

### Styling System
- CSS custom properties for consistent theming (`:root` variables)
- Intersection Observer API for scroll animations
- Bootstrap 5 for responsive grid and components
- Custom hover effects and transitions

## Development Notes

- No build process required - static files served directly
- No database - contact form only logs to console
- No testing framework currently implemented
- Single-file application architecture for simplicity