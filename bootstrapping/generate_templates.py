import csv

def generate_template(title, text, link):
    return (
        f'<!-- DO NOT EDIT BELOW -->\n'
        f'{{% extends "layout.html" %}}\n'
        f'{{% block title %}}\n'
        f'{title}\n'
        f'{{% endblock %}}\n'
        f'{{% block content %}}\n'
        f'{{% filter markdown %}}\n'
        f'## Your new hobby is: \n'
        f'# {title}\n'
        f'<!-- DO NOT EDIT ABOVE -->\n'

        f'<!-- You can add new information in Markdown here! -->\n'
        f'<!-- You are welcome and encouraged to link to useful resources or communities for a new hobbyist. -->\n'
        f'{text}\n\n'
        f'Find out more on [Wikipedia]({link})!\n\n'
        f'<!-- DO NOT EDIT BELOW -->\n'
        f'{{% endfilter %}}\n'
        f'{{% endblock %}}\n'
        f'<!-- DO NOT EDIT ABOVE -->\n'
        )

def save_output(title, template):
    try:
        with open(f'../templates/{title}.html', 'w') as output_file:
            output_file.write(template)
    except:
        print("Issue with saving title: " + title)

with open('hobby_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for hobby in reader:
        if "bad title" not in hobby[1]:
            save_output(hobby[0], generate_template(hobby[0], hobby[1], hobby[2]))