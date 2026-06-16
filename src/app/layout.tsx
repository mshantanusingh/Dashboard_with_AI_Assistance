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
        
        <div className="relative min-h-screen">
          <header className="fixed top-0 left-0 right-0 z-40 w-full px-8 py-4 border-b border-white/5 bg-[#0A0A0A]/80 backdrop-blur-md">
            <div className="max-w-7xl mx-auto flex items-center justify-between">
              <div className="flex items-center gap-3 animate-fade-in">
                <div className="w-7 h-7 rounded bg-white flex items-center justify-center">
                  <span className="text-xs font-bold text-black">C</span>
                </div>
                <div className="flex items-baseline gap-2">
                  <h1 className="text-sm font-semibold tracking-tight text-white">CampusAI</h1>
                  <span className="text-[10px] text-neutral-500 font-medium uppercase tracking-widest hidden sm:inline-block">Unified Intelligence</span>
                </div>
              </div>
            </div>
          </header>

          <div className="pt-24 pb-12">
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
