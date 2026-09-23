from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# ==========================================
# Home / Dashboard
# ==========================================

@app.route("/")
def home():

    # --------------------------------------
    # Get filter values
    # --------------------------------------

    placement_filter = request.args.get("placement", "All")

    min_cgpa = request.args.get("min_cgpa", "")

    internship_filter = request.args.get("internship", "All")

    min_projects = request.args.get("min_projects", "")

    page = request.args.get("page", 1, type=int)

    per_page = 20

    offset = (page - 1) * per_page

    college_id = request.args.get("college_id", "")


    # --------------------------------------
    # Connect to Database
    # --------------------------------------

    conn = sqlite3.connect("students.db")


    # ======================================
    # Dashboard Statistics
    # ======================================

    stats_query = """
    SELECT
        COUNT(*) AS total_students,

        SUM(
            CASE
                WHEN Placement = 'Yes' THEN 1
                ELSE 0
            END
        ) AS placed_students,

        ROUND(
            100.0 *
            SUM(
                CASE
                    WHEN Placement = 'Yes' THEN 1
                    ELSE 0
                END
            ) / COUNT(*),
            2
        ) AS placement_rate

    FROM students
    """

    stats = conn.execute(stats_query).fetchone()


    # ======================================
    # Student Records Query
    # ======================================

    query = """
    SELECT
        College_ID,
        CGPA,
        Internship_Experience,
        Projects_Completed,
        Communication_Skills,
        Placement

    FROM students

    WHERE 1=1
    """

    params = []


    # ======================================
    # Placement Filter
    # ======================================

    if placement_filter in ["Yes", "No"]:

        query += " AND Placement = ?"

        params.append(placement_filter)


    # ======================================
    # Minimum CGPA Filter
    # ======================================

    if min_cgpa:

        query += " AND CGPA >= ?"

        params.append(float(min_cgpa))


    # ======================================
    # Internship Filter
    # ======================================

    if internship_filter in ["Yes", "No"]:

        query += " AND Internship_Experience = ?"

        params.append(internship_filter)


    # ======================================
    # Minimum Projects Filter
    # ======================================

    if min_projects:

        query += " AND Projects_Completed >= ?"

        params.append(int(min_projects))


    # ======================================
    # College ID Filter
    # ======================================

    if college_id:

        query += " AND College_ID = ?"

        params.append(college_id)


    # ======================================
    # Count Actual Matching Students
    # ======================================

    count_query = """
    SELECT COUNT(*)

    FROM students

    WHERE 1=1
    """

    count_params = []


    # Placement filter for count

    if placement_filter in ["Yes", "No"]:

        count_query += " AND Placement = ?"

        count_params.append(placement_filter)


    # CGPA filter for count

    if min_cgpa:

        count_query += " AND CGPA >= ?"

        count_params.append(float(min_cgpa))


    # Internship filter for count

    if internship_filter in ["Yes", "No"]:

        count_query += " AND Internship_Experience = ?"

        count_params.append(internship_filter)


    # Projects filter for count

    if min_projects:

        count_query += " AND Projects_Completed >= ?"

        count_params.append(int(min_projects))


    # College ID filter for count

    if college_id:

        count_query += " AND College_ID = ?"

        count_params.append(college_id)


    # Get actual filtered count

    filtered_students = conn.execute(
        count_query,
        count_params
    ).fetchone()[0]


    # ======================================
    # Get Student Records
    # ======================================

    # Show maximum 20 records

    query += " LIMIT ? OFFSET ?"

    params.append(per_page)
    params.append(offset)

    students = conn.execute(
        query,
        params
    ).fetchall()


    # ======================================
    # Close Database
    # ======================================

    conn.close()


    # ======================================
    # Send Data to HTML
    # ======================================

    return render_template(

        "index.html",

        total_students=stats[0],

        placed_students=stats[1],

        placement_rate=stats[2],

        students=students,

        placement_filter=placement_filter,

        min_cgpa=min_cgpa,

        internship_filter=internship_filter,

        min_projects=min_projects,

        college_id=college_id,

        filtered_students=filtered_students,
        
        page=page,

        per_page=per_page
    )


# ==========================================
# Run Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)