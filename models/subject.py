import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class Subject:
    def __init__(self, id, user_id, name, color, description=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.color = color
        self.description = description

    def __repr__(self):
        return (
            f"Subject(id={self.id}, user_id={self.user_id}, "
            f"name='{self.name}', color='{self.color}', "
            f"description='{self.description}')"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "color": self.color,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            name=data["name"],
            color=data["color"],
            description=data.get("description")
        )


class SubjectModel:
    FILE_PATH = os.path.join(DATA_DIR, 'subjects.json')

    def __init__(self):
        self.subjects = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Subject.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [s.to_dict() for s in self.subjects],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.subjects

    def get_by_id(self, subject_id: int):
        return next((s for s in self.subjects if s.id == subject_id), None)

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)
        self._save()

    def update_subject(self, updated_subject: Subject):
        for i, subject in enumerate(self.subjects):
            if subject.id == updated_subject.id:
                self.subjects[i] = updated_subject
                self._save()
                break

    def delete_subject(self, subject_id: int):
        self.subjects = [s for s in self.subjects if s.id != subject_id]
        self._save()
