import React from "react";
import Animation from "../components/Animation";
import { Outlet } from "react-router-dom";

const Signup = () => {
  return (
    <section className="signup-page">
      <Animation />
      <Outlet />
    </section>
  );
};

export default Signup;
