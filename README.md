# CampusAI - Unified Campus Intelligence Dashboard 🎓🤖

## 1. Project Overview

**The Problem:**
Modern university campuses suffer from deeply fragmented information systems. Students are forced to navigate multiple disparate platforms—a legacy portal for library resources, static PDFs for cafeteria menus, external calendars for club events, and separate handbooks for academic schedules. This friction leads to wasted time and missed opportunities.

**Our Solution & Target Users:**
CampusAI is a unified, intelligent web dashboard built for university students. It aggregates scattered campus data into a single, beautiful, and real-time interface. Instead of relying on brittle web scrapers or centralized databases, CampusAI leverages independent **Model Context Protocol (MCP) Servers** for each data source, ensuring modularity and real-time accuracy. 

**Key Objectives & Expected Outcomes:**
- **Centralize Information:** Bring Academics, Library, Cafeteria, and Events into one unified view.
- **Natural Language Access:** Allow students to query campus data seamlessly using an embedded AI Assistant.
- **Real-Time Accuracy:** Eliminate stale data through a zero-database, live-fetch architecture.
- **Personalized Context:** Filter information based on the student's specific persona and schedule.

---

## 2. Features

- **Independent MCP Architecture:** Four distinct microservices (Academics, Library, Cafeteria, and Events) run as independent Model Context Protocol servers, providing high cohesion and loose coupling.
- **Intelligent AI Assistant:** An embedded chatbot powered by Gemini with native function-calling capabilities. Students can ask questions like "What's for lunch?" or "Where is my next class?" and the AI dynamically routes the request to the correct MCP server.
- **Unified Live Dashboard:** A premium, interactive React dashboard that visualizes real-time updates from all campus domains simultaneously, without requiring a page reload.
- **Zero-Database Architecture:** Data is queried live from the source MCP servers, meaning there is no central database to maintain or keep synchronized.
- **Contextual Persona Personalization:** A built-in persona switcher tailors the academic and library data shown on the dashboard to the active user's major and academic year (e.g., Freshman CS vs. Senior Math).

---

## 3. Tech Stack

### Frontend
- **Next.js 16 (App Router) & React 19:** Provides a robust, server-rendered foundation for the unified dashboard.
- **Tailwind CSS v4 & Framer Motion:** Ensures a highly responsive, modern, and micro-animated user interface.
- **Lucide React:** Beautiful and consistent iconography.

### Backend
- **Python 3.9+ & FastAPI:** Powers the highly performant API and MCP servers.
- **Uvicorn:** ASGI web server implementation for Python.

### Database
- **Zero-Database Architecture:** Fetches data directly via MCP API routes in real-time, completely bypassing traditional databases.

### AI/ML Services
- **Google Generative AI SDK:** Integrates `gemini-flash-lite-latest` for natural language understanding and tool calling (LLM routing).

### APIs and Integrations
- **Model Context Protocol (MCP):** Standardized HTTP transport layer for connecting the AI Assistant seamlessly to the independent campus data domains.

### Deployment/Infrastructure
- **Vercel:** Hosts the Next.js frontend and serverless Python API routes.
- **Render:** Manages deployment of the standalone Python MCP servers.

### Development Tools
- **TypeScript:** Enforces type safety on the frontend.
- **ESLint & PostCSS:** Code quality and CSS transformation.

---

## 4. Architecture and Workflow

**System Architecture:**
CampusAI operates on a modular microservices architecture. The Next.js frontend serves as the orchestrator and user interface. Behind the scenes, four independent FastAPI servers run the MCP endpoints for Academics, Library, Cafeteria, and Events. 

**Data Flow:**
1. **User Interaction:** The user asks a question in the AI chat or interacts with dashboard widgets.
2. **AI Routing:** The Next.js application sends the query to the Gemini AI model, providing it with the schemas of all available MCP tools.
3. **Tool Execution:** If the AI determines it needs external data (e.g., the cafeteria menu), it issues a tool call. The frontend proxies this call to the respective Python MCP server via the `/api/` routes.
4. **Data Retrieval & Synthesis:** The Python MCP server processes the logic and returns the raw data. The Gemini AI synthesizes this data into a natural, conversational response.
5. **Dashboard Update:** Simultaneously, the React components fetch and render this live data visually on the dashboard.

