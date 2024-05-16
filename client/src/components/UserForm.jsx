import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { NavLink } from "react-router-dom";

const UserForm = () => {
  const [visiblePassword, setVisiblePassword] = useState(false);
  const [visibleCPassword, setVisisibleCPassword] = useState(false);
  const [credentials, setCredentials] = useState({
    username: "",
    password: "",
    cpassword: "",
  });
  const toggleVisisbility = () => {
    setVisiblePassword(!visiblePassword);
  };
  const toggleCPasswordVsisibility = () => {
    setVisisibleCPassword(!visibleCPassword);
  };
  return (
    <section className="userform-component">
      <Form className="border border-primary-subtle p-4">
        <h2>Sign Up</h2>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter username"
            value={credentials.username}
            onChange={(e) =>
              setCredentials({ ...credentials, username: e.target.value })
            }
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <div className="password-input-wrapper">
            <Form.Control
              type={visiblePassword ? "text" : "password"}
              placeholder="Password"
              name="password"
              value={credentials.password}
              className="password-input"
              onChange={(e) =>
                setCredentials({ ...credentials, password: e.target.value })
              }
            />
            <span onClick={toggleVisisbility}>
              {visiblePassword ? "Hide" : "Show"}
            </span>
          </div>
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Confirm Password</Form.Label>
          <div className="password-input-wrapper">
            <Form.Control
              type={visibleCPassword ? "text" : "password"}
              placeholder="Confirm Password"
              name="cpassword"
              value={credentials.cpassword}
              className="password-input"
              onChange={(e) =>
                setCredentials({ ...credentials, cpassword: e.target.value })
              }
            />
            <span onClick={toggleCPasswordVsisibility}>
              {visibleCPassword ? "Hide" : "Show"}
            </span>
          </div>
        </Form.Group>
        <div className="next-btn-div">
          <NavLink to="/signup/profile">
            <Button variant="primary" type="submit">
              Next
            </Button>
          </NavLink>
        </div>
      </Form>
    </section>
  );
};

export default UserForm;
