import { useEffect, useState } from "react";
import { api } from "../api";

type WorldCup = {
  id: number;
  year: number;
  host: string;
  winner: string;
  runner_up: string;
  third_place?: string | null;
  final_score: string;
  stadium: string;
  referee?: string | null;
  attendance?: number | null;
  image_url?: string | null;
  continent?: string | null;
};

const fallback =
  "https://upload.wikimedia.org/wikipedia/commons/d/d5/Uruguay_national_football_team_1930.jpg";

export default function WorldCupsList() {
  const [data, setData] = useState<WorldCup[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedId, setExpandedId] = useState<number | null>(null);

  useEffect(() => {
    api
      .get<WorldCup[]>("/worldcups")
      .then((res) => {
        const sorted = [...res.data].sort((a, b) => a.year - b.year);
        setData(sorted);
      })
      .catch((err) => {
        console.error("API error:", err);
        setError(err?.message ?? "Failed to load World Cups");
      })
      .finally(() => setLoading(false));
  }, []);

  const toggle = (id: number) => {
    setExpandedId((prev) => (prev === id ? null : id));
  };

  if (loading) return <div style={{ padding: 24 }}>Loading…</div>;
  if (error) return <div style={{ padding: 24, color: "crimson" }}>{error}</div>;
  if (!data.length) return <div style={{ padding: 24 }}>No World Cups yet.</div>;

  return (
    <div style={{ padding: 24 }}>
      <h1 style={{ 
        marginBottom: 16, 
        color: "black", 
        textAlign: 'center',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        gap: '8px'
         }}
        >
            World Cups
            <img 
            src="https://cdn.britannica.com/85/139485-050-BCF84C18/FIFA-World-Cup-trophy.jpg" 
            alt="smile" 
            style={{width: 50, height: 60}}    
        />
        </h1>

      <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
        {data.map((cup) => {
          const isOpen = expandedId === cup.id;
          const src = cup.image_url || fallback;

          return (
            <article
              key={cup.id}
              style={{
                display: "grid",
                gridTemplateColumns: isOpen ? "minmax(220px, 40%) 1fr" : "1fr",
                border: "1px solid #e5e7eb",
                borderRadius: 12,
                overflow: "hidden",
                background: "rgba(255,255,255,0.9)",
                boxShadow: "0 1px 2px rgba(0,0,0,0.06)",
                backdropFilter: "blur(2px)",
                
              }}
            >
              {/* LEFT: image (only when expanded) */}
              {isOpen && (
                <div style={{ position: "relative", minHeight: 180 }}>
                  <img
                    src={src}
                    alt={`${cup.year} World Cup — ${cup.winner} vs ${cup.runner_up}`}
                    onError={(e) => {
                      (e.target as HTMLImageElement).src = fallback;
                    }}
                    style={{ width: "100%", height: "100%", objectFit: "cover" }}
                  />
                  <div
                    style={{
                      position: "absolute",
                      top: 8,
                      left: 8,
                      background: "rgba(0,0,0,0.6)",
                      color: "white",
                      padding: "2px 8px",
                      borderRadius: 6,
                      fontSize: 12,
                    }}
                  >
                    {cup.continent ?? "—"}
                  </div>
                </div>
              )}

              {/* RIGHT: content */}
              <div
                style={{
                  padding: 16,
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "space-between",
                }}
              >
                <div>
                  <h2 style={{ margin: "0 0 6px", fontSize: 18, color: 'black' }}>
                    {cup.year} — {cup.host}
                  </h2>

                  <p style={{ margin: "0 0 8px", color: "#374151" }}>
                    <strong>{cup.winner}</strong> beat <strong>{cup.runner_up}</strong> (
                    {cup.final_score})
                    {cup.stadium ? ` in ${cup.stadium}` : ""}.
                  </p>

                  {cup.third_place && (
                    <p style={{ margin: 0, color: "#6b7280", fontSize: 14 }}>
                      3rd place: {cup.third_place}
                    </p>
                  )}
                </div>

                {/* Button */}
                <div style={{ marginTop: 10 }}>
                  <button
                    onClick={() => toggle(cup.id)}
                    aria-expanded={isOpen}
                    aria-controls={`details-${cup.id}`}
                    style={{
                      padding: "6px 10px",
                      borderRadius: 8,
                      border: "1px solid #d1d5db",
                      background: isOpen ? "#111827" : "#f9fafb",
                      color: isOpen ? "white" : "#111827",
                      cursor: "pointer",
                    }}
                  >
                    {isOpen ? "Less" : "More"}
                  </button>
                </div>

                {/* Expanded meta */}
                {isOpen && (
                  <div id={`details-${cup.id}`} style={{ marginTop: 12, fontSize: 14, color: 'black' }}>
                    {cup.referee && <p>Referee: {cup.referee}</p>}
                    {cup.attendance != null && (
                      <p>Attendance: {cup.attendance.toLocaleString?.() ?? cup.attendance}</p>
                    )}
                    {cup.continent && <p>Continent: {cup.continent}</p>}
                  </div>
                )}
              </div>
            </article>
          );
        })}
      </div>
    </div>
  );
}
