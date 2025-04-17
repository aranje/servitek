from ninja import Router, Schema
from .models import Ticket
from django.contrib.auth import get_user_model

router = Router()
User = get_user_model()

class TicketSchema(Schema):
    user_id: int
    title: str
    description: str
    ticket_type: str
    created_at: str
    updated_at: str

class TicketOut(Schema):
    id: int
    user: str
    title: str
    description: str
    ticket_type: str
    created_at: str
    updated_at: str

@router.post("/create")
def create_ticket(request, payload: TicketSchema):
    try:
        user = User.objects.get(id = payload.user_id)
    except User.DoesNotExist:
        return {"error": "user not found"}
    
    new_ticket = Ticket.objects.create(
        user = user,
        title = payload.title,
        description = payload.description,
        ticket_type = payload.ticket_type
    )

    return {
        "id": new_ticket.id,
        "user": new_ticket.user.username,
        "title": new_ticket.title,
        "description": new_ticket.description,
        "ticket_type": new_ticket.ticket_type,
        "created_at": new_ticket.created_at,
        "updated_at": new_ticket.updated_at
    }

@router.get("{ticket_id}")
def get_ticket(request, ticket_id: int):
    try:
        ticket = Ticket.objects.get(id = ticket_id)
    except Ticket.DoesNotExist:
        return {"error": "ticket not found"}

    return {
        "id": ticket.id,
        "user": ticket.user.username,
        "title": ticket.title,
        "description": ticket.description,
        "ticket_type": ticket.ticket_type,
        "created_at": ticket.created_at.isoformat(),
        "updated_at": ticket.updated_at.isoformat()
    }