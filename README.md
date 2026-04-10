# AutoStream Agent – Social-to-Lead Workflow

## Overview
This project is a conversational AI agent built for a fictional SaaS product "AutoStream".

It can:
- Answer product queries
- Provide pricing (using a knowledge base)
- Detect high-intent users
- Capture leads interactively

---

## Features

### Intent Detection
Detects:
- Greetings
- Pricing queries
- Purchase intent

### RAG (Retrieval-Augmented Generation)
Uses a local JSON file (`knowledge.json`) to fetch pricing dynamically.

### Lead Capture
Collects:
- Name
- Email (with validation)
- Platform

### Tool Execution
Simulates saving lead data.

---

## How to Run

```bash
python main.py

