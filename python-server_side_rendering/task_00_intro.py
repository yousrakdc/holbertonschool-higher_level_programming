import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A"
        invitation = template.format(
            name=attendee.get("name", "N/A") or "N/A",
            event_title=attendee.get("event_title", "N/A") or "N/A",
            event_date=attendee.get("event_date", "N/A") or "N/A",
            event_location=attendee.get("event_location", "N/A") or "N/A"
        )

        # Write the processed template to the output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)
        
        print(f"Generated {output_filename}")
