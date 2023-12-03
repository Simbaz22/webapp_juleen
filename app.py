from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja environment
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

# Define quiz data
quiz_data = [
    {'id': 'q1', 'question': 'What does HTTP stand for?', 'options': ['HyperText Transfer Protocol', 'HyperText Transfer Privacy', 'HyperText Technical Protocol']},
    {'id': 'q2', 'question': 'What is the purpose of DNS?', 'options': ['Domain Name System', 'Dynamic Network System', 'Digital Naming Service']},
    {'id': 'q3', 'question': 'Which programming language is known for its simplicity and readability?', 'options': ['Python', 'Java', 'C++']},
    {'id': 'q4', 'question': 'What is the main function of a firewall?', 'options': ['Monitor and control incoming and outgoing network traffic', 'Manage computer hardware', 'Encrypt data transmissions']},
    {'id': 'q5', 'question': 'What is the purpose of an IP address?', 'options': ['Identify and locate a device on a network', 'Encode website URLs', 'Facilitate email communication']},
]

# Render the HTML using Jinja
template = env.get_template('index.html')
rendered_html = template.render(quiz_data=quiz_data)

# Save the generated HTML to index.html
with open('index.html', 'w') as file:
    file.write(rendered_html)
