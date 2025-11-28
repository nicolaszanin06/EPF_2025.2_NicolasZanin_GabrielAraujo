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

        notes = request.forms.get("notes") or None
        status = request.forms.get("status") or None
        study_type = request.forms.get("study_type") or None
        difficulty = request.forms.get("difficulty") or None

        session = StudySession(id=new_id,user_id=user_id,subject_id=subject_id,topic_id=topic_id,
                               date=date,duration_minutes=duration_minutes,notes=notes,status=status,
                               study_type=study_type,difficulty=difficulty,)

        self.model.add_session(session)

    def update(self, session: StudySession):
        date = request.forms.get("date")
        if date:
            session.date = date

        duration_raw = request.forms.get("duration_minutes")
        if duration_raw:
            session.duration_minutes = int(duration_raw)

        notes = request.forms.get("notes")
        if notes is not None:
            session.notes = notes or None

        topic_id_raw = request.forms.get("topic_id")
        if topic_id_raw is not None:
            session.topic_id = int(topic_id_raw) if topic_id_raw else None

        status_raw = request.forms.get("status")
        if status_raw is not None:
            session.status = status_raw or None

        study_type_raw = request.forms.get("study_type")
        if study_type_raw is not None:
            session.study_type = study_type_raw or None

        difficulty_raw = request.forms.get("difficulty")
        if difficulty_raw is not None:
            session.difficulty = difficulty_raw or None

        self.model.update_session(session)

    def delete(self, session_id: int):
        self.model.delete_session(session_id)