---

## 5. Installation and Setup

### Prerequisites
- **Node.js:** v18 or higher
- **Python:** v3.9 or higher
- **API Key:** A valid Google Gemini API Key

### Local Development Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mshantanusingh/Dashboard_with_AI_Assistance.git
   cd Dashboard_with_AI_Assistance
   ```

2. **Install Frontend Dependencies:**
   ```bash
   npm install
   ```

3. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Configuration:**
   Create a `.env.local` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the Application:**
   Because the project utilizes serverless Python API routes, running the project via the Vercel CLI is recommended.
   
   First, install the Vercel CLI globally if you haven't already:
   ```bash
   npm install -g vercel
   ```
   
   Start the development server:
   ```bash
   vercel dev
   ```
   
   *(Alternatively, you can run the Next.js frontend using `npm run dev` and manually start the FastAPI servers in the `mcp-servers` directory on their respective local ports).*

6. **Access the Dashboard:**
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000).

---

## 6. Usage Guide

- **Dashboard Exploration:** Upon logging in, use the Persona Switcher at the top of the dashboard to simulate different student profiles. Watch as the Academic schedule and Library recommendations instantly adjust to fit the persona.
- **AI Assistant Interaction:** Open the chat interface and use natural language queries. 
  - *Example 1:* "What is being served for lunch in the main cafeteria today?"
  - *Example 2:* "Do I have any computer science classes tomorrow?"
  - *Example 3:* "Are there any tech events happening this weekend?"
- **Visual Widgets:** Review the dedicated cards for Academics, Events, Library, and Cafeteria for an at-a-glance view of your day.

---

## 7. Project Structure

```text
Dashboard_with_AI_Assistance/
├── api/                # Next.js / Vercel Serverless Python routes exposing MCP functionality
├── mcp-servers/        # Independent Python microservices
│   ├── academics/      # MCP server for courses, exams, and schedules
│   ├── cafeteria/      # MCP server for dining menus
│   ├── events/         # MCP server for campus events and clubs
│   └── library/        # MCP server for book availability and reservations
├── src/                # Next.js Frontend Application
│   ├── app/            # App Router (Pages, Layouts)
│   ├── components/     # Reusable React components (Dashboard widgets, UI elements)
│   ├── context/        # React Context for global state management
│   ├── hooks/          # Custom React hooks
│   └── lib/            # Utility functions and AI configurations
├── public/             # Static assets (images, fonts, icons)
├── package.json        # Frontend dependencies and npm scripts
├── requirements.txt    # Python backend dependencies
├── render.yaml         # Configuration for deploying MCP servers on Render
└── vercel.json         # Vercel configuration for API routes
```

---

## 8. Deployment

The deployment architecture is split between the frontend orchestrator and the backend MCP services:
- **Frontend & API Proxies (Vercel):** The Next.js app and the `/api/` Python serverless functions are deployed to Vercel. Connect the GitHub repository directly to Vercel for automatic deployments on push.
- **MCP Servers (Render):** The standalone MCP servers can be deployed to Render using the provided `render.yaml` configuration. Each server runs as an independent web service.

---

## 9. Demo and Links

- **Demo Link:** Not Yet Deployed
- **GitHub Repository:** [mshantanusingh/Dashboard_with_AI_Assistance](https://github.com/mshantanusingh/Dashboard_with_AI_Assistance)

---

## 10. Future Enhancements

- **LMS Integration:** Connect the Academics MCP server directly to real-world platforms like Canvas or Blackboard.
- **Authentication:** Implement robust student SSO authentication using NextAuth.js or Clerk.
- **Mobile Application:** Build a React Native counterpart for on-the-go access.
- **Push Notifications:** Alert students about immediate class cancellations or expiring library book loans.
- **Advanced Caching:** Implement Redis caching on the MCP servers to handle massive spikes in traffic during finals week or enrollment periods.

---

## 11. Contributing

We welcome contributions to make CampusAI even better! 
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

Please ensure your code follows the existing style guidelines and passes all ESLint checks before submitting a PR.

---

## 12. License

This project is licensed under the MIT License. See the `LICENSE` file for details.
