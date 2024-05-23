import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import UserForm from "./components/UserForm";
import ProfileForm from "./components/ProfileForm";
function App() {
  return (
    <Routes>
      <Route path="/" element={<Signup />}>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<UserForm />} />
        <Route path="/signup/profile" element={<ProfileForm />} />
      </Route>
    </Routes>
  );
}

export default App;
