import React from "react";
import Lottie from "react-lottie";
import shopping from "../lotties/shopping.json";

const Animation = () => {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: shopping,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };
  return (
    <section className="animation-component">
      <div className="animation-container">
        <Lottie
          className="animation"
          options={defaultOptions}
          isClickToPauseDisabled={true}
        />
      </div>
      <p>HCM supermarket</p>
    </section>
  );
};

export default Animation;
