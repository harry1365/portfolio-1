from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

filename = 'Harry Resume.pdf'
doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='MyTitle', fontSize=26, leading=32, alignment=TA_CENTER, spaceAfter=18, textColor=colors.HexColor('#0f172a')))
styles.add(ParagraphStyle(name='MyHeading', fontSize=16, leading=20, spaceBefore=16, spaceAfter=10, textColor=colors.HexColor('#1d4ed8')))
styles.add(ParagraphStyle(name='MyBody', fontSize=11.5, leading=16, textColor=colors.HexColor('#172554')))
styles.add(ParagraphStyle(name='MySmall', fontSize=10, leading=14, textColor=colors.HexColor('#475569')))

story = []
story.append(Paragraph('Harsh Rasal', styles['MyTitle']))
story.append(Paragraph('AI & Machine Learning Diploma Student | Full-Stack Developer', styles['MyBody']))
story.append(Spacer(1, 12))

story.append(Paragraph('<b>Contact</b>', styles['MyHeading']))
contact_data = [
    ['Location:', 'Mumbai, India'],
    ['Email:', 'harshrasal17@gmail.com'],
    ['Alternate Email:', '438jhondhale@gmail.com'],
    ['Phone:', '+91 79777 24822'],
    ['LinkedIn:', 'linkedin.com/in/harsh-rasal-557a27382'],
    ['GitHub:', 'github.com/harry1365'],
]
table = Table(contact_data, colWidths=[1.3 * inch, 4.7 * inch], hAlign='LEFT')
table.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#0f172a')),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10.5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
story.append(table)
story.append(Spacer(1, 14))

story.append(Paragraph('<b>Profile Summary</b>', styles['MyHeading']))
story.append(Paragraph('AI & Machine Learning diploma student with a strong foundation in logical problem-solving, rapid prototyping, and collaborative development. I turn AI concepts into production-ready full-stack solutions.', styles['MyBody']))
story.append(Spacer(1, 12))

story.append(Paragraph('<b>Education</b>', styles['MyHeading']))
story.append(Paragraph('Diploma in Artificial Intelligence & Machine Learning<br/>S.H. Jondhale Polytechnic, Dombivli | 2024 - Present<br/>Current: 2nd Year · 72% aggregate', styles['MyBody']))
story.append(Spacer(1, 12))

story.append(Paragraph('<b>Core Skills</b>', styles['MyHeading']))
skills = ['Java', 'JavaScript', 'Python', 'C', 'HTML5', 'CSS3', 'Spring Boot', 'Next.js', 'React', 'Node.js', 'JWT Auth', 'REST APIs', 'Integration Testing', 'ML Concepts', 'Algorithmic Thinking']
story.append(Paragraph(', '.join(skills), styles['MyBody']))
story.append(Spacer(1, 12))

story.append(Paragraph('<b>Featured Projects</b>', styles['MyHeading']))
project_list = [
    ('Jarvis AI Engine', 'High-throughput AI engine built for fast token generation and efficient inferencing across large parameter counts.'),
    ('AI Content PRO Platform', 'Full-stack platform with Spring Boot backend and Next.js frontend, featuring JWT authentication and performance-first UI design.'),
    ('InfiniCode Ecosystem', 'Platform focused on backend reliability, environment scalability, and team-friendly workflows.'),
    ('Console Checkers Engine', 'Command-line game engine in C with board tracking, move validation, and optimized decision flow.'),
]
for title, desc in project_list:
    story.append(Paragraph(f'<b>{title}</b>', styles['MyBody']))
    story.append(Paragraph(desc, styles['MySmall']))
    story.append(Spacer(1, 8))

story.append(Spacer(1, 12))
story.append(Paragraph('<b>GitHub Repositories</b>', styles['MyHeading']))
repo_list = [
    ('rocketride-server', 'AI pipeline engine with C++ core and Python integration.'),
    ('ai-llm-', 'Vercel deployment project for AI frontend applications.'),
    ('base-sepolia-', 'Blockchain and Ethereum tooling work.'),
    ('college-pro', 'Academic and college project work.'),
    ('Jrvis', 'AI automation and tooling experiment.'),
    ('tech-spur', 'AWS and cloud-focused development work.'),
]
for title, desc in repo_list:
    story.append(Paragraph(f'<b>{title}</b> — {desc}', styles['MySmall']))
    story.append(Spacer(1, 6))

story.append(Spacer(1, 12))
story.append(Paragraph('<b>Goals</b>', styles['MyHeading']))
story.append(Paragraph('Advance UI/UX design, cloud deployment, scalable microservices, and advanced neural networks.', styles['MyBody']))

# Build PDF

doc.build(story)
print(f'Generated {filename}')
