import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class Topic:
    def __init__(self, id, subject_id, title, status, estimated_minutes, order):
        self.id = id
        self.subject_id = subject_id
        self.title = title
        self.status = status
        self.estimated_minutes = estimated_minutes
        self.order = order

    def __repr__(self):
        return (
            f"Topic(id={self.id}, subject_id={self.subject_id}, "
            f"title='{self.title}', status='{self.status}', "
            f"estimated_minutes={self.estimated_minutes}, order={self.order})"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "title": self.title,
            "status": self.status,
            "estimated_minutes": self.estimated_minutes,
            "order": self.order
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            subject_id=data["subject_id"],
            title=data["title"],
            status=data["status"],
            estimated_minutes=data["estimated_minutes"],
            order=data["order"]
        )


class TopicModel:
    FILE_PATH = os.path.join(DATA_DIR, 'topics.json')

    def __init__(self):
        self.topics = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Topic.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [t.to_dict() for t in self.topics],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.topics

    def get_by_id(self, topic_id: int):
        return next((t for t in self.topics if t.id == topic_id), None)

    def add_topic(self, topic: Topic):
        self.topics.append(topic)
        self._save()

    def update_topic(self, updated_topic: Topic):
        for i, topic in enumerate(self.topics):
            if topic.id == updated_topic.id:
                self.topics[i] = updated_topic
                self._save()
                break

    def delete_topic(self, topic_id: int):
        self.topics = [t for t in self.topics if t.id != topic_id]
        self._save()
