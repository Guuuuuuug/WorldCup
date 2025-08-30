import WorldCupList from "./components/WorldCupsList";
import WorldCupWins from "./components/WorldCupWins";
import WorldCupRunnerUps from "./components/WorldCupsRunnerUps";
import WorldCupThirdPlaces from "./components/WorldCupThirdPlaces";
import './App.css';
import { Routes, Route, NavLink } from "react-router-dom";
import Home from "./components/Home";


function App(){
  const linkStyle = ({ isActive }: { isActive: boolean }) => ({
    color: "white",
    fontWeight: isActive ? 700 : 400,
    textDecoration: "none",
  });

  
  return (
    <div>
      <nav style={{ padding: 10, background: "#222", display: "flex", gap:12 }}>
        <NavLink to="/" style={linkStyle}>Home</NavLink>
        <NavLink to="/worldcups" style={linkStyle}>World Cups</NavLink>
        <NavLink to="/wins" style={linkStyle}>Wins by Country</NavLink>
        <NavLink to="/runnerups" style={linkStyle}>Runner-ups</NavLink>
        <NavLink to="/thirdplaces" style={linkStyle}>3rd Places</NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/worldcups" element={<WorldCupList />} />
        <Route path="/wins" element={<WorldCupWins />} />
        <Route path="/runnerups" element={<WorldCupRunnerUps />}></Route>
        <Route path="/thirdplaces" element={<WorldCupThirdPlaces />}></Route>
      </Routes>
    </div>
  );
}

export default App;