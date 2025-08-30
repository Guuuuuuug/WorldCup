import { useEffect, useState } from "react";
import { api } from "../api";

type WinsData = {
    country: string;
    titles: number;
    year: number[];
};

export default function WorldCupWins() {
    const [data, setData] = useState<WinsData[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        api
        .get<WinsData[]>("/worldcups/wins")
        .then((res) => setData(res.data))
        .catch((err) => {
            console.error("API error", err);
            setError(err?.message ?? "Failed to load wins data");
        })
        .finally(() => setLoading(false));
    }, []);

    if (loading) return <div style={{ padding: 24 }}>Loading wins...</div>;
    if (error) return <div style={{ padding: 24, color: "crimson" }}>{error}</div>;
    if (!data.length) return <div style={{ padding: 24 }}>No stats yet.</div>;

    return (
        <div style={{ padding: 24, marginTop: 40 }}>
            <h2 style={{ color: "black", textAlign: 'center'}}>🏆 Wins by Country</h2>
            <table style={{ width: "100%", borderCollapse: "collapse", marginTop: 16 }}>
                <thead>
                    <tr style={{ background: "#111827", color: 'white' }}>
                        <th style={{ padding: 8, textAlign: "left" }}>Country</th>
                        <th style={{ padding: 8, textAlign: "left" }}>Wins</th>
                        <th style={{ padding: 8, textAlign: "left" }}>Years</th>
                    </tr>                   
                </thead>
                <tbody>
                    {data.map((row) => (
                        <tr key={row.country} style={{ background: "rgba(255,255,255,0.9)", color: "black"}}>
                            <td style={{ padding: 8 }}>{row.country}</td>
                            <td style={{ padding: 8 }}> {row.titles}</td>
                            <td style={{ padding: 8 }}> {row.year.join(", ")}</td>
                        </tr>
                    ))}
                </tbody>          
            </table>
        </div>
    );
}