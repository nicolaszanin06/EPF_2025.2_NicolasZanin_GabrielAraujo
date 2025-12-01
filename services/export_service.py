# services/export_service.py
import json
import csv
import io


class ExportService:

    def __init__(self, session_service, subject_service, topic_service):
        self.session_service = session_service
        self.subject_service = subject_service
        self.topic_service = topic_service

    # ---------- helpers internos ----------

    def _get_user_subjects(self, user_id: int):
        subjects = []
        for s in self.subject_service.list_all():
            s_user_id = getattr(s, "user_id", getattr(s, "id_usuario", None))
            if s_user_id == user_id:
                subjects.append(s)
        return subjects

    def _get_user_topics(self, user_id: int):
        subjects = self._get_user_subjects(user_id)
        subject_ids = {s.id for s in subjects}
        topics = []
        for t in self.topic_service.list_all():
            t_subject_id = getattr(
                t, "subject_id", getattr(t, "id_materia", None))
            if t_subject_id in subject_ids:
                topics.append(t)
        return topics

    def _get_user_sessions(self, user_id: int):
        sessions = []
        for s in self.session_service.list_all():
            s_user_id = getattr(s, "user_id", getattr(s, "id_usuario", None))
            if s_user_id == user_id:
                sessions.append(s)
        return sessions

    # ---------- conversores ----------

    def _subject_to_dict(self, s):
        return {
            "id": s.id,
            "user_id": getattr(s, "user_id", getattr(s, "id_usuario", None)),
            "name": getattr(s, "name", getattr(s, "nome", None)),
            "color": getattr(s, "color", getattr(s, "cor", None)),
            "description": getattr(s, "description", getattr(s, "descricao", None)),
        }

    def _topic_to_dict(self, t):
        return {
            "id": t.id,
            "subject_id": getattr(t, "subject_id", getattr(t, "id_materia", None)),
            "title": getattr(t, "title", getattr(t, "titulo", None)),
            "status": getattr(t, "status", None),
            "estimated_duration": getattr(
                t,
                "estimated_duration",
                getattr(t, "duracao_estimada", None),
            ),
            "order": getattr(t, "order", getattr(t, "ordem", None)),
        }

    def _session_to_dict(self, s):
        return {
            "id": s.id,
            "user_id": getattr(s, "user_id", getattr(s, "id_usuario", None)),
            "subject_id": getattr(s, "subject_id", getattr(s, "id_materia", None)),
            "topic_id": getattr(s, "topic_id", getattr(s, "topico_id", None)),
            "date": getattr(s, "date", getattr(s, "data", None)),
            "duration_minutes": getattr(
                s, "duration_minutes", getattr(s, "duracao", None)
            ),
            "notes": getattr(s, "notes", getattr(s, "notas", None)),
        }

    # ---------- EXPORT: JSON COMPLETO ----------

    def export_full_json(self, user_id: int) -> str:
        subjects = self._get_user_subjects(user_id)
        topics = self._get_user_topics(user_id)
        sessions = self._get_user_sessions(user_id)

        data = {
            "user_id": user_id,
            "subjects": [self._subject_to_dict(s) for s in subjects],
            "topics": [self._topic_to_dict(t) for t in topics],
            "sessions": [self._session_to_dict(s) for s in sessions],
        }

        return json.dumps(data, indent=2, ensure_ascii=False)

    # ---------- EXPORT: CSV – sessions ----------

    def export_sessions_csv(self, user_id: int) -> str:
        sessions = self._get_user_sessions(user_id)

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(
            ["id", "user_id", "subject_id", "topic_id",
                "date", "duration_minutes", "notes"]
        )

        for s in sessions:
            d = self._session_to_dict(s)
            writer.writerow(
                [
                    d["id"],
                    d["user_id"],
                    d["subject_id"],
                    d["topic_id"],
                    d["date"],
                    d["duration_minutes"],
                    d["notes"],
                ]
            )

        return output.getvalue()

    # ---------- EXPORT: CSV – subjects ----------

    def export_subjects_csv(self, user_id: int) -> str:
        subjects = self._get_user_subjects(user_id)

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(["id", "user_id", "name", "color", "description"])

        for s in subjects:
            d = self._subject_to_dict(s)
            writer.writerow(
                [d["id"], d["user_id"], d["name"], d["color"], d["description"]]
            )

        return output.getvalue()

    # ---------- EXPORT: CSV – topics ----------

    def export_topics_csv(self, user_id: int) -> str:
        topics = self._get_user_topics(user_id)

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(
            ["id", "subject_id", "title", "status", "estimated_duration", "order"]
        )

        for t in topics:
            d = self._topic_to_dict(t)
            writer.writerow(
                [
                    d["id"],
                    d["subject_id"],
                    d["title"],
                    d["status"],
                    d["estimated_duration"],
                    d["order"],
                ]
            )

        return output.getvalue()
