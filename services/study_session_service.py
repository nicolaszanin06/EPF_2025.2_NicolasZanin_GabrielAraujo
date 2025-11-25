from bottle import request
from models.study_session import StudySessionModel, StudySession


class StudySessionService:
    def __init__(self):
        self.model = StudySessionModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, session_id: int):
        return self.model.get_by_id(session_id)

    def save(self):
        sessions = self.model.get_all()
        last_id = max((s.id for s in sessions), default=0)
        new_id = last_id + 1

        user_id = int(request.forms.get("user_id"))

        subject_id = int(request.forms.get("subject_id"))

        topic_id_raw = request.forms.get("topic_id")
        topic_id = int(topic_id_raw) if topic_id_raw else None

        date = request.forms.get("date")
        duration_minutes = int(request.forms.get("duration_minutes"))
        notes = request.forms.get("notes")

        session = StudySession(
            id=new_id,
            user_id=user_id,
            subject_id=subject_id,
            topic_id=topic_id,
            date=date,
            duration_minutes=duration_minutes,
            notes=notes,
        )

        self.model.add_session(session)

    def update(self, session: StudySession):
        date = request.forms.get("date")
        if date:
            session.date = date

        duration_raw = request.forms.get("duration_minutes")
        if duration_raw:
            session.duration_minutes = int(duration_raw)

        session.notes = request.forms.get("notes")

        self.model.update_session(session)

    def delete(self, session_id: int):
        self.model.delete_session(session_id)
