import { useState, useEffect } from "react";
import { api } from "../api";


type CountryThirdPlaces = {
    country: string;
    bronze: number;
    years: number[];
}

export default function WorldCupThirdPlaces() {
    const [data, setData] = useState<CountryThirdPlaces[]>([]);
    const [loading, setLoading] = useState(true);
    const [err, setError] = useState<string | null>(null);

    useEffect(() => {
        api.get<CountryThirdPlaces[]>("/worldcups/thirdplaces")
            .then(res => setData(res.data))
            .catch(err => setError(err?.message ?? "Failed to load third places"))
            .finally(() => setLoading(false));
    }, [])

    if (loading) return <div style={{ padding: 24 }}>Loading…</div>;
    if (err) return <div style={{ padding: 24, color: "crimson" }}>{err}</div>;
    if (!data.length) return <div style={{ padding: 24 }}>No data.</div>

    return (
        <div style={{ padding: 24, marginTop:40 }}>
            <h2 style={{ marginBottom:12, color: "black", textAlign: "center" }}>
                3rd Places by Country 🥉
            </h2>
            <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: 16 }}>
                <thead>
                    <tr style={{ background: "#111827", color: "white" }}>
                        <th style={{ padding: 8, textAlign: 'left'}}>Country</th>
                        <th style={{ padding: 8, textAlign: 'left'}}>3rd Places</th>
                        <th style={{ padding: 8, textAlign: 'left'}}>Years</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((rows) => (
                        <tr key={rows.country} style={{ background: "rgba(255,255,255,0.9)", color: 'black'}}>
                            <td style={{ padding: 8 }}>{rows.country}</td>
                            <td style={{ padding: 8 }}>{rows.bronze}</td>
                            <td style={{ padding: 8 }}>{rows.years.join(', ')}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}