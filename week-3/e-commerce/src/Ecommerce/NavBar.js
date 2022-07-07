import ThemeContext from "./ThemeContext";
import { useContext, useState } from "react";
import { Link } from "react-router-dom";

function NavBar() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <div className="nav-bar">
      <button onClick={toggleTheme} className="button">
        Click me to change theme.
      </button>
      <a href="/">
        <div className="logo">E-COMMERCE</div>
      </a>
      <div className="cart-icon">
        <Link to="/cart">
          <img src="https://upload.wikimedia.org/wikipedia/commons/d/df/Shopping_cart_icon.svg"></img>
        </Link>
      </div>
    </div>
  );
}

export default NavBar;
