# Phase 03 — First API Call

## Goal

Establish successful communication between Python and the locally running Qwen3.5 9B model through LM Studio.

## Implementation

A minimal Python script was created using the OpenAI Python SDK.

The script:

1. Connects to LM Studio
2. Sends a user message
3. Receives a completion
4. Prints the response

## Architecture

Python Script
↓
OpenAI SDK
↓
LM Studio API
↓
Qwen3.5 9B
↓
Response

## Endpoint

http://127.0.0.1:1234/v1

## Model

qwen/qwen3.5-9b

## Result

Successfully received a response from the local model.

This validates the core communication layer required for the rest of the project.

## Lessons Learned

* LM Studio exposes an OpenAI-compatible API.
* The OpenAI SDK can be used with local models by changing the base URL.
* Local inference can be integrated without any cloud dependency.
* Verifying connectivity early reduces debugging complexity later.
