from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql+psycopg:///students')

db = SQLAlchemy(app)





class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.id} {self.first_name}"
def student_serializer(stud: Students) -> dict:
    return {
        "id": stud.id,
        "full_name": f"{stud.first_name} {stud.last_name}",
        "age": stud.age,
        "grade": stud.grade
    }





@app.route('/')
def home():
    return '<h1>Welcome To The Homepage<h1>'


@app.route('/students/', methods=['GET']) 
def get_students():
    all_students = Students.query.all()
    print(all_students)
    return jsonify([student_serializer(stud) for stud in all_students])

@app.route('/old_students', methods=['GET'])
def old_students():
    old_studs = Students.query.filter(Students.age > 20).all()
    return jsonify([student_serializer(student) for student in old_studs])
    

@app.route('/young_students', methods= ['GET'])
def young_students():
    young_studs = Students.query.filter(Students.age < 21).all()
    result = []
    for stud in young_studs:
        serialized = student_serializer(stud)
        result.append(serialized)
    return jsonify(result)

@app.route('/advance_students', methods=['GET'])
def advance_students():
    result = []
    advance_studs = Students.query.filter(
        Students.age < 21,
        Students.grade =='A'
        ).all()
    
    for stud in advance_studs:
        serialized = student_serializer(stud)
        result.append(serialized)
    return jsonify(result)

@app.route('/student_names', methods= ['GET'])
def student_names():
    result = []
    stud_names = Students.query.all()
    
    for stud in stud_names:
        result.append({
            'first_name' : stud.first_name,
            'last_name' : stud.last_name
        })
    return jsonify(result)


















if __name__ == '__main__':
    app.run(debug=True, port=8000)
    