# Hackathon Submission — Agents Assemble: The Healthcare AI Endgame Challenge

**Hackathon:** [Agents Assemble — The Healthcare AI Endgame Challenge](https://agents-assemble.devpost.com/)
**Organizer:** Prompt Opinion (Darena Health)
**Track:** Track 1 — Superpower (MCP-based)
**Submission Window:** March 4, 2026 – May 11, 2026

---

## Project Name

**CogniAuraFit**

> *Personalized lifestyle guidance, delivered as interoperable MCP tools for any healthcare AI agent.*

---

## Elevator Pitch

Patients with chronic conditions like hypertension and diabetes receive generic lifestyle advice that they rarely follow. CogniAuraFit exposes condition-aware, structured lifestyle recommendations — exercise routines, dietary guidance, and wellness tips — as MCP tools, so any AI agent in the healthcare ecosystem can fetch and deliver personalized guidance in real time, without rebuilding this logic from scratch.

---

## Problem Statement

Chronic disease management depends heavily on patient lifestyle — what they eat, how they move, how they sleep. Yet:

- Clinicians lack time to deliver detailed lifestyle counseling at every visit
- Generic health apps don't adapt to specific medical conditions
- AI health agents have no standardized way to access curated, condition-specific lifestyle knowledge

The result: patients leave appointments without actionable, personalized lifestyle guidance.

---

## Solution

CogniAuraFit is a **FastMCP-based MCP server** that exposes healthcare lifestyle knowledge as four callable tools. Any MCP-compatible AI agent can call these tools — passing a patient ID and medical condition — and receive structured, ready-to-deliver recommendations.

By packaging lifestyle intelligence as MCP tools, CogniAuraFit becomes a **reusable building block** in the healthcare AI ecosystem: plug it into any agent, any platform, any workflow.

---

## Track Justification — Track 1: Superpower (MCP-based)

CogniAuraFit is purpose-built for Track 1. It:

- Implements a **FastMCP server** exposing healthcare-specific tools via HTTP transport
- Tools are **agent-agnostic** — any MCP client can discover and call them without custom integration
- Follows the MCP tool contract: typed inputs, structured JSON outputs, async execution
- Designed to be **published to the Prompt Opinion Marketplace** as a reusable healthcare superpower

---

## How It Works

```
AI Agent / Chatbot
      │
      │  MCP Tool Call (HTTP)
      ▼
CogniAuraFit MCP Server (FastMCP)
      │
      ├── exercise_tips(patient_id, condition)  →  Exercise plan + yoga poses
      ├── diet_tips(patient_id, condition)       →  Recommended & avoided foods
      ├── general_tips(patient_id, condition)    →  Wellness & monitoring tips
      └── greet(name)                            →  Connectivity validation
```

1. An AI agent receives a patient query (e.g., "What lifestyle changes should I make for hypertension?")
2. The agent calls the relevant CogniAuraFit tools via MCP
3. Tools return structured JSON recommendations based on the patient's condition
4. The agent synthesizes and delivers the guidance to the patient in natural language

All three recommendation tools can be called **in parallel** using `asyncio.gather()`, reducing latency to a single round-trip.

---

## MCP Tools Exposed

| Tool | Input | Output |
|------|-------|--------|
| `exercise_tips` | `patient_id`, `query` (condition) | Aerobic, strength, flexibility exercises + daily yoga poses |
| `diet_tips` | `patient_id`, `query` (condition) | Recommended foods and foods to avoid |
| `general_tips` | `patient_id`, `query` (condition) | Lifestyle, monitoring, and wellness tips |
| `greet` | `name` | Greeting string (connectivity check) |

---

## Supported Medical Conditions

| Condition | Exercise | Diet | General Tips |
|-----------|----------|------|--------------|
| Hypertension | Yes | Yes | Yes |
| Diabetes | Yes | Yes | Yes |
| Sore Throat | — | Yes | Yes |
| General / Default | Fallback | Fallback | Fallback |

---

## Judging Criteria Alignment

### The AI Factor
CogniAuraFit transforms static clinical lifestyle guidelines into **dynamically callable AI tools**. Rather than hard-coding lifestyle advice into a single app, this MCP server makes the knowledge composable — any AI agent can layer it into its reasoning, combine it with patient history, lab values, or physician notes, and generate advice that traditional rule-based software cannot produce.

### Potential Impact
- **Patients** with chronic conditions get specific, actionable lifestyle guidance at scale — not generic pamphlets
- **Clinicians** can delegate routine lifestyle counseling to AI agents backed by structured, curated knowledge
- **Developers** get a ready-made MCP superpower they can integrate into their own healthcare agents without rebuilding the domain knowledge
- Conditions covered (hypertension, diabetes) affect **hundreds of millions of patients globally** — a meaningful surface area for impact

### Feasibility
- **Privacy-safe by design**: no PHI is stored or logged; `patient_id` is used only as a session identifier and is never persisted
- **No external data dependencies**: all recommendations are curated, structured, and self-contained within the server — no third-party API calls that could fail or leak data
- **Regulatory alignment**: recommendations follow standard lifestyle guidance aligned with established clinical practice (low-sodium diet for hypertension, low-glycemic for diabetes, etc.)
- **Lightweight deployment**: a single Python process, no database, no infrastructure complexity

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| MCP Framework | [FastMCP](https://github.com/jlowin/fastmcp) |
| Language | Python 3.8+ |
| Transport | Streamable HTTP |
| Concurrency | `asyncio` / `asyncio.gather()` |
| Server Port | `127.0.0.1:9002` (configurable via `LIFESTYLE_MCP_PORT`) |

---

## Running the Project

**Start the server:**
```bash
pip install fastmcp fastapi
fastmcp run main.py --transport http --host 127.0.0.1 --port 9002
```

**Run the reference client (demonstrates parallel tool calls for hypertension):**
```bash
python client.py
```

---

## Demo Video

> *[Link to demo video — under 3 minutes, showing CogniAuraFit tools called within the Prompt Opinion platform]*

The demo covers:
1. Starting the CogniAuraFit MCP server
2. An AI agent discovering the available tools
3. Parallel calls to `exercise_tips`, `diet_tips`, and `general_tips` for a hypertension patient
4. The consolidated lifestyle recommendation response delivered to the patient

---

## What's Next

- Expand condition coverage: cardiovascular disease, obesity, arthritis, anxiety
- Integrate FHIR patient context so recommendations adapt to lab values and vitals
- Add severity tiers within each condition (mild / moderate / severe hypertension)
- A2A interoperability: expose CogniAuraFit as an agent-callable skill in Track 2 workflows
- Publish to the Prompt Opinion Marketplace as a certified healthcare superpower

---

## Team

| Name | Role |
|------|------|
| Deepti | Developer & Domain Designer |
| Vandana | Developer |

---

*Built for the Agents Assemble — Healthcare AI Endgame Challenge.*
*Submitted under Track 1: Superpower (MCP-based).*
