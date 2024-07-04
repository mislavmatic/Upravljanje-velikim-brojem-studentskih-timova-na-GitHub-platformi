from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from sqlalchemy.orm import joinedload
import excel_parse2
from excel_parse2 import Asistent, Demos, Student, Zadatak, Grupa, StudGrupa
# import excel_parse
# from excel_parse import Asistent, Demos, Student, Zadatak, Grupa, StudGrupa

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

    # excel_parse.parsiranje(file)
    excel_parse2.parsiranje(file)

    return 'File processed successfully', 200


# @app.route('/get_data', methods=['GET']) 
# def get_data():
#     session =  excel_parse.create_session()

#     data = []
#     assistants = session.query(Asistent).options(joinedload(Asistent.demos)).all()

#     for assistant in assistants:
#         assistant_data = {
#             "name_asist": assistant.name_asist,
#             "groups": []
#         }

#         for demos in assistant.demos:
#             for group in demos.groups:
#                 group_data = {
#                     "name_demos": demos.name_demos,
#                     "name_g": group.name_g,
#                     "github": group.github,
#                     "name_zad": group.zadatak.name_zad,
#                     "students": []
#                 }

#                 for stud_grupa in group.students:
#                     student_data = {
#                         "name": stud_grupa.student.name_stud,
#                         "is_leader": stud_grupa.student.s_id == group.leader_id
#                     }
#                     group_data["students"].append(student_data)

#                 assistant_data["groups"].append(group_data)

#         data.append(assistant_data)

#     response = jsonify(data)
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     with open('temp/tempJSON', 'w') as file:
#         file.write(response.get_data(as_text=True))
        
#     return response

@app.route('/get_data', methods=['GET']) 
def get_data():
    # session =  excel_parse.create_session()
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
                group_data = {
                    "name_demos": demos.name_demos,
                    "name_g": group.name_g,
                    "github": group.github,
                    "name_zad": group.zadatak.name_zad,
                    "students": []
                }

                for stud_grupa in session.query(StudGrupa).filter(StudGrupa.github == group.github).all():
                    student_data = {
                        "name": stud_grupa.student.name_stud,
                        # "is_leader": stud_grupa.student.s_id == group.leader_id
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
    
    eror_file.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)#, port=3000)