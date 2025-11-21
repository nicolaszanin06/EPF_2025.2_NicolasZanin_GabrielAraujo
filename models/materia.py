class Materia:
    def __init__(self, id, user_id, name, description= None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            name=data["name"],
            description=data.get("description")
        )
