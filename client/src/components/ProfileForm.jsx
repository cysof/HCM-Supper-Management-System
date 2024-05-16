import React from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { IoIosArrowBack } from "react-icons/io";
import { NavLink } from "react-router-dom";
const ProfileForm = () => {
  return (
    <section className="profile-component">
      <Form className="border border-primary-subtle p-4">
        <h2>Personal Details</h2>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>First Name</Form.Label>
          <Form.Control type="text" placeholder="Enter First Name" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Last Name</Form.Label>
          <Form.Control type="text" placeholder="Enter Last Name" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Phone Number</Form.Label>
          <Form.Control type="text" placeholder="Enter Phone number" />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Address</Form.Label>
          <Form.Control type="text" placeholder="Enter Address" />
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
