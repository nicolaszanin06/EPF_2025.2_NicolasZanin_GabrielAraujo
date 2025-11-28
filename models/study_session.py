import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '.', 'data')


class StudySession:
    def __init__(self,id,user_id,subject_id,topic_id,date,duration_minutes,
                 notes=None,status=None,study_type=None,difficulty=None,):
        self.id = id
        self.user_id = user_id
        self.subject_id = subject_id
        self.topic_id = topic_id  
        self.date = date
        self.duration_minutes = duration_minutes
        self.notes = notes
        self.status = status          
        self.study_type = study_type 
        self.difficulty = difficulty  

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subject_id": self.subject_id,
            "topic_id": self.topic_id,
            "date": self.date,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes,
            "status": self.status,
            "study_type": self.study_type,
            "difficulty": self.difficulty,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            subject_id=data["subject_id"],
            topic_id=data.get("topic_id"),  
            date=data["date"],
            duration_minutes=data["duration_minutes"],
            notes=data.get("notes"),
            status=data.get("status"),
            study_type=data.get("study_type"),
            difficulty=data.get("difficulty"),
        )


class StudySessionModel:
    FILE_PATH = os.path.join(DATA_DIR, 'study_sessions.json')

    def __init__(self):
        self.sessions = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [StudySession.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(
                [s.to_dict() for s in self.sessions],
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_all(self):
        return self.sessions

    def get_by_id(self, session_id: int):
        return next((s for s in self.sessions if s.id == session_id), None)

    def add_session(self, session: StudySession):
        self.sessions.append(session)
        self._save()

    def update_session(self, updated_session: StudySession):
        for i, session in enumerate(self.sessions):
            if session.id == updated_session.id:
                self.sessions[i] = updated_session
                self._save()
                break

    def delete_session(self, session_id: int):
        self.sessions = [s for s in self.sessions if s.id != session_id]
        self._save()
