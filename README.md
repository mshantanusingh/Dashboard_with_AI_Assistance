# CampusAI - Unified Campus Intelligence Dashboard 🎓🤖

A unified campus dashboard that brings together scattered university data—library systems, cafeteria menus, event calendars, and academic schedules—into one beautiful, real-time interface. Powered by an intelligent AI Assistant using the **Model Context Protocol (MCP)**.

---

## 📖 The Problem & The Solution

**The Problem:** College campuses suffer from deeply fragmented data. Students have to check a legacy portal for library books, a PDF for the cafeteria menu, a Google Calendar for club events, and a massive handbook for their class schedule. 

**Our Solution:** We built a unified web dashboard with an embedded AI Assistant. Instead of building brittle scrapers to dump data into a massive database, we built independent **Model Context Protocol (MCP) Servers** for each campus data source. The dashboard fetches real-time data directly from these servers, and the AI Assistant dynamically routes natural-language queries to them via LLM function calling.

## ✨ Key Features

- **Independent MCP Servers:** Four distinct Python-based MCP APIs serving data for `Academics`, `Library`, `Cafeteria`, and `Events`.
- **Intelligent AI Assistant:** Powered by `gemini-flash-lite-latest` with native tool-calling capabilities. Ask "What's for lunch?" or "Where is my computer networks class?" and it intelligently queries the exact right MCP server.
- **Unified Live Dashboard:** A premium, enterprise-grade React dashboard showing real-time updates from all campus servers simultaneously.
- **Zero-Database Architecture:** Live data is fetched dynamically. No stale databases.
- **Student Personalization:** Built-in Persona Switcher (Freshman CS vs. Senior Math) that filters academic and library data based on the active user's context.

## 🛠 Tech Stack

**Frontend & Orchestration:**
- **Framework:** Next.js (App Router) & React
- **Styling:** TailwindCSS, `lucide-react` icons
- **State Management:** React Context API
- **AI Integration:** Google Generative AI SDK (`@google/generative-ai`)

**Backend & MCP Servers:**
- **Framework:** Python (Serverless Functions via Vercel)
- **Protocol:** Model Context Protocol (HTTP Transport layer)

**Deployment:**
- **Hosting:** Vercel (Frontend + Serverless Python API routes)

## 🚀 Setup Instructions

### Prerequisites
- Node.js (v18+)
- Python 3.9+
- A Google Gemini API Key

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/mshantanusingh/Dashboard_with_AI_Assistance.git
   cd Dashboard_with_AI_Assistance
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env.local` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the Application**
   You can run everything simultaneously using Vercel's dev environment (recommended, as it handles the Python API routes automatically):
   ```bash
   npm i -g vercel
   vercel dev
   ```
   
   *Alternatively, if running via standard `npm run dev`, make sure your Python MCP servers are also running on the correct local ports and update your `.env.local` with the local URLs.*

6. Open [http://localhost:3000](http://localhost:3000) with your browser.

## 🌐 Deployed Demo

**Live Demo Link:** [Insert Vercel Deployment Link Here]

*(Note: Don't forget to add your deployed link to this README before submitting the hackathon!)*

## 🎥 Hackathon Demo Video

[Insert Link to 5-10 minute YouTube/Loom Demo Video]

---
*Built for the Unified Campus Intelligence Hackathon.*
