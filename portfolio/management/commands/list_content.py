import os
from django.core.management.base import BaseCommand
from django.conf import settings
from portfolio.utils import get_all_projects, get_all_experiences


class Command(BaseCommand):
    help = 'List all projects and experiences'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['projects', 'experiences', 'all'],
            default='all',
            help='Type of content to list'
        )

    def handle(self, *args, **options):
        content_type = options['type']

        if content_type in ['projects', 'all']:
            self.stdout.write(self.style.SUCCESS('\n=== PROJECTS ==='))
            projects = get_all_projects()
            if not projects:
                self.stdout.write(self.style.WARNING('  No projects found'))
            else:
                for project in projects:
                    self.stdout.write(f"  • {project['name']}")
                    self.stdout.write(f"    Slug: {project['slug']}")
                    metadata = project.get('metadata', {})
                    if 'date' in metadata:
                        self.stdout.write(f"    Date: {metadata['date'][0]}")
                    if 'category' in metadata:
                        self.stdout.write(f"    Category: {metadata['category'][0]}")
                    self.stdout.write('')

        if content_type in ['experiences', 'all']:
            self.stdout.write(self.style.SUCCESS('\n=== EXPERIENCES ==='))
            experiences = get_all_experiences()
            if not experiences:
                self.stdout.write(self.style.WARNING('  No experiences found'))
            else:
                for exp in experiences:
                    self.stdout.write(f"  • {exp['name']}")
                    self.stdout.write(f"    Slug: {exp['slug']}")
                    metadata = exp.get('metadata', {})
                    if 'date' in metadata:
                        self.stdout.write(f"    Date: {metadata['date'][0]}")
                    if 'location' in metadata:
                        self.stdout.write(f"    Location: {metadata['location'][0]}")
                    self.stdout.write('')

        self.stdout.write(self.style.SUCCESS('\nTotal:'))
        if content_type in ['projects', 'all']:
            self.stdout.write(f"  Projects: {len(get_all_projects())}")
        if content_type in ['experiences', 'all']:
            self.stdout.write(f"  Experiences: {len(get_all_experiences())}")
