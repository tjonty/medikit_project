# Medikit 🩺  
**Your Health, Centralized and Accessible**  

## Current Status ⏳  
Medikit was deployed on Heroku but is now archived due to Heroku’s free tier discontinuation. The source code and screenshots remain available, demonstrating my ability to build practical, impactful applications.

## About Medikit 🏥  
Medikit is a Django-based web application designed to centralize patients’ medical data, offering a single gateway for doctors, pathologists, and patients to manage and access health information. Doctors and pathologists can upload prescriptions, medication details, and pathology results, which patients can later view to better understand their health history. Previously live on Heroku, Medikit is now archived due to Heroku ending its free tier, but it remains a standout project in my portfolio for its real-world utility and technical sophistication.

### Why It Matters 💡  
- **Centralized Records**: Consolidates prescriptions, medications, and test results in one secure place.  
- **Improved Care**: Enables doctors to make informed decisions with access to past treatment data.  
- **Health Education**: Features an articles section for doctors and authors to share insights.  
- **Professional Directory**: Connects users with doctors, pathologists, and hospitals.  
- **Secure & User-Friendly**: Prioritizes privacy and ease of use for all stakeholders.  

## Motivation 💪  
Patients often struggle to recall their treatment history, and without this information, doctors may lack critical context about past medications, adverse effects, or conditions. Medikit addresses this by providing a simple, secure online platform to store and retrieve medical data, enhancing treatment accuracy and patient outcomes.

## Features 📋  
- **Record Management**: Upload, store, view, and edit medical records online.  
- **Health Articles**: Doctors and authors can publish articles to improve health literacy.  
- **Directory**: Searchable list of doctors, pathologists, and hospitals.  
- **Secure Access**: Role-based authentication for patients, doctors, and pathologists.  
- **Email Notifications**: Alerts for uploads and updates via SendGrid integration.  

## Tech Stack 🧰  
- **Framework**: [Django (Python 3)***REMOVED***(https://docs.djangoproject.com/en/3.2/intro/tutorial01/)  
- **Database**: [MongoDB***REMOVED***(https://www.mongodb.com) (via Djongo)  
- **Frontend**: HTML, CSS, JavaScript, [Bootstrap 4***REMOVED***(https://getbootstrap.com/docs/4.0/getting-started/introduction/)  
- **Email**: [SendGrid***REMOVED***(https://sendgrid.com) for notifications  
- **Form Rendering**: [Crispy Forms***REMOVED***(https://django-crispy-forms.readthedocs.io/en/latest/)  
- **Deployment**: Heroku (archived)  

## Architecture Highlights 🏗️  
- **Django MVT**: Clean Model-View-Template structure for maintainability.  
- **MongoDB**: NoSQL database for flexible, scalable storage of medical data.  
- **Authentication**: Django’s built-in system with role-based access control.  
- **Media Handling**: Secure uploads and storage of medical documents.  
- **Email Integration**: Automated notifications using SendGrid’s SMTP service.  

## Screenshots 📷  
- **Home Page**  
  <img width="1508" alt="Home Page" src="https://user-images.githubusercontent.com/47101523/145343130-ce671d59-8c8d-4881-93d9-a4317e2502fa.png">  
- **Signup/Login Page**  
  <img width="1511" alt="Signup/Login Page" src="https://user-images.githubusercontent.com/47101523/145341249-74853654-57c6-4df2-a188-2bb66f394ea4.png">  
- **Patient’s Report**  
  <img width="1504" alt="Patient's Report" src="https://user-images.githubusercontent.com/47101523/145343105-e35aeb3b-7afb-45ae-a08f-718b29db8b1d.png">  
- **Doctor List**  
  <img width="1501" alt="Doctor List" src="https://user-images.githubusercontent.com/47101523/145343184-14cd1c6d-be35-4c6a-9fdd-5e2da983a08b.png">  
- **Articles**  
  <img width="1508" alt="Articles" src="https://user-images.githubusercontent.com/47101523/145362475-14d41524-347a-433c-9685-df36a31cddcc.png">  

## Lessons Learned 📚  
- Mastered full-stack development with Django and MongoDB.  
- Gained experience integrating third-party APIs like SendGrid.  
- Learned to implement role-based access control for multiple user types.  
- Improved skills in secure file handling and media uploads.  
- Enhanced UI/UX design with Bootstrap and Crispy Forms.  

## Setup & Deployment ⚙️  
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-repo/medikit.git
   ```  
2. **Install Dependencies**
3. **Set Environment Variables**:  
   - `SECRET_KEY`: Your Django secret key  
   - `SEND_GRID_API_KEY`: SendGrid API key for email  
   - Update other email settings (e.g., `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`)  
4. **Run Migrations**:  
   ```bash
   python manage.py migrate
   ```  
5. **Start the Server**:  
   ```bash
   python manage.py runserver
   ```  
6. **Access Locally**: Visit `http://localhost:8000` in your browser.  

## Contributing 🧨  
I welcome feedback! Feel free to open issues or submit pull requests to collaborate.

## About Me 🧑‍💻  
Check out my [portfolio***REMOVED***(https://jontytejani.com) for more projects!
