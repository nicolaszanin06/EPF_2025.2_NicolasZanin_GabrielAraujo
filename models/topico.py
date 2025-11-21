class Topic:
    def __init__(self, id, subject_id, title, description = None):
        self.id = id
        self.subject_id = subject_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "title": self.title,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            subject_id=data["subject_id"],
            title=data["title"],
            description=data.get("description")
        )
