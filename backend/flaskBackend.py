from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import excel_parse2
from excel_parse2 import Asistent, Demos, Student, Zadatak, Grupa, StudGrupa
from podsustavDamjan import getCommitCount

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)
    filepath = os.path.join('.', 'temp', filename)
    file.save(filepath)

    excel_parse2.parsiranje(file)

    return 'File processed successfully', 200

@app.route('/get_data', methods=['GET']) 
def get_data():
    session =  excel_parse2.create_session()
    eror_file = open('temp/eror.txt', 'w', encoding='utf-8')
    data = []
    assistants = session.query(Asistent).all()

    for assistant in assistants:
        eror_file.write(assistant.name_asist + "\n")
        assistant_data = {
            "name_asist": assistant.name_asist,
            "groups": []
        }

        for demos in assistant.demos:
            eror_file.write("   " + demos.name_demos + "\n")
            for group in demos.groups:
                eror_file.write("      " + group.name_g + "\n")
                # temp_c_c = getCommitCount(group.github)
                group_data = {
                    "name_demos": demos.name_demos,
                    "name_g": group.name_g,
                    "github": group.github,
                    "name_zad": group.zadatak.name_zad,
                    "commit_count": group.commit_count,
                    # "commit_count": temp_c_c,
                    "students": []
                }

                for stud_grupa in session.query(StudGrupa).filter(StudGrupa.github == group.github).all():
                    student_data = {
                        "name": stud_grupa.student.name_stud,
                        "stud_email": stud_grupa.student.s_email,
                        "is_leader": stud_grupa.student.s_email == group.leader_email,
                    }
                    group_data["students"].append(student_data)

                assistant_data["groups"].append(group_data)

        data.append(assistant_data)

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    with open('temp/tempJSON', 'w') as file:
        file.write(response.get_data(as_text=True))
    
    session.close()
    eror_file.close()
    return response

@app.route('/api/group-commit-count/<path:group_link>', methods=['GET'])
def get_commit_count(group_link):
    commit_count = getCommitCount(group_link)
    session =  excel_parse2.create_session()
    group_data = session.query(Grupa).filter(Grupa.github == group_link).first()
    if group_data:
        group_data.commit_count = commit_count
        session.commit()

        demos = session.query(Demos).filter(Demos.de_id == group_data.de_id).first()
        demos_name = demos.name_demos if demos else 'Unknown'
        
        group_dict = {
            "name_demos": demos_name,
            "name_g": group_data.name_g,
            "github": group_data.github,
            "name_zad": group_data.name_zad,
            "commit_count": group_data.commit_count,
            "students": []
        }
        

        for stud_grupa in session.query(StudGrupa).filter(StudGrupa.github == group_data.github).all():
            student_data = {
                "name": stud_grupa.student.name_stud,
                "stud_email": stud_grupa.student.s_email,
                "is_leader": stud_grupa.student.s_email == group_data.leader_email,
            }
            group_dict["students"].append(student_data)

    session.close()
    # print(group_dict)
    response = jsonify(group_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
