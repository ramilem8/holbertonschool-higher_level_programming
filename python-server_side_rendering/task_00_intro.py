#!/usr/bin/env python3
"""
task_00_intro.py - Generates personalized invitation files from a template.
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def generate_invitations(template, attendees):
    # --- Type validation ---
    if not isinstance(template, str):
        logging.error(
            "Invalid input: 'template' must be a string, got %s.",
            type(template).__name__,
        )
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        logging.error(
            "Invalid input: 'attendees' must be a list of dictionaries."
        )
        return

    # --- Empty input checks ---
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # --- Placeholders expected in the template ---
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # --- Process each attendee ---
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            replacement = str(value) if value is not None else "N/A"
            invitation = invitation.replace(f"{{{key}}}", replacement)

        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(invitation)

        logging.info("Generated: %s", output_filename)