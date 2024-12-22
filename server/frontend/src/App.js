import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Register from './components/Register/Register'; // adjust the path based on where your Register component is located


function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}
export default App;
