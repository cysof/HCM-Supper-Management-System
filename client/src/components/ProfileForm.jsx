import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { NavLink } from "react-router-dom";
const ProfileForm = () => {
  const [details, setDetails] = useState({
    email: "",
    firstName: "",
    lastName: "",
    phoneNumber: "",
    address: "",
  });
  const handleChange = (e) => {
    const { name, value } = e.target;
    setDetails({ ...details, [name]: value });
  };
  const handleSubmit = () => {
    console.log(user);
  };
  return (
    <section className="profile-component">
      <Form
        className="border border-primary-subtle p-4"
        onSubmit={handleSubmit}
      >
        <h2>Personal Details</h2>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            name="email"
            value={details.email}
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>First Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter First Name"
            name="firstName"
            value={details.firstName}
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Last Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Last Name"
            name="lastName"
            value={details.lastName}
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Phone Number</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Phone number"
            name="phoneNumber"
            value={details.phoneNumber}
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Address</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Address"
            name="address"
            value={details.address}
            onChange={(e) => handleChange(e)}
          />
        </Form.Group>
        <div className="profile-btn-div">
          <NavLink to="/signup/">
            <Button variant="primary" type="submit">
              Back
            </Button>
          </NavLink>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </div>
      </Form>
    </section>
  );
};

export default ProfileForm;
