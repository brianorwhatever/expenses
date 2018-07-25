def expense_reducer(previous_event, current_event):
    event_type = current_event.get('data').get('event_type')
    if event_type == 'ExpenseCreated':
        return current_event.get('data').get('expense')
    elif event_type == 'ExpenseUpdated':
        price = current_event.get('data').get('expense').get('price') \
            or previous_event.get('data').get('expense').get('price')
        paid_by = current_event.get('data').get('expense').get('paid_by') \
            or previous_event.get('data').get('expense').get('paid_by')
        description = current_event.get('data').get('expense').get('description') \
            or previous_event.get('data').get('expense').get('description')
        return {
            'content': {
                'price': price,
                'description': description,
                'paid_by': paid_by
            }
        }