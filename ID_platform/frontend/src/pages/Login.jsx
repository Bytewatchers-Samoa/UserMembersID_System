import { useState } from "react";
import { login } from "../api/auth";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e){
    e.preventDefault();
    setError("");

    try {
      const data = await login(email, password);
      localStorage.setItem("token", data.access_token);
      alert("Login successful!");
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="page">
      <h1>Bytewatchers</h1>
      <h2>Welcome back</h2>

      <form onSubmit={handleSubmit} className="login-form">
        <input
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit" className="login-button">Login</button>

        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
}
