# Phase 05 — Continuous Chat Loop

## Goal

Transform the application from a single-request script into a continuously running conversational interface.

## Problem

The previous implementation handled only one interaction.

Workflow:

User Message
↓
Model Response
↓
Program Terminates

To ask another question, the user had to restart the application.

This behavior was inconvenient and did not resemble a real AI assistant.

## Solution

Introduce a continuous input loop using Python's while statement.

The application now remains active after each response and waits for additional user input.

Workflow:

User Message
↓
Model Response
↓
Wait For Next Message
↓
Model Response
↓
Wait For Next Message

This cycle continues until the user explicitly exits the application.

## Implementation

A loop was added around the interaction logic:

while True

Each iteration:

1. Reads user input
2. Sends the prompt to the model
3. Prints the response
4. Returns to the input prompt

## Exit Mechanism

A special command was introduced:

exit

When the user enters:

exit

the application breaks out of the loop and terminates gracefully.

Example:

You > exit

Goodbye Aditya....

## Benefits

* Multiple interactions per session
* Improved usability
* More natural conversational workflow
* Foundation for future conversation memory

## Lessons Learned

* Long-running applications require control flow management.
* User input loops are a fundamental pattern in CLI development.
* Exit conditions should be handled explicitly.
* Building functionality incrementally simplifies debugging.

## Outcome

AdityaCLI evolved from a single-request utility into a persistent conversational assistant capable of handling multiple interactions within the same session.
