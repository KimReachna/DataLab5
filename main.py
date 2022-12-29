import json

from flask import Flask, request
from StudentStorage import StudentStorage
from Student import Student


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


app = Flask(__name__)
student_storage = None


@app.route('/student', methods=['GET'])
def get_all_cats():
    return json.dumps(student_storage.get_all_students(), indent=4, cls=CustomEncoder)


@app.route('/student', methods=['POST'])
def create_student():
    print("Add student name")
    request_data = request.get_json()
    s_name = request_data["name"]
    s_mark = request_data["mark"]
    s_id = request_data["id"]
    student = Student(s_name, s_mark, s_id)
    student_storage.add_student(student)
    return json.dumps(student, indent=4, cls=CustomEncoder)


if __name__ == '__main__':
    print("started")
    student_storage = StudentStorage()
    student_storage.fill_init_students()
    app.run()