from bottle import request
from models.subject import SubjectModel, Subject


class SubjectService:
    def __init__(self):
        self.model = SubjectModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, subject_id: int):
        return self.model.get_by_id(subject_id)

    def save(self):
        subjects = self.model.get_all()
        last_id = max((s.id for s in subjects), default=0)
        new_id = last_id + 1

        user_id = int(request.forms.get("user_id"))

        name = request.forms.get("name")
        color = request.forms.get("color")
        description = request.forms.get("description")

        subject = Subject(
            id=new_id,
            user_id=user_id,
            name=name,
            color=color,
            description=description
        )

        self.model.add_subject(subject)

    def update(self, subject: Subject):
        subject.name = request.forms.get("name")
        subject.color = request.forms.get("color")
        subject.description = request.forms.get("description")

        self.model.update_subject(subject)

    def delete(self, subject_id: int):
        self.model.delete_subject(subject_id)
