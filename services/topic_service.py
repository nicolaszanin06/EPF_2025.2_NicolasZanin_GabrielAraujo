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
        title = request.forms.get("title")
        status = request.forms.get("status")
        estimated_minutes = int(request.forms.get("estimated_minutes"))
        order = int(request.forms.get("order"))

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
        topic.title = request.forms.get("title")
        topic.status = request.forms.get("status")
        estimated_raw = request.forms.get("estimated_minutes")
        order_raw = request.forms.get("order")

        if estimated_raw:
            topic.estimated_minutes = int(estimated_raw)
        if order_raw:
            topic.order = int(order_raw)

        self.model.update_topic(topic)

    def delete(self, topic_id: int):
        self.model.delete_topic(topic_id)
