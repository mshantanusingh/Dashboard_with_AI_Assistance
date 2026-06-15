import { LibraryCard } from "@/components/dashboard/LibraryCard";
import { CafeteriaCard } from "@/components/dashboard/CafeteriaCard";
import { EventsCard } from "@/components/dashboard/EventsCard";
import { AcademicsCard } from "@/components/dashboard/AcademicsCard";
import { ChatWidget } from "@/components/chat/ChatWidget";
import { ServerStatusDisplay } from "@/components/dashboard/ServerStatusDisplay";

export default function Home() {
  return (
    <main className="min-h-screen px-8 py-10 max-w-7xl mx-auto relative z-10">
      <div className="mb-10 animate-fade-in delay-100 flex justify-between items-end">
        <div>
          <h2 className="text-3xl font-semibold tracking-tight text-white mb-1">
            Good afternoon.
          </h2>
          <p className="text-[var(--text-secondary)] text-sm font-medium">
            Here's your campus intelligence overview for today.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <ServerStatusDisplay />
        </div>
      </div>

      <div className="bento-grid">
        <div className="animate-fade-in delay-200 h-full"><LibraryCard /></div>
        <div className="animate-fade-in delay-300 h-full"><CafeteriaCard /></div>
        <div className="animate-fade-in delay-400 h-full"><EventsCard /></div>
        <div className="animate-fade-in delay-400 h-full"><AcademicsCard /></div>
      </div>

      <ChatWidget />
    </main>
  );
}
