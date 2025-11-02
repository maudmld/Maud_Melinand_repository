import json
from pathlib import Path


def generate_html():
    with open('students.json', 'r', encoding='utf-8') as f:
        students = json.load(f)

    students_sorted = sorted(students, key=lambda s: (s['nom'], s['prenom']))

    students_html = ""
    for student in students_sorted:
        students_html += f"""
        <div class="student-card">
            <div class="student-emoji">{student['emoji']}</div>
            <div class="student-info">
                <h3>{student['prenom']} {student['nom']}</h3>
                <p class="student-promo">Promo {student['promo']}</p>
                <p class="student-matiere">Matière préférée : {student['matiere_preferee']}</p>
                <a href="{student['github_page']}" target="_blank" class="student-link">
                    Voir le site →
                </a>
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio de la Promo 2025</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            color: white;
            margin-bottom: 3rem;
        }}

        h1 {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}

        .subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}

        .stats {{
            text-align: center;
            color: white;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }}

        .students-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }}

        .student-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            gap: 1rem;
        }}

        .student-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}

        .student-emoji {{
            font-size: 3rem;
            flex-shrink: 0;
        }}

        .student-info {{
            flex: 1;
        }}

        .student-info h3 {{
            color: #2c3e50;
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }}

        .student-promo {{
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 0.3rem;
        }}

        .student-matiere {{
            color: #34495e;
            margin-bottom: 1rem;
            font-size: 0.95rem;
        }}

        .student-link {{
            display: inline-block;
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.2s;
        }}

        .student-link:hover {{
            color: #764ba2;
        }}

        footer {{
            text-align: center;
            color: white;
            padding: 2rem;
            opacity: 0.8;
        }}

        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}

            .students-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 Portfolio de la Promo 2025</h1>
            <p class="subtitle">Découvrez les sites personnels de vos camarades</p>
        </header>

        <div class="stats">
            {len(students)} étudiant{'s' if len(students) > 1 else ''} dans l'annuaire
        </div>

        <div class="students-grid">
            {students_html}
        </div>

        <footer>
            <p>Généré automatiquement via GitHub Actions</p>
            <p>Pour vous ajouter, créez une Pull Request !</p>
        </footer>
    </div>
</body>
</html>
"""

    Path('index.html').write_text(html_content, encoding='utf-8')
    print(f"✅ HTML généré avec succès ({len(students)} étudiants)")


if __name__ == '__main__':
    generate_html()