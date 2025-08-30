import { useEffect, useState } from "react";
import { api } from "../api";

type CountryRunnerUps = {
    country: string;
    silver: number;
    years: number[];
};

export default function WorldCupRunnerUps() {
    const [data, setData] = useState<CountryRunnerUps[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        api.get<CountryRunnerUps[]>("/worldcups/runnerups")
            .then(res => setData(res.data))
            .catch(err => setError(err?.message ?? "Failed to load runner-ups"))
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <div style={{ padding: 24 }}>Loading…</div>;
    if (error) return <div style={{ padding: 24, color: "crimson" }}>{error}</div>;
    if (!data.length) return <div style={{ padding: 24 }}>No data.</div>;

    return (
        <div style={{ padding: 24, marginTop: 40 }}>
            <h2 style={{ marginBottom: 12, color: "black", textAlign: 'center' }}>
                Runner-ups by Country 🥈
            </h2>
            <table style={{ width: "100%", borderCollapse: "collapse", marginTop: 16 }}>
                <thead>
                    <tr style={{ background: "#111827", color: 'white' }}>
                        <th style={{ padding: 8, textAlign: "left" }}>Country</th>
                        <th style={{ padding: 8, textAlign: "left" }}>Runner-Ups</th>
                        <th style={{ padding: 8, textAlign: "left" }}>Years</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((row) => (
                        <tr key={row.country} style={{ background: "rgba(255,255,255,0.9)", color: "black"}}>
                            <td style={{ padding: 8 }}>{row.country}</td>
                            <td style={{ padding: 8 }}> {row.silver}</td>
                            <td style={{ padding: 8 }}> {row.years.join(', ')}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}