from bottle import request
from models.topic import TopicModel, Topic


class TopicService:
    def __init__(self):
        self.model = TopicModel()

    def list_all(self):
        return self.model.get_all()

    def get_by_id(self, topic_id: int):
        return self.model.get_by_id(topic_id)

    def save(self):
        topics = self.model.get_all()
        last_id = max((t.id for t in topics), default=0)
        new_id = last_id + 1

        subject_id = int(request.forms.get("subject_id"))
        title = request.forms.get("title") or ""
        status = request.forms.get("status") or "pending"

        estimated_raw = request.forms.get("estimated_minutes") or "0"
        order_raw = request.forms.get("order") or "0"

        try:
            estimated_minutes = int(estimated_raw)
        except ValueError:
            estimated_minutes = 0

        try:
            order = int(order_raw)
        except ValueError:
            order = 0

        topic = Topic(
            id=new_id,
            subject_id=subject_id,
            title=title,
            status=status,
            estimated_minutes=estimated_minutes,
            order=order
        )

        self.model.add_topic(topic)

    def update(self, topic: Topic):

        title = request.forms.get("title")
        if title is not None:
            topic.title = title or topic.title

        status = request.forms.get("status")
        if status is not None:
            topic.status = status or topic.status

        estimated_raw = request.forms.get("estimated_minutes")
        if estimated_raw is not None and estimated_raw != "":
            try:
                topic.estimated_minutes = int(estimated_raw)
            except ValueError:
                pass  # se vier lixo, ignora

        order_raw = request.forms.get("order")
        if order_raw is not None and order_raw != "":
            try:
                topic.order = int(order_raw)
            except ValueError:
                pass
            
        self.model.update_topic(topic)

    def delete(self, topic_id: int):
        self.model.delete_topic(topic_id)

    def toggle_status(self, topic_id: int):
        topic = self.model.get_by_id(topic_id)
        if not topic:
            return None

        topic.status = "completed" if topic.status != "completed" else "pending"
        self.model.update_topic(topic)
        return topic
