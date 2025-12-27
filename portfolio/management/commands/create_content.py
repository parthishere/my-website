import os
from datetime import date
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Create a new project or experience markdown file'

    def add_arguments(self, parser):
        parser.add_argument(
            'content_type',
            type=str,
            choices=['project', 'experience'],
            help='Type of content to create (project or experience)'
        )
        parser.add_argument(
            'title',
            type=str,
            help='Title of the project or experience'
        )
        parser.add_argument(
            '--category',
            type=str,
            default='Development',
            help='Category (for projects)'
        )
        parser.add_argument(
            '--company',
            type=str,
            help='Company name (for experiences)'
        )
        parser.add_argument(
            '--location',
            type=str,
            default='Remote',
            help='Location (for experiences)'
        )

    def handle(self, *args, **options):
        content_type = options['content_type']
        title = options['title']

        # Generate slug from title
        slug = self.slugify(title)

        # Determine directory and template
        if content_type == 'project':
            directory = os.path.join(settings.BASE_DIR, 'content', 'projects')
            template = self.get_project_template(title, options)
        else:
            directory = os.path.join(settings.BASE_DIR, 'content', 'experiences')
            template = self.get_experience_template(title, options)

        # Ensure directory exists
        os.makedirs(directory, exist_ok=True)

        # Create file
        filepath = os.path.join(directory, f'{slug}.md')

        if os.path.exists(filepath):
            raise CommandError(f'File already exists: {filepath}')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {content_type}: {filepath}')
        )
        self.stdout.write(
            self.style.WARNING(f'Remember to edit the file and add your content!')
        )

    def slugify(self, text):
        """Convert text to a slug"""
        import re
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')

    def get_project_template(self, title, options):
        """Generate project template"""
        today = date.today().strftime('%Y-%m-%d')
        category = options.get('category', 'Development')

        return f"""Title: {title}
Date: {today}
Category: {category}
Featured: false

## Overview

Write a brief overview of your project here. Explain:

- What problem does it solve?
- Who is it for?
- What makes it unique?

## Key Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Technical Implementation

Describe the technical aspects:

### Architecture
How is the system designed?

### Key Technologies
What technologies are used and why?

### Challenges
What difficulties did you overcome?

## Technologies Used

```json
{{
  "primary_language": "Python",
  "technologies": [
    {{
      "name": "Django",
      "icon": "fab fa-python",
      "color": "#092E20",
      "proficiency": 90
    }},
    {{
      "name": "PostgreSQL",
      "icon": "fas fa-database",
      "color": "#336791",
      "proficiency": 85
    }}
  ]
}}
```

## Results & Impact

- **Metric 1**: Quantifiable result
- **Metric 2**: User impact
- **Metric 3**: Performance improvement

## Links

- **Live Demo**: https://example.com
- **GitHub**: https://github.com/yourusername/project
- **Documentation**: https://docs.example.com

## Future Enhancements

- Planned feature 1
- Planned feature 2
- Planned feature 3
"""

    def get_experience_template(self, title, options):
        """Generate experience template"""
        today = date.today().strftime('%Y-%m-%d')
        company = options.get('company', 'Company Name')
        location = options.get('location', 'Remote')

        return f"""Title: {title}
Date: {today}
EndDate: Present
Location: {location}
Type: Full-time

## Role Overview

Describe your role and primary responsibilities in 2-3 sentences.

## Key Responsibilities

- Led development of critical features
- Managed team members and projects
- Architected and implemented solutions
- Collaborated with cross-functional teams

## Major Achievements

### Project 1: Achievement Title
Brief description of what you accomplished.

- Specific outcome 1
- Specific outcome 2
- Quantifiable result

### Project 2: Another Achievement
Another significant accomplishment.

- Technical implementation
- Team collaboration
- Business impact

## Technologies & Skills

```json
{{
  "primary_languages": ["Python", "JavaScript"],
  "technologies": [
    {{
      "name": "Django",
      "icon": "fab fa-python",
      "color": "#092E20",
      "proficiency": 95
    }},
    {{
      "name": "React",
      "icon": "fab fa-react",
      "color": "#61DAFB",
      "proficiency": 90
    }},
    {{
      "name": "PostgreSQL",
      "icon": "fas fa-database",
      "color": "#336791",
      "proficiency": 85
    }}
  ]
}}
```

## Impact & Metrics

- Improved system reliability by X%
- Reduced deployment time by Y hours
- Mentored N team members
- Delivered M major features

## Team & Collaboration

- Team size and structure
- Cross-functional collaboration
- Leadership responsibilities
- Mentorship activities
"""
