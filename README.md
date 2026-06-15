# CampusAI — Unified Campus Intelligence Dashboard

A modern, AI-powered centralized dashboard for university campuses, built with **Next.js**, **React**, and the **Model Context Protocol (MCP)**.

## 🌟 The Problem
College campuses have data scattered everywhere: the library uses one portal, the cafeteria menu is a PDF, events are on Google Calendars, and academic handbooks are massive PDFs. Students waste time digging through 5 different systems just to find information.

## 🚀 The Solution
This project implements an **Agentic AI Architecture**. Instead of building massive, brittle web scrapers that dump everything into one giant database, we built independent **MCP (Model Context Protocol) Servers** for each campus data source.

An embedded AI Assistant dynamically routes questions to these servers in real-time, pulling live data and synthesizing answers.

## 🏗️ Architecture

1. **Frontend Dashboard** (Next.js 15, React, Tailwind CSS)
   - Real-time Bento Grid widgets for Library, Cafeteria, Events, and Academics.
   - Beautiful Glassmorphism UI design system.
   - Embedded Chat Widget.

2. **AI Orchestrator** (Next.js API Route)
   - Server-side integration with **Google Gemini 2.0 Flash**.
   - Discovers tools across all MCP servers dynamically.
   - Multi-turn function calling to route LLM intents to the appropriate microservices.

3. **Independent MCP Servers** (Python, FastAPI)
   - `library` (Port 8001): Book availability, search, hours.
   - `cafeteria` (Port 8002): Daily mess menu, nutrition.
   - `events` (Port 8003): Upcoming campus events and clubs.
   - `academics` (Port 8004): Class schedules, syllabus.

## 🛠️ Setup & Run Instructions

### 1. Prerequisites
- Node.js (v18+)
- Python (v3.10+)

### 2. Environment Variables
Copy `.env.example` to `.env.local` in the project root:
```bash
cp .env.example .env.local
```
Add your **Gemini API Key**:
```
GEMINI_API_KEY=your_api_key_here
```

### 3. Start All Services
We provided a convenient PowerShell script to start all 4 MCP servers and the Next.js frontend in parallel.

From the project root:
```powershell
.\scripts\start-all.ps1
```

Once running, access the dashboard at: **http://localhost:3000**

## 💡 Example Queries to ask the AI
- *"What's for lunch today?"*
- *"Are there any available copies of 'Clean Code' in the library?"*
- *"What classes do I have today?"*
- *"Are there any events happening this week? Also, what's for dinner?"* (Multi-tool invocation!)

## 🎨 Design System
- Built with custom CSS properties (`globals.css`).
- Inter font family.
- Uses `lucide-react` for beautiful iconography.
- Fully responsive Bento Grid layout.
