function Product(props) {
  const {
    product: { image, name, salePrice, sku, customerReviewAverage },
  } = props;

  const currentProduct = props.product;
  currentProduct.quantity = 1;
  function addToCart() {
    const productsInCartString = localStorage.getItem("cart");
    const productsInCart = JSON.parse(productsInCartString);
    const searchProductIndex = productsInCart.findIndex(
      (element) => element.sku === sku
    );
    if (searchProductIndex > -1) {
      productsInCart[searchProductIndex].quantity++;
    } else {
      productsInCart.push(currentProduct);
    }

    localStorage.setItem("cart", JSON.stringify(productsInCart));
  }
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
        <button onClick={addToCart} className="button">
          Add to cart
        </button>
      </div>
    </div>
  );
}

export default Product;
