# Agency Supervisor Crew - Setup Guide

## What This Does

A **Supervisor Agent** that can delegate tasks to 150+ specialized agents from the agency-agents repo.

```
User → Supervisor Agent → Delegated Specialist Agent → Result
```

## Two Ways to Use

### Option A: Run Locally (With API Keys)

```bash
cd C:\agency-agents\CrewAI

# Set API keys
set GROQ_API_KEY=your_groq_key
set GEMINI_API_KEY=your_gemini_key

# Run chat
python src\agency_crew\main.py
```

### Option B: Import to CrewAI Web

1. Go to **https://app.crewai.com**
2. Create **New Crew**
3. Name: `agency-supervisor`
4. Set **Process**: Hierarchical

#### Add Supervisor Agent:
```
Role: Agency Supervisor
Goal: Coordinate and delegate tasks to the right specialist agent
Backstory: |
    You are the Agency Supervisor - a highly intelligent coordinator 
    managing 150+ specialized agents. You delegate tasks to the 
    perfect specialist based on their expertise.
LLM: Gemini 2.5 Flash
Allow Delegation: YES
```

#### Add Specialist Agents:

**Frontend Developer:**
```
Role: Frontend Developer
Goal: Build responsive, accessible web applications
Backstory: Expert in React, Vue, Angular, pixel-perfect UIs
LLM: Groq (Llama 3-70B)
```

**Backend Architect:**
```
Role: Backend Architect
Goal: Design scalable APIs and database systems
Backstory: Expert in REST/GraphQL, PostgreSQL, microservices
LLM: Groq (Llama 3-70B)
```

**AI Engineer:**
```
Role: AI Engineer
Goal: Build and deploy ML models
Backstory: Expert in TensorFlow, PyTorch, MLOps
LLM: Gemini 2.5 Flash
```

**DevOps Automator:**
```
Role: DevOps Automator
Goal: Build CI/CD pipelines and infrastructure
Backstory: Expert in Kubernetes, Docker, Terraform
LLM: Groq (Llama 3-70B)
```

**Security Engineer:**
```
Role: Security Engineer
Goal: Identify vulnerabilities and implement security
Backstory: Expert in threat modeling, secure code review
LLM: Gemini 2.5 Flash
```

**QA Engineer:**
```
Role: QA Engineer
Goal: Ensure quality through comprehensive testing
Backstory: Expert in test automation, performance testing
LLM: Groq (Llama 3-70B)
```

## Set Environment Variables

In CrewAI settings:
```
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## How It Works

1. You chat with the **Supervisor**
2. Supervisor **understands** your request
3. Supervisor **delegates** to the right specialist
4. Specialist **does the work**
5. Supervisor **synthesizes** and **returns result**

## Example Conversations

**"Build a React login form"**
→ Supervisor → Frontend Developer

**"Design our database schema"**
→ Supervisor → Backend Architect

**"Set up CI/CD for our app"**
→ Supervisor → DevOps Automator

**"Review our code for vulnerabilities"**
→ Supervisor → Security Engineer

**"Build an ML pipeline"**
→ Supervisor → AI Engineer + Data Engineer

## Available Specialists

### Engineering
- Frontend Developer, Backend Architect
- AI Engineer, Data Engineer
- DevOps, Security Engineer
- Mobile App Builder, QA Engineer
- Database Optimizer, SRE

### Design
- UI Designer, UX Researcher
- Brand Guardian, Visual Storyteller
- Whimsy Injector

### Marketing
- Content Creator, Growth Hacker
- SEO Specialist, Social Media Strategist
- TikTok Strategist, LinkedIn Creator

### Sales
- Outbound Strategist, Discovery Coach
- Deal Strategist, Proposal Strategist

### Testing
- Evidence Collector, Performance Benchmarker
- API Tester, Accessibility Auditor

...and 140+ more!

## Cloud Processing

✅ All processing on Groq/Gemini servers
✅ Your PC stays idle
✅ Real-time delegation via CrewAI AMP
