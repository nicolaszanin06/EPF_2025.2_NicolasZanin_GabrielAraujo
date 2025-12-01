from datetime import date


class StatsService:

    def __init__(self, session_service, subject_service, topic_service):
        self.session_service = session_service
        self.subject_service = subject_service
        self.topic_service = topic_service

    def _parse_date(self, value: str):
        if not value:
            return None
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None


    def get_stats(self, user_id: int, start_date: str=None, end_date: str=None):

        start = self._parse_date(start_date)
        end = self._parse_date(end_date)

        # -------- MATÉRIAS --------
        subjects = [
            s for s in self.subject_service.list_all()
            if s.user_id == user_id
        ]
        subjects_by_id = {s.id: s for s in subjects}

        # -------- SESSÕES --------
        sessions = [
            s for s in self.session_service.list_all()
            if s.user_id == user_id
        ]

        filtered_sessions = []
        for s in sessions:
            try:
                s_date = date.fromisoformat(s.date)
            except Exception:
                s_date = None

            if start and s_date and s_date < start:
                continue
            if end and s_date and s_date > end:
                continue

            filtered_sessions.append(s)

        total_minutes = sum(
            getattr(s, 'duration_minutes', 0)
            for s in filtered_sessions
        )
        total_hours = total_minutes / 60 if total_minutes else 0

        sessions_count = len(filtered_sessions)

        minutes_per_subject = {}
        for s in filtered_sessions:
            subj_id = getattr(s, 'subject_id', None)
            if subj_id is None:
                continue
            minutes_per_subject.setdefault(subj_id, 0)
            minutes_per_subject[subj_id] += getattr(s, 'duration_minutes', 0)

        # -------- TÓPICOS --------
        topics = [
            t for t in self.topic_service.list_all()
            if t.subject_id in subjects_by_id
        ]

        completed_status = {'done', 'completed', 'concluido', 'concluído'}

        topics_total = len(topics)
        topics_completed = 0

        for t in topics:
            status = (t.status or "").strip().lower()
            if status in completed_status:
                topics_completed += 1

        # -------- resultado final --------

        return {
            "total_minutes": total_minutes,
            "total_hours": round(total_hours, 1),
            "sessions_count": sessions_count,
            "subjects_count": len(subjects),
            "topics_total": topics_total,
            "topics_completed": topics_completed,
            "minutes_per_subject": minutes_per_subject,
            "start_date": start_date or "",
            "end_date": end_date or "",
            "subjects": subjects,   
        }
