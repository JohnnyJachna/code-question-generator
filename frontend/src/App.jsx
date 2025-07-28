import { ClerkProviderWithRoutes } from "./auth/ClerkProviderWithRoutes.jsx";
import { Routes, Rout } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <ClerkProviderWithRoutes>
      <Routes></Routes>
    </ClerkProviderWithRoutes>
  );
}

export default App;
