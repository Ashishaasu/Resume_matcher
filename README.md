# Resume_matcher
Resume Matcher
A Django-based web application that compares a resume with a job description and calculates the match percentage using cosine similarity and TF-IDF vectorization.

Features:
>Upload a resume file and a job description file.
>Clean and preprocess textual data.
>Calculate the match percentage between the uploaded files.
>Display results dynamically using cosine similarity.
>Handles file decoding errors and provides debugging capabilities.

Prerequisites:
>Ensure you have the following installed:
Python (3.8 or higher)
Django (4.0 or higher)
Required Python packages (see requirements.txt)

Installation:
1.Clone the repository:
git clone https://github.com/Ashishaasu/resume-matcher.git
cd resume-matcher

2.Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install dependencies:
pip install -r requirements.txt

4.Run migrations:
python manage.py migrate

5.Start the development server:
python manage.py runserver

*Usage:
Open a web browser and go to http://127.0.0.1:8000/.
Upload a resume file (e.g., PDF or plain text) and a job description file.
Click Submit to calculate the match percentage.
View the results on the response page.

*File Structure:
resume-matcher/
├── matcher/                   # Core Django app
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   ├── views.py               # Core logic for file handling and matching
├── resume_matcher/            # Main Django project
├── static/                    # Static files (CSS, JS)
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

*Requirements:
The required Python packages are listed in requirements.txt. Install them using:
pip install -r requirements.txt

*Sample requirements.txt:
Django>=4.0
scikit-learn

*How It Works:
1.Upload: Accepts user-uploaded files for the resume and job description.
2.Preprocessing: Cleans the text by:
    Lowercasing
    Removing punctuation
    Normalizing spaces
3.Vectorization: Converts the text into numerical vectors using TF-IDF.
4.Similarity Calculation: Uses cosine similarity to determine how closely the texts match.
5.Result: Displays the match percentage to the user.

*Example Output:
Match Results:
Files processed successfully.
Match Percentage: 85.76%
