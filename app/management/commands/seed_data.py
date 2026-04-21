"""
Management command to seed the database with resume data.
Run: python manage.py seed_data
"""
import sys
import io
from django.core.management.base import BaseCommand
from app.models import (
    Profile, Education, Experience, Project,
    SkillCategory, Skill, Certification, Language
)


class Command(BaseCommand):
    help = "Seeds the database with Phanindra's portfolio data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('[*] Seeding portfolio data...'))

        # ── Profile ──────────────────────────────────────
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            name='Phanindra Varma Gunturi',
            title='Aspiring Software Developer | Python & Django | Web Applications',
            bio=(
                'Passionate Computer Science Engineering student with strong skills in '
                'Python and Django. Experienced in building real-world applications, '
                'including internship experience as a Full Stack Developer at Fratello '
                'Innotech Pvt Ltd. I love turning ideas into robust web applications and '
                'am always eager to learn new technologies.'
            ),
            email='phanindravarmagunturi@gmail.com',
            location='Hyderabad, India',
            github_url='https://github.com/',
            linkedin_url='https://linkedin.com/in/',
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Profile created'))

        # ── Education ────────────────────────────────────
        Education.objects.all().delete()
        Education.objects.create(
            degree='B.Tech – Computer Science Engineering',
            institution='ANITS (Anil Neerukonda Institute of Technology & Sciences)',
            start_year='2025',
            end_year='2028',
            cgpa='8.3',
            description='Currently pursuing B.Tech in CSE with focus on software development, algorithms, and database management.',
            order=1,
        )
        Education.objects.create(
            degree='Diploma – Computer Science Engineering',
            institution='AANM & VVRSR Polytechnic',
            start_year='2022',
            end_year='2025',
            cgpa='9.5',
            description='Completed Diploma in CSE with distinction. Built a strong foundation in programming, web development, and database systems.',
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Education created'))

        # ── Experience ───────────────────────────────────
        Experience.objects.all().delete()
        Experience.objects.create(
            role='Full Stack Developer Intern',
            company='Fratello Innotech Pvt Ltd',
            duration='6 Months',
            description=(
                'Built full-stack web applications using Django and Python\n'
                'Worked with MySQL databases for data storage and management\n'
                'Developed responsive UI using HTML, CSS, and JavaScript\n'
                'Delivered a complete Online Locker Booking System from design to deployment\n'
                'Collaborated with a team following agile development practices'
            ),
            order=1,
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Experience created'))

        # ── Projects ─────────────────────────────────────
        Project.objects.all().delete()
        Project.objects.create(
            title='Online Locker Booking System',
            description=(
                'A full-featured locker management web application with real-time '
                'availability tracking, secure user authentication, online booking '
                'system, and a comprehensive admin panel for locker management.'
            ),
            tech_stack='Django, Python, MySQL, HTML, CSS, JavaScript, Bootstrap',
            github_url='https://github.com/',
            featured=True,
            order=1,
        )
        Project.objects.create(
            title='Money Saver – Personal Finance Tracker',
            description=(
                'A personal finance management application that helps users track '
                'expenses, set savings goals, and view analytics dashboards. '
                'Features beautiful charts and category-based expense tracking.'
            ),
            tech_stack='Django, Python, SQLite, Chart.js, HTML, CSS, JavaScript',
            github_url='https://github.com/',
            featured=True,
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Projects created'))

        # ── Skills ───────────────────────────────────────
        SkillCategory.objects.all().delete()

        lang_cat = SkillCategory.objects.create(name='Languages', icon='fas fa-code', order=1)
        Skill.objects.create(category=lang_cat, name='Python', proficiency=90, order=1)
        Skill.objects.create(category=lang_cat, name='Java', proficiency=70, order=2)
        Skill.objects.create(category=lang_cat, name='C', proficiency=72, order=3)
        Skill.objects.create(category=lang_cat, name='JavaScript', proficiency=75, order=4)

        fw_cat = SkillCategory.objects.create(name='Frameworks', icon='fas fa-layer-group', order=2)
        Skill.objects.create(category=fw_cat, name='Django', proficiency=88, order=1)
        Skill.objects.create(category=fw_cat, name='Node.js', proficiency=65, order=2)
        Skill.objects.create(category=fw_cat, name='Express.js', proficiency=62, order=3)
        Skill.objects.create(category=fw_cat, name='React.js', proficiency=60, order=4)

        fe_cat = SkillCategory.objects.create(name='Frontend', icon='fas fa-palette', order=3)
        Skill.objects.create(category=fe_cat, name='HTML', proficiency=92, order=1)
        Skill.objects.create(category=fe_cat, name='CSS', proficiency=85, order=2)
        Skill.objects.create(category=fe_cat, name='Tailwind CSS', proficiency=78, order=3)

        db_cat = SkillCategory.objects.create(name='Databases', icon='fas fa-database', order=4)
        Skill.objects.create(category=db_cat, name='MySQL', proficiency=82, order=1)
        Skill.objects.create(category=db_cat, name='SQLite', proficiency=85, order=2)
        Skill.objects.create(category=db_cat, name='MongoDB', proficiency=60, order=3)

        self.stdout.write(self.style.SUCCESS('  [OK] Skills created'))

        # ── Certifications ───────────────────────────────
        Certification.objects.all().delete()
        Certification.objects.create(
            title='Smart India Hackathon – Participant',
            issuer='Government of India',
            description='Participated in one of the largest hackathons in the world, developing innovative solutions for national challenges.',
            order=1,
        )
        Certification.objects.create(
            title='AWS Cloud Workshop',
            issuer='Amazon Web Services',
            description='Completed hands-on AWS Cloud workshop covering core cloud computing concepts, S3, EC2, and Lambda services.',
            order=2,
        )
        Certification.objects.create(
            title='Hackathon Organizer',
            issuer='AANM & VVRSR Polytechnic',
            description='Organized and managed a college-level hackathon, coordinating participants, mentors, and judging panels.',
            order=3,
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Certifications created'))

        # ── Languages ────────────────────────────────────
        Language.objects.all().delete()
        Language.objects.create(name='Telugu', proficiency='native', order=1)
        Language.objects.create(name='English', proficiency='professional', order=2)
        Language.objects.create(name='Hindi', proficiency='limited', order=3)
        Language.objects.create(name='Oriya', proficiency='basic', order=4)
        self.stdout.write(self.style.SUCCESS('  [OK] Languages created'))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('[DONE] All data seeded successfully!'))
        self.stdout.write(self.style.WARNING(
            '[NEXT] Run: python manage.py createsuperuser  then visit /admin to manage content'
        ))
