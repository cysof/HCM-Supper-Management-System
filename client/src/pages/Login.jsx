import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { NavLink } from "react-router-dom";

const Login = () => {
  const [visible, setVisible] = useState(false);
  const [user, setUser] = useState({
    username: "",
    password: "",
  });
  const toggleVisibility = () => {
    setVisible(!visible);
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser({ ...user, [name]: value });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    // hit login endpoint
  };
  return (
    <div className="login-component">
      <Form onSubmit={handleSubmit}>
        <h2>Login</h2>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter username"
            value={user.username}
            name="username"
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <div className="password-input-wrapper">
            <Form.Control
              type={visible ? "text" : "password"}
              placeholder="Password"
              name="password"
              value={user.password}
              onChange={(e) => handleChange(e)}
            />
            <span onClick={toggleVisibility}>{visible ? "Hide" : "Show"}</span>
          </div>
        </Form.Group>
        <div className="login-btn">
          <NavLink to="/signup">Don't have an account? Sign up</NavLink>
          <Button variant="primary" type="submit">
            Login
          </Button>
        </div>
      </Form>
    </div>
  );
};

export default Login;
