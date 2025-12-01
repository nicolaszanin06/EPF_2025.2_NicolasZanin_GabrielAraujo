from datetime import datetime, timedelta
from models.study_session import StudySessionModel
from models.subject import SubjectModel
from models.topic import TopicModel


def _parse(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        return None


class DashboardService:
    def _init_(self):
        self.session_model = StudySessionModel()
        self.subject_model = SubjectModel()
        self.topic_model = TopicModel()

    # -----------------------------------------------------
    # SESSIONS FILTER
    # -----------------------------------------------------
    def _sessions_of_user(self, user_id):
        return [
            s for s in self.session_model.get_all()
            if s.user_id == user_id
        ]

    # -----------------------------------------------------
    # RESUMO TOTAL GERAL
    # -----------------------------------------------------
    def get_overview(self, user_id):
        sessions = self._sessions_of_user(user_id)
        subjects = [
            s for s in self.subject_model.get_all()
            if s.user_id == user_id
        ]
        subject_map = {s.id: s for s in subjects}
        topic_map = {t.id: t for t in self.topic_model.get_all()}

        total_minutes = sum(s.duration_minutes for s in sessions)
        total_hours = total_minutes / 60

        return {
            "total_hours": total_hours,
            "sessions_count": len(sessions),
            "subjects_count": len(subjects),
            "topics_count": len(topic_map),
        }

    # -----------------------------------------------------
    # HORAS POR MATÉRIA
    # -----------------------------------------------------
    def get_hours_per_subject(self, user_id):
        sessions = self._sessions_of_user(user_id)
        subjects = [
            s for s in self.subject_model.get_all()
            if s.user_id == user_id
        ]

        hours_per_subject = {}
        for subject in subjects:
            total_minutes = sum(
                s.duration_minutes
                for s in sessions
                if s.subject_id == subject.id
            )
            hours_per_subject[subject.name] = total_minutes / 60

        return hours_per_subject

    # -----------------------------------------------------
    # HORAS POR TÓPICO
    # -----------------------------------------------------
    def get_hours_per_topic(self, user_id, subject_id=None):
        sessions = self._sessions_of_user(user_id)
        topics = [
            t for t in self.topic_model.get_all()
            if subject_id is None or t.subject_id == subject_id
        ]

        hours_per_topic = {}
        for t in topics:
            total_minutes = sum(
                s.duration_minutes
                for s in sessions
                if s.topic_id == t.id
            )
            hours_per_topic[t.title] = total_minutes / 60

        return hours_per_topic

    # -----------------------------------------------------
    # HORAS POR DIA (últimos N dias)
    # -----------------------------------------------------
    def hours_last_days(self, user_id, days=7):
        sessions = self._sessions_of_user(user_id)
        today = datetime.today().date()
        start = today - timedelta(days=days)

        result = {}
        for i in range(days+1):
            day = start + timedelta(days=i)
            result[str(day)] = 0

        for s in sessions:
            d = _parse(s.date)
            if d and str(d) in result:
                result[str(d)] += s.duration_minutes / 60

        return result

    # -----------------------------------------------------
    # PROGRESSO POR MATÉRIA
    # concluídos vs não concluídos
    # -----------------------------------------------------
    def subject_progress(self, user_id):
        subjects = [
            s for s in self.subject_model.get_all()
            if s.user_id == user_id
        ]
        topics = [
            t for t in self.topic_model.get_all()
            if t.subject_id in {s.id for s in subjects}
        ]

        progress = {}
        for subject in subjects:
            ts = [t for t in topics if t.subject_id == subject.id]

            done = len([t for t in ts if (t.status or "").lower()
                       in ("done", "concluido", "concluído")])
            pending = len(ts) - done

            progress[subject.name] = {
                "done": done,
                "pending": pending,
            }

        return progress
