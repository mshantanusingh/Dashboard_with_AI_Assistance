export function AmbientBackground() {
  return (
    <div className="fixed inset-0 overflow-hidden pointer-events-none z-0">
      {/* Huge blurred orbs for ambient lighting */}
      <div className="absolute top-[-10%] left-[-10%] w-[50vw] h-[50vw] bg-[var(--accent-indigo)]/10 rounded-full blur-[120px] animate-ambient" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[60vw] h-[60vw] bg-[var(--accent-cyan)]/5 rounded-full blur-[150px] animate-ambient" style={{ animationDelay: '-5s' }} />
      <div className="absolute top-[40%] left-[20%] w-[40vw] h-[40vw] bg-[var(--accent-violet)]/10 rounded-full blur-[100px] animate-ambient" style={{ animationDelay: '-10s' }} />
    </div>
  );
}
