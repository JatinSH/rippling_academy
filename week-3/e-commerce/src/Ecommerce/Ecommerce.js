import { useContext, useState } from "react";
import EcommerceHome from "./EcommerceHome/EcommereceHome";
import ThemeContext from "./ThemeContext";
import "./Ecommerce.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Cart from "./Cart/Cart";
import NavBar from "./NavBar";

function Ecommerce() {
  //replace light n dark with const
  const [theme, setTheme] = useState("light");
  function toggleTheme() {
    console.log("hi");
    if (theme === "dark") {
      setTheme("light");
    } else {
      setTheme("dark");
    }
  }

  function initialzeLocalStorage() {
    localStorage.setItem("cart", JSON.stringify([]));
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <BrowserRouter>
        <NavBar></NavBar>
        <Routes>
          <Route path="/" element={<EcommerceHome></EcommerceHome>}></Route>
          <Route path="/cart" element={<Cart />}></Route>
        </Routes>
      </BrowserRouter>
    </ThemeContext.Provider>
  );
}
export default Ecommerce;
