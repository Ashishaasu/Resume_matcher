from django.shortcuts import render
from django.http import HttpResponse
import PyPDF2
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Helper functions to extract text from files
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    document = Document(file)
    return '\n'.join([paragraph.text for paragraph in document.paragraphs])

def calculate_match_percentage(text1, text2):
    """Calculate similarity percentage between two texts using TF-IDF."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity * 100, 2)  # Convert to percentage


# View logic
def match_view(request):
    if request.method == 'POST':
        try:
            # Get the uploaded files
            resume_file = request.FILES.get('resume')
            job_description_file = request.FILES.get('job_description')

            if not resume_file or not job_description_file:
                return HttpResponse("Both files are required.", status=400)

            # Determine the file type and process accordingly
            resume_text = ''
            job_description_text = ''

            if resume_file.name.endswith('.pdf'):
                resume_text = extract_text_from_pdf(resume_file)
            elif resume_file.name.endswith('.docx'):
                resume_text = extract_text_from_docx(resume_file)
            else:
                resume_text = resume_file.read().decode('utf-8', errors='ignore')  # Fallback for plain text files

            if job_description_file.name.endswith('.pdf'):
                job_description_text = extract_text_from_pdf(job_description_file)
            elif job_description_file.name.endswith('.docx'):
                job_description_text = extract_text_from_docx(job_description_file)
            else:
                job_description_text = job_description_file.read().decode('utf-8', errors='ignore')  # Fallback for plain text files

            # Calculate match percentage
            match_percentage = calculate_match_percentage(resume_text, job_description_text)

            return HttpResponse(f"Match Percentage: {match_percentage}%")
        except Exception as e:
            return HttpResponse(f"Error processing files: {e}", status=500)

    return render(request,'upload.html')
