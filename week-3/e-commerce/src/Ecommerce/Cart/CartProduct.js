import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function CartProduct(props) {
  const {
    product: { image, name, salePrice, sku, customerReviewAverage },
  } = props;

  const productsInCart = JSON.parse(localStorage.getItem("cart"));

  const currentProductIndex = productsInCart.findIndex(
    (element) => element.sku === sku
  );

  const [quantity, setQuantity] = useState(
    productsInCart[currentProductIndex].quantity
  );

  function handleTypeChange(event) {
    const newQuantity = event.target.value;
    const newProductsInCart = JSON.parse(localStorage.getItem("cart"));
    newProductsInCart[currentProductIndex].quantity = newQuantity;
    localStorage.setItem("cart", JSON.stringify(newProductsInCart));
    setQuantity(newQuantity);
    console.log(quantity);
  }

  function handleSubmit(event) {
    event.preventDefault();
  }

  function removeProductFromCart() {
    productsInCart.splice(currentProductIndex, 1);
    localStorage.setItem("cart", JSON.stringify(productsInCart));
  }

  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(productsInCart));
  }, [quantity]);
  return (
    <div className="product">
      <img src={image} className="product-image"></img>
      <div className="product-info">
        <div>
          <b>Product ID :</b> {sku}
        </div>
        <br></br>
        <div>
          <b>Name :</b> {name}
        </div>
        <br></br>
        <div>
          <b>Price :</b> {salePrice}
        </div>
        <br></br>
        <div>
          <b>Customer Review Rating :</b> {customerReviewAverage}/5
        </div>
        <br></br>
        <form onSubmit={handleSubmit}>
          <label>Quantity : </label>
          <input
            type="number"
            min="1"
            value={quantity}
            onChange={handleTypeChange}
          ></input>
        </form>
        <br></br>
        <a href="/cart">
          <button onClick={removeProductFromCart} className="button">
            Remove product from cart.
          </button>
        </a>
      </div>
    </div>
  );
}

export default CartProduct;
