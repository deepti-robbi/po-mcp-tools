# CogniAuraFit — Lifestyle Recommendation MCP Server

CogniAuraFit is a **Model Context Protocol (MCP) server** that delivers personalized lifestyle recommendations for patients based on their medical conditions. It exposes structured health advice — covering exercise routines, diet guidance, and general wellness tips — as MCP tools that any MCP-compatible AI client can call.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Tools Reference](#tools-reference)
  - [greet](#greet)
  - [exercise\_tips](#exercise_tips)
  - [diet\_tips](#diet_tips)
  - [general\_tips](#general_tips)
- [Supported Medical Conditions](#supported-medical-conditions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Configuration](#configuration)
- [Response Format](#response-format)

---

## Overview

CogniAuraFit bridges AI assistants and healthcare lifestyle guidance. The server exposes domain-specific knowledge as callable MCP tools, allowing an AI agent or chatbot to programmatically fetch:

- **Exercise recommendations** — aerobic, strength training, flexibility, and daily yoga poses
- **Diet recommendations** — foods to eat and foods to avoid
- **General wellness tips** — condition-specific lifestyle habits and monitoring advice

The server is condition-aware. Each tool inspects the medical condition provided in the query and returns tailored advice for that condition, falling back to general wellness guidance when the condition is not specifically recognized.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MCP Client / AI Agent                │
│                      (client.py)                        │
└────────────────────────┬────────────────────────────────┘
                         │  HTTP  (StreamableHttpTransport)
                         │  http://127.0.0.1:9002/mcp
┌────────────────────────▼────────────────────────────────┐
│              FastMCP Server  (server.py)                │
│              Server Name: "CogniAuraFit"                │
│                                                         │
│   Registered Tools                                      │
│   ├── greet          →  tools/greet.py                  │
│   ├── exercise_tips  →  tools/exercise.py               │
│   ├── diet_tips      →  tools/diet.py                   │
│   └── general_tips   →  tools/general.py                │
└─────────────────────────────────────────────────────────┘
```

- **Transport**: Streamable HTTP (stateless request/response)
- **Framework**: [FastMCP](https://github.com/jlowin/fastmcp) — a Python framework for building MCP servers
- **Concurrency**: Tools are `async` functions; the client uses `asyncio.gather()` to call all three recommendation tools in parallel

---

## Project Structure

```
po-mcp-tools/
├── main.py          # Entry point — starts the FastMCP server
├── server.py        # MCP server definition and tool registration
├── client.py        # Reference client — demonstrates parallel tool calls
├── config.py        # Environment-based configuration (port)
├── __init__.py
└── tools/
    ├── greet.py     # Tool: greet — simple name greeting
    ├── exercise.py  # Tool: exercise_tips — exercise recommendations
    ├── diet.py      # Tool: diet_tips — dietary recommendations
    └── general.py   # Tool: general_tips — general wellness tips
```

---

## Tools Reference

### `greet`

A simple utility tool for validating connectivity.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | `str` | No | `"World"` | Name of the person to greet |

**Returns**: `str` — A greeting message.

**Example**:
```
Input:  name = "Alice"
Output: "Hello, Alice!"
```

---

### `exercise_tips`

Returns structured exercise recommendations for a patient's medical condition.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `patient_id` | `str` | Yes | UUID identifying the patient |
| `query` | `str` | Yes | Medical condition (e.g., `"hypertension"`, `"diabetes"`) |

**Returns**: `dict` with condition-specific exercise recommendations including aerobic, strength training, flexibility exercises, and daily yoga poses.

**Example**:
```python
await exercise_tips(patient_id="c947658d-...", query="hypertension")
```

---

### `diet_tips`

Returns dietary recommendations tailored to a patient's medical condition.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `patient_id` | `str` | Yes | UUID identifying the patient |
| `query` | `str` | Yes | Medical condition |

**Returns**: `dict` with lists of recommended foods and foods to avoid for the given condition.

---

### `general_tips`

Returns general lifestyle and wellness tips for a patient's medical condition.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `patient_id` | `str` | Yes | UUID identifying the patient |
| `query` | `str` | Yes | Medical condition |

**Returns**: `dict` with actionable wellness tips covering monitoring, medication adherence, stress management, sleep, and more.

---

## Supported Medical Conditions

All three recommendation tools (`exercise_tips`, `diet_tips`, `general_tips`) support the following conditions. Matching is **case-insensitive**.

| Condition | Query String | Coverage |
|-----------|-------------|----------|
| Hypertension | `"hypertension"` | Exercise, Diet, General tips |
| Diabetes | `"diabetes"` | Exercise, Diet, General tips |
| Sore Throat | `"sore throat"` | Diet, General tips |
| All others | any other string | Generic fallback recommendations |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [FastMCP](https://github.com/jlowin/fastmcp) installed

```bash
pip install fastmcp fastapi
```

### Running the Server

```bash
fastmcp run main.py --transport http --host 127.0.0.1 --port 9002
```

The server will be available at `http://127.0.0.1:9002/mcp`.

To use a different port, set the `LIFESTYLE_MCP_PORT` environment variable (see [Configuration](#configuration)).

### Running the Client

With the server running, execute the reference client to see all tools called in parallel for the `"hypertension"` condition:

```bash
python client.py
```

The client will:
1. Connect to the server via HTTP transport
2. Call `general_tips`, `diet_tips`, and `exercise_tips` concurrently using `asyncio.gather()`
3. Print the consolidated JSON response

---

## Configuration

| Environment Variable | Default | Description |
|----------------------|---------|-------------|
| `LIFESTYLE_MCP_PORT` | `9003` | Port for the MCP server (note: `main.py` hardcodes `9002` — update both if changing) |

---

## Response Format

All three recommendation tools return a dictionary following this general structure:

```json
{
  "condition": "hypertension",
  "recommendations": {
    "general_tips": [
      "Monitor blood pressure regularly",
      "..."
    ],
    "diet": {
      "recommended": ["Leafy greens", "Berries", "..."],
      "avoid": ["High-sodium foods", "..."]
    },
    "exercise": {
      "aerobic": { "activities": ["..."], "duration": "..." },
      "strength_training": { "activities": ["..."], "frequency": "..." },
      "flexibility": { "activities": ["..."] }
    },
    "daily_yoga": [
      "Tadasana (Mountain Pose)",
      "Vrikshasana (Tree Pose)",
      "..."
    ]
  }
}
```

The exact keys present depend on which tool is called and which condition is matched.
