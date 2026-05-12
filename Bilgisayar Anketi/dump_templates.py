import os
import glob

base_dir = r"c:\Users\Yusuf Cemal DURMUŞ\Desktop\Bilgisayar Anketi"

templates = {
    'polls/index.html': os.path.join(base_dir, 'polls', 'templates', 'polls', 'index.html'),
    'polls/detail.html': os.path.join(base_dir, 'polls', 'templates', 'polls', 'detail.html'),
    'polls/results.html': os.path.join(base_dir, 'polls', 'templates', 'polls', 'results.html'),
    'polls/add_poll.html': os.path.join(base_dir, 'polls', 'templates', 'polls', 'add_poll.html'),
    'registration/login.html': os.path.join(base_dir, 'templates', 'registration', 'login.html'),
    'registration/signup.html': os.path.join(base_dir, 'templates', 'registration', 'signup.html'),
}

out_path = os.path.join(base_dir, 'polls', 'python_templates.py')

with open(out_path, 'w', encoding='utf-8') as out:
    out.write('TEMPLATES_DICT = {\n')
    for name, path in templates.items():
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            out.write(f'    "{name}": """{content}""",\n')
    out.write('}\n')

print("Generated python_templates.py")
