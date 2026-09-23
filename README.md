# Student Performance & Placement Analytics Dashboard

A web-based dashboard for analyzing student academic performance and placement data.

## Project Overview

This project analyzes student academic and placement-related data and presents useful insights through an interactive web dashboard.

The application uses Python for data analysis, SQL for data storage and querying, Flask for the backend, and HTML/CSS for the frontend.

## Features

- Student placement statistics
- Placement rate calculation
- CGPA analysis
- Internship experience analysis
- Projects completed analysis
- Communication skills analysis
- Student record filtering
- Placement status filter
- Minimum CGPA filter
- Internship filter
- Minimum projects filter
- College ID search
- Pagination of student records
- Data visualization using charts
- SQLite database integration

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Flask
- SQLite
- SQL
- HTML
- CSS

## Dataset

The project uses a College Student Placement dataset containing academic, skill, internship, project and placement-related information.

### Dataset Columns

- College_ID
- IQ
- Prev_Sem_Result
- CGPA
- Academic_Performance
- Internship_Experience
- Extra_Curricular_Score
- Communication_Skills
- Projects_Completed
- Placement

## Project Structure

```text
StudentAnalysisProject/
│
├── app.py
├── data_analysis.py
├── students.db
├── README.md
│
├── data/
│   └── college_student_placement_dataset.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── placement_status.png
    ├── cgpa_placement.png
    ├── internship_placement.png
    ├── projects_placement.png
    └── communication_placement.png
How to Run
1. Install required libraries

pip install flask pandas numpy matplotlib seaborn

2. Run the Flask application

python app.py

3. Open the application

Open the local Flask URL shown in the terminal, usually:

http://127.0.0.1:5000/

Future Improvements

Machine Learning based placement prediction
Login and authentication
Advanced analytics
More interactive visualizations
Deployment to a cloud platform

Project Status

Ongoing

This project is being developed as a learning and portfolio project to demonstrate skills in Python, SQL, data analysis and web development.