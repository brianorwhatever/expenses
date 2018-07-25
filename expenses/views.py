import json
from uuid import uuid4
from functools import reduce

from django.http import JsonResponse

from .models import ExpenseEventLog
from .reducer import expense_reducer

def create_expense(request):
    next_event = {
        "event_type": "ExpenseCreated",
        "expense": {"content": request.POST.dict()}
    }

    event = ExpenseEventLog.objects.create(
        guid=uuid4(),
        sequence=0,
        data=next_event
    )

    return JsonResponse(data={
        "guid": event.guid,
        "sequence": event.sequence,
        "data": event.data
    })

def edit_expense(request, expense_id):
    if request.method == "POST":
        previous_event = ExpenseEventLog.objects.filter(guid=expense_id)\
            .order_by('sequence').last()
        next_sequence = previous_event.sequence + 1
        next_event = {
            "event_type": "ExpenseUpdated",
            "expense": {"content": request.POST.dict()}
        }

        event = ExpenseEventLog.objects.create(
            guid=expense_id,
            sequence=next_sequence,
            data=next_event
        )

        return JsonResponse(data={
            "guid": event.guid,
            "sequence": event.sequence,
            "data": event.data
        })
    elif request.method == "GET":
        events = ExpenseEventLog.objects.filter(guid=expense_id)\
            .order_by('sequence').values('data')

        expense = reduce(expense_reducer, events)

        return JsonResponse(data={
            "guid": expense_id,
            "data": expense
        })
