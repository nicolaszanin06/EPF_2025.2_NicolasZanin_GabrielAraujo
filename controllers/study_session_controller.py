from bottle import Bottle, request
from .base_controller import BaseController
from services.study_session_service import StudySessionService
from services.subject_service import SubjectService
from services.topic_service import TopicService

SESSION_SECRET = "sua-chave-secreta-aqui"


class StudySessionController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)

        self.session_service = StudySessionService()
        self.subject_service = SubjectService()
        self.topic_service = TopicService()

        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/sessions', method='GET', callback=self.list_sessions)

        self.app.route(
            '/subjects/<subject_id:int>/sessions',
            method='GET',
            callback=self.list_sessions_by_subject,
        )

        self.app.route(
            '/subjects/<subject_id:int>/topics/<topic_id:int>/sessions',
            method='GET',
            callback=self.list_sessions_by_topic,
        )

        self.app.route(
            '/sessions/new',
            method=['GET', 'POST'],
            callback=self.new_session_global,
        )

        self.app.route(
            '/subjects/<subject_id:int>/sessions/new',
            method=['GET', 'POST'],
            callback=self.new_session_from_subject,
        )

        self.app.route(
            '/subjects/<subject_id:int>/topics/<topic_id:int>/sessions/new',
            method=['GET', 'POST'],
            callback=self.new_session_from_topic,
        )

        self.app.route(
            '/sessions/<session_id:int>/edit',
            method=['GET', 'POST'],
            callback=self.edit_session,
        )

        self.app.route(
            '/sessions/<session_id:int>/delete',
            method='POST',
            callback=self.delete_session,
        )

    def _require_login(self):
        """Retorna o ID do usuário logado ou None."""
        user_id = request.get_cookie("session_user", secret=SESSION_SECRET)
        if not user_id:
            return None
        return int(user_id)

    def _get_user_subjects(self, user_id: int):
        return [
            s for s in self.subject_service.list_all()
            if s.user_id == user_id
        ]

    def list_sessions(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        sessions = [
            s for s in self.session_service.list_all()
            if s.user_id == user_id
        ]

        subjects = {s.id: s for s in self._get_user_subjects(user_id)}
        subject_ids = set(subjects.keys())

        topics = {
            t.id: t
            for t in self.topic_service.list_all()
            if t.subject_id in subject_ids
        }

        return self.render(
            'sessions',
            sessions=sessions,
            subjects=subjects,
            topics=topics,
            current_subject=None,
            current_topic=None,
        )

    def list_sessions_by_subject(self, subject_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        subject = self.subject_service.get_by_id(subject_id)
        if not subject or subject.user_id != user_id:
            return "Subject not found or not allowed"

        sessions = [
            s for s in self.session_service.list_all()
            if s.user_id == user_id and s.subject_id == subject_id
        ]

        subjects = {s.id: s for s in self._get_user_subjects(user_id)}
        subject_ids = set(subjects.keys())

        topics = {
            t.id: t
            for t in self.topic_service.list_all()
            if t.subject_id in subject_ids
        }

        return self.render(
            'sessions',
            sessions=sessions,
            subjects=subjects,
            topics=topics,
            current_subject=subject,
            current_topic=None,
        )

    def list_sessions_by_topic(self, subject_id: int, topic_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        subject = self.subject_service.get_by_id(subject_id)
        topic = self.topic_service.get_by_id(topic_id)

        if not subject or subject.user_id != user_id:
            return "Subject not found or not allowed"
        if not topic or topic.subject_id != subject_id:
            return "Topic not found or not allowed"

        sessions = [
            s for s in self.session_service.list_all()
            if s.user_id == user_id
            and s.subject_id == subject_id
            and s.topic_id == topic_id
        ]

        subjects = {s.id: s for s in self._get_user_subjects(user_id)}
        subject_ids = set(subjects.keys())

        topics = {
            t.id: t
            for t in self.topic_service.list_all()
            if t.subject_id in subject_ids
        }

        return self.render(
            'sessions',
            sessions=sessions,
            subjects=subjects,
            topics=topics,
            current_subject=subject,
            current_topic=topic,
        )

    def new_session_global(self):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        if request.method == 'GET':
            subjects = self._get_user_subjects(user_id)
            subject_ids = {s.id for s in subjects}

            topics = [
                t for t in self.topic_service.list_all()
                if t.subject_id in subject_ids
            ]

        return self.render(
            'session_form',
            action="/sessions/new",
            session=None,
            subjects=subjects,
            topics=topics,
            current_subject=None,
            current_topic=None,
            user_id=user_id,
        )

        request.forms['user_id'] = str(user_id)
        self.session_service.save()
        return self.redirect('/sessions')

    def new_session_from_subject(self, subject_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        subject = self.subject_service.get_by_id(subject_id)
        if not subject or subject.user_id != user_id:
            return "Subject not found or not allowed"

        if request.method == 'GET':
            subjects = self._get_user_subjects(user_id)
            topics = [
                t for t in self.topic_service.list_all()
                if t.subject_id == subject_id
            ]

            return self.render(
                'session_form',
                action=f"/subjects/{subject_id}/sessions/new",
                session=None,
                subjects=subjects,
                topics=topics,
                current_subject=subject,
                current_topic=None,
                user_id=user_id,
            )

        request.forms['user_id'] = str(user_id)
        request.forms['subject_id'] = str(subject_id)
        self.session_service.save()
        return self.redirect(f"/subjects/{subject_id}/sessions")

    def new_session_from_topic(self, subject_id: int, topic_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        subject = self.subject_service.get_by_id(subject_id)
        topic = self.topic_service.get_by_id(topic_id)

        if not subject or subject.user_id != user_id:
            return "Subject not found or not allowed"
        if not topic or topic.subject_id != subject_id:
            return "Topic not found or not allowed"

        if request.method == 'GET':
            subjects = self._get_user_subjects(user_id)
            topics = [
                t for t in self.topic_service.list_all()
                if t.subject_id == subject_id
            ]

            return self.render(
                'session_form',
                action=f"/subjects/{subject_id}/topics/{topic_id}/sessions/new",
                session=None,
                subjects=subjects,
                topics=topics,
                current_subject=subject,
                current_topic=topic,
                user_id=user_id,
            )

        request.forms['user_id'] = str(user_id)
        request.forms['subject_id'] = str(subject_id)
        request.forms['topic_id'] = str(topic_id)
        self.session_service.save()
        return self.redirect(
            f"/subjects/{subject_id}/topics/{topic_id}/sessions"
        )

    def edit_session(self, session_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        session = self.session_service.get_by_id(session_id)
        if not session or session.user_id != user_id:
            return "Session not found or not allowed"

        if request.method == 'GET':
            subjects = self._get_user_subjects(user_id)
            subject_ids = {s.id for s in subjects}

            topics = [
                t for t in self.topic_service.list_all()
                if t.subject_id in subject_ids
            ]

        return self.render(
            'session_form',
            action=f"/sessions/{session_id}/edit",
            session=session,
            subjects=subjects,
            topics=topics,
            current_subject=None,
            current_topic=None,
            user_id=user_id,
        )

        self.session_service.update(session)
        return self.redirect('/sessions')

    def delete_session(self, session_id: int):
        user_id = self._require_login()
        if not user_id:
            return self.redirect('/login')

        session = self.session_service.get_by_id(session_id)
        if not session or session.user_id != user_id:
            return "Session not found or not allowed"

        self.session_service.delete(session_id)
        return self.redirect('/sessions')


session_routes = Bottle()
session_controller = StudySessionController(session_routes)
