import { useContext, useEffect, useState } from "react";
import ThemeContext from "../ThemeContext";
import "../Ecommerce.css";
import Product from "./Product";

function buildPriceFilterString(priceFilterMinValue, priceFilterMaxValue) {
  return (
    "(salePrice>=" +
    priceFilterMinValue +
    "&salePrice<=" +
    priceFilterMaxValue +
    ")"
  );
}

function EcommerceHome() {
  const { theme, toggleTheme } = useContext(ThemeContext);
  const [homeProducts, setHomeProducts] = useState([]);
  const [filterOnPrice, setFilterOnPrice] = useState("");
  const [priceFilterString, setPriceFilterString] = useState("");
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(0);
  const [sortBy, setSortBy] = useState("sku");
  const [sortType, setSortType] = useState("asc");
  const [category, setCategory] = useState("");

  let url = `https://api.bestbuy.com/v1/products${category}${filterOnPrice}?apiKey=qhqws47nyvgze2mq3qx4jadt&sort=${sortBy}.${sortType}&show=customerReviewAverage,sku,image,name,salePrice&pageSize=10&format=json`;

  function categoryTV() {
    setCategory("(categoryPath.id=abcat0101000)");
  }
  function categoryLaptop() {
    setCategory("(categoryPath.id=abcat0502000)");
  }
  function categoryPS() {
    setCategory("(categoryPath.id=pcmcat295700050012)");
  }
  function categoryXB1() {
    setCategory("(categoryPath.id=pcmcat300300050002)");
  }
  function categoryHeadphones() {
    setCategory("(categoryPath.id=abcat0204000)");
  }
  function filterPrice0to10() {
    setFilterOnPrice("(salePrice>=0&salePrice<=10)");
    console.log(filterOnPrice);
  }

  function filterPrice10to100() {
    setFilterOnPrice("(salePrice>=10&salePrice<=100)");
    console.log(filterOnPrice);
  }

  function filterPrice100to500() {
    setFilterOnPrice("(salePrice>=100&salePrice<=500)");
    console.log(filterOnPrice);
  }

  function filterPrice500AndMore() {
    setFilterOnPrice("(salePrice>=500)");
    console.log(filterOnPrice);
  }

  function handleMinPrice(event) {
    setMinPrice(event.target.value);
  }

  function handleMaxPrice(event) {
    setMaxPrice(event.target.value);
  }

  function customPriceFilter() {
    console.log(priceFilterString);
    setFilterOnPrice(priceFilterString);
  }

  function sortByOption(event) {
    setSortBy(event.target.value);
  }

  function sortTypeOption(event) {
    setSortType(event.target.value);
  }

  async function fetchProducts() {
    let response = await fetch(url);
    let data = await response.json();
    setHomeProducts(data.products);
  }

  useEffect(() => {
    fetchProducts();
    setPriceFilterString(buildPriceFilterString(minPrice, maxPrice));
  }, [
    filterOnPrice,
    sortBy,
    sortType,
    minPrice,
    maxPrice,
    priceFilterString,
    category,
  ]);

  return (
    <div className={theme}>
      <div className="categories">
        <button onClick={categoryTV} className="button">
          TVs
        </button>
        <button onClick={categoryLaptop} className="button">
          Laptops
        </button>
        <button onClick={categoryPS} className="button">
          PlayStation 5
        </button>
        <button onClick={categoryXB1} className="button">
          Xbox One
        </button>
        <button onClick={categoryHeadphones} className="button">
          Headphones
        </button>
      </div>
      <div className="filters-products">
        <div className="filter-container">
          <div className="filter-heading">FILTERS</div>
          <div className="filters">
            <button onClick={filterPrice0to10} className="button">
              $0 - $10
            </button>
            <br></br>
            <button onClick={filterPrice10to100} className="button">
              $10 - $100
            </button>
            <br></br>
            <button onClick={filterPrice100to500} className="button">
              $100 - $500
            </button>
            <br></br>
            <button onClick={filterPrice500AndMore} className="button">
              {">"}$500
            </button>
            <br></br>
            <div>
              <span>$</span>
              <input
                type="number"
                style={{ width: 70 }}
                min="0"
                value={minPrice}
                onChange={handleMinPrice}
                className="input"
              ></input>
              <span> - $</span>
              <input
                type="number"
                style={{ width: 70 }}
                min="0"
                value={maxPrice}
                onChange={handleMaxPrice}
                className="input"
              ></input>
              <br></br>
              <br></br>
              <button onClick={customPriceFilter} className="button">
                Set custom price filter.
              </button>
            </div>
            <br></br>
            <div>Sort By : </div>
            <br></br>
            <select name="sortBy" onChange={sortByOption} className="input">
              <option value="salePrice">Price</option>
              <option value="customerReviewAverage">
                Customer Review Rating
              </option>
            </select>
            <br></br>
            <label>Sort Type : </label>
            <br></br>
            <select name="sortType" onChange={sortTypeOption} className="input">
              <option value="asc">Ascending</option>
              <option value="dsc">Descending </option>
            </select>
          </div>
        </div>
        <div>
          {homeProducts.map((homeProduct) => {
            return (
              <Product key={homeProduct.sku} product={homeProduct}></Product>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default EcommerceHome;
