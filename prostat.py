'''
Prostat - A project status tool for the command line.

Usage:
    prostat.py <project folder> 
        -h | --help         - Show this screen.
        -v | --version      - Show version.
        -s | --status       - Show project status.
        -d | --date         - Show oldest and newest date.
        -l | --lines        - Show total lines of code.
        -f | --files        - Show total files.
        -F | --folders      - Show total folders.
        -S | --structure    - Show project structure.
        -a | --all          - Show all project information.


'''

from argparse import ArgumentParser
from datetime import datetime
import os
import sys
import os


class Prostat:
    '''The main class for Prostat.'''

    def __init__(self, path: str = './', ignore: list[str] = []) -> None:
        '''Initialize the Prostat class.'''
        self.path = path
        self.ignore = ignore
        # Check if the .gitignore file exists, if so, add it to the ignore list
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                self.ignore.extend(f.read().splitlines())

    def get_oldest_date(self):
        '''Get the oldest date from the project files.'''
        pass

    def get_newest_date(self):
        '''Get the newest date from the project files.'''
        pass

    def get_project_status(self):
        '''Get the project status.'''
        pass

    def get_project_structure(self):
        '''Get the project structure.'''

        def list_files(startpath):
            '''List all files with folder recursively.'''
            prefix = '|__'
            for root, dirs, files in os.walk(startpath):
                level = root.replace(startpath, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print(f'{indent}{prefix}{os.path.basename(root)}/')
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    if not any([f.endswith(pattern) for pattern in self.ignore]):
                        print(f'{subindent}{prefix}{f}')

        # Call the list_files function
        list_files(self.path)

    def get_total_lines_of_code(self):
        '''Get the total lines of code.'''

    def get_total_files(self):
        '''Get the total files.'''
        pass

    def get_total_folders(self):
        '''Get the total folders.'''
        pass


class ProstatCLI:
    '''The command line interface for Prostat.'''

    def __init__(self):
        '''The ProstatCLI class for the command line interface.'''

        self.prostat = Prostat()
        self.parser = ArgumentParser(
            description='A project status tool for the command line.',
            usage='prostat.py <project folder> [-h | --help] [-v | --version] [-s | --status] [-d | --date] [-l | --lines] [-f | --files] [-F | --folders] [-S | --structure] [-a | --all]'
        )
        self.parser.add_argument('project_folder', help='The project folder.')
        self.parser.add_argument(
            '-v', '--version', action='version', version='%(prog)s 0.1')
        self.parser.add_argument(
            '-s', '--status', action='store_true', help='Show project status.')
        self.parser.add_argument(
            '-d', '--date', action='store_true', help='Show oldest and newest date.')
        self.parser.add_argument(
            '-l', '--lines', action='store_true', help='Show total lines of code.')
        self.parser.add_argument(
            '-f', '--files', action='store_true', help='Show total files.')
        self.parser.add_argument(
            '-F', '--folders', action='store_true', help='Show total folders.')
        self.parser.add_argument(
            '-S', '--structure', action='store_true', help='Show project structure.')
        self.parser.add_argument(
            '-a', '--all', action='store_true', help='Show all project information.')
        self.args = self.parser.parse_args()

    def run(self):
        '''Run the command line interface.'''

        if len(sys.argv) == 1:
            self.parser.print_help()
            sys.exit(1)

        if self.args.status:
            self.prostat.get_project_status()
        elif self.args.date:
            self.prostat.get_oldest_date()
            self.prostat.get_newest_date()
        elif self.args.lines:
            self.prostat.get_total_lines_of_code()
        elif self.args.files:
            self.prostat.get_total_files()
        elif self.args.folders:
            self.prostat.get_total_folders()
        elif self.args.structure:
            self.prostat.get_project_structure()
        elif self.args.all:
            self.prostat.get_project_status()
            self.prostat.get_oldest_date()
            self.prostat.get_newest_date()
            self.prostat.get_total_lines_of_code()
            self.prostat.get_total_files()
            self.prostat.get_total_folders()
            self.prostat.get_project_structure()
        else:
            self.parser.print_help()
            sys.exit(1)


if __name__ == '__main__':
    # ProstatCLI().run()
    Prostat(path='./example_project_1', ignore=['*.pyc', '*__pycache__', '.git']) \
        .get_project_structure()
