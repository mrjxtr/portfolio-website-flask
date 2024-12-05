from flask import render_template
from app.main import bp
from datetime import datetime

@bp.route('/')
def index():
    projects = [
        {
            "title": "Web Automation",
            "description": "Automated testing and web scraping solutions using Selenium",
            "tech": ["Selenium", "Python", "BeautifulSoup", "Pytest"]
        },
        {
            "title": "Data Science & Analytics", 
            "description": "AI/ML solutions for data analysis and predictive modeling",
            "tech": ["Python", "TensorFlow", "Scikit-learn", "Pandas"]
        },
        {
            "title": "Web Development",
            "description": "Full-stack web applications with Python frameworks",
            "tech": ["Django", "Flask", "PostgreSQL", "REST APIs"]
        }
    ]
    
    testimonials = [
        {
            "text": " Jester is a great developer. He helped me with my project and delivered exactly what I needed. He is very professional and communicative. I would definitely work with him again. ",
            "author": "Upwork Client",
            "role": "Web Automation Project"
        },
        {
            "text": " Jester did an excellent job on my project. He was very responsive and delivered high-quality work. I highly recommend him for any data science needs. ",
            "author": "Upwork Client",
            "role": "Data Analytics Project"
        },
        {
            "text": " Great communication and technical skills. Delivered the project ahead of schedule with excellent quality. Would definitely work with him again. ",
            "author": "Upwork Client",
            "role": "Django Development"
        }
    ]
    
    return render_template('index.html', 
                         projects=projects, 
                         testimonials=testimonials,
                         now=datetime.now()) 
