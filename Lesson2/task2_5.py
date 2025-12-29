events = []


def work_with_events():
    """Gets operations with events"""

    def add(new_event: str):
        """Adds new event in the calendar"""
        events.append(new_event)
        print(f"Event '{new_event}' is added successfully")

    def delete(event: str):
        """Deletes specified event from the calendar"""
        if event in events:
            events.remove(event)
            print(f"Event '{event}' is deleted successfully")
        else:
            print(f"Event '{event}' is not found")

    def get_events() -> list:
        """Shows events in the calendar"""
        if not events:
            print("Event list is empty")
            return events
        for num, event in enumerate(events, 1):
            print(f'{num} - {event}')
        return events

    return add, delete, get_events


add_new_event, delete_event, get_available_events = work_with_events()

add_new_event("Meeting with Alex")
add_new_event("Meeting with Bob")
add_new_event("Meeting with Sarah")
add_new_event("Meeting with Frank")
get_available_events()
delete_event("Meeting with Alex")
get_available_events()
delete_event("Meeting with Alex")
get_available_events()
