import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AmbientBackground } from "@/components/ui/AmbientBackground";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "CampusAI Dashboard",
  description: "Unified Intelligence Dashboard for your campus",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${inter.className} antialiased`}
      >
        <AmbientBackground />
        
        <div className="relative min-h-screen pt-6">
          <header className="fixed top-6 left-1/2 -translate-x-1/2 z-40 w-full px-4">
            <div className="glass-card rounded-full px-6 py-3 flex items-center justify-between w-full max-w-2xl mx-auto shadow-2xl">
              <div className="flex items-center gap-3 animate-fade-in">
                <div className="w-8 h-8 rounded-full bg-white flex items-center justify-center">
                  <span className="text-sm font-bold text-black">C</span>
                </div>
                <div className="flex items-baseline gap-2">
                  <h1 className="text-sm font-semibold tracking-tight text-white">CampusAI</h1>
                  <span className="text-[10px] text-[var(--text-muted)] font-medium uppercase tracking-widest hidden sm:inline-block">Unified Intelligence</span>
                </div>
              </div>
            </div>
          </header>

          <div className="pt-28 pb-12">
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
