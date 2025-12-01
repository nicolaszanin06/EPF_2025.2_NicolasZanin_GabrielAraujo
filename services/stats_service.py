from datetime import datetime
from models.study_session import StudySessionModel
from models.subject import SubjectModel
from models.topic import TopicModel


def _parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


class StatsService:
    def __init__(self):
        self.session_model = StudySessionModel()
        self.subject_model = SubjectModel()
        self.topic_model = TopicModel()

    def _filter_sessions_by_user_and_period(
        self,
        user_id: int,
        start_date_str: str | None,
        end_date_str: str | None,
    ):
        start_date = _parse_date(start_date_str)
        end_date = _parse_date(end_date_str)

        sessions = [
            s for s in self.session_model.get_all()
            if s.user_id == user_id
        ]

        if start_date:
            sessions = [
                s for s in sessions
                if _parse_date(s.date) and _parse_date(s.date) >= start_date
            ]

        if end_date:
            sessions = [
                s for s in sessions
                if _parse_date(s.date) and _parse_date(s.date) <= end_date
            ]

        return sessions

    def get_stats(
        self,
        user_id: int,
        start_date: str | None = None,
        end_date: str | None = None,
    ):
        sessions = self._filter_sessions_by_user_and_period(
            user_id, start_date, end_date
        )

        total_minutes = sum(s.duration_minutes for s in sessions)
        total_hours = total_minutes / 60 if total_minutes else 0

        subjects = [
            s for s in self.subject_model.get_all()
            if s.user_id == user_id
        ]
        subject_ids = {s.id for s in subjects}

        topics = [
            t for t in self.topic_model.get_all()
            if t.subject_id in subject_ids
        ]

        completed_topics = [
            t for t in topics
            if (t.status or "").lower() in ("done", "concluido", "concluído")
        ]

        return {
            "total_minutes": total_minutes,
            "total_hours": total_hours,
            "sessions_count": len(sessions),
            "completed_topics_count": len(completed_topics),
            "period": {
                "start_date": start_date,
                "end_date": end_date,
            },
        }
