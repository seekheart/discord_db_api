import json

pros = {
    "reddeth#4265": ["php", "sql", "zend", "doctrine", "javascript", "html", "css"],
    "bribrian#2748": ["python", "java", "HTML", "CSS", "JavaScript", "AngularJS", "Firebase", "LabVIEW", "PHP", "C", "C++"],
    "devoidfury#3045": ["Javascript", "Node", "Python", "django", "SQL", "PHP" "HTML", "CSS", "linux"],
    "seekheart#5892": ["Python", "SQL", "Mongo", "HTML", "CSS", "Perl"],
    "LewisTheScot#9402": ["Python", "SQL", "HTML", "CSS", "JavaScript"],
    "RikerCabra#6365": ["C#", "visualbasic", "SQL", "JavaScript", "Oracle", "Regex"],
    "gizmo#2538": ["Python", "C", "Matlab", "R", "ScientificComputing", "MPI"]
}

pros_by_lang = dict()
for uname, langs in pros.items():
    for language in langs:
        try:
            pros_by_lang[language.lower()].append(uname)
        except KeyError:
            pros_by_lang[language.lower()] = [uname]

with open('pros.json', 'w') as fp:
    json.dump(pros_by_lang, fp, indent=4)