import { Link } from "react-router-dom";

const cardStyle: React.CSSProperties = {
  textDecoration: "none",
  background: "rgba(255,255,255,0.9)",
  color: "#111827",
  padding: "16px 18px",
  borderRadius: 12,
  border: "1px solid #e5e7eb",
  boxShadow: "0 1px 2px rgba(0,0,0,0.06)"
};

const cardTitle: React.CSSProperties = { 
  margin: "0 0 6px", 
  fontSize: 18, 
  fontWeight: 700 
};

const cardText: React.CSSProperties  = { 
  margin: 0, 
  fontSize: 14, 
  color: "#374151" 
};

export default function Home() {
    return (
        <main style={{ padding: 24, maxWidth: 900, margin: "0 auto", color: 'black' }}>
            <section style={{ textAlign: 'center', marginBottom: 28 }}>
                <h1 style={{ fontSize: 36, marginBottom: 12 }}>FIFA World Cup - History & Stats</h1>
                <p style={{ opacity: 0.9, lineHeight: 1.6, color: "black" }}>
                    The FIFA World Cup is the biggest tournament in international football. 
                    Held every four years since 1930 (with interruptions in 1942 and 1946 due to WWII), 
                    it has crowned legends and created iconic moments—from Uruguay’s early glory to 
                    Maracanazo in 1950, Pelé’s Brazil, Maradona’s 1986 run, and Messi’s triumph in 2022.
                </p>
            </section>

            <section style={{ 
                display: "grid",
                gap: 16,
                gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))"
            }}>
                <Link to="/worldcups" style={cardStyle}>
                    <h3 style={cardTitle}>All World Cups</h3>
                    <p style={cardText}>Browse each tournament, final score, venue, attendance and more.</p>
                </Link>

                <Link to="/wins" style={cardStyle}>
                    <h3 style={cardTitle}>Wins by Country</h3>
                    <p style={cardText}>See which nations have the most World Cup titles. 🏆</p>
                </Link>

                <Link to="/runnerups" style={cardStyle}>
                    <h3 style={cardTitle}>Runner-ups</h3>
                    <p style={cardText}>
                        See which countries reached the finals but finished second across all World Cups.
                    </p>
                </Link>
                
                <Link to="/thirdplaces" style={cardStyle}>
                    <h3 style={cardTitle}>3rd Places</h3>
                    <p style={cardText}>
                        Discover the nations that claimed bronze in World Cup history and how often they reached the podium.
                    </p>
                </Link>
            </section>
        </main>
    )
}

