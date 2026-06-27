import api from "../api/api";

export default function ProductCard({ product }) {
  return (
    <div className="product-card">
      <div className="product-image">
        <img
          src={`${api.defaults.baseURL}/${product.image}`}
          alt={product.name}
        />
      </div>

      <div className="product-info">
        <h5>{product.name}</h5>

        <p>Product ID: {product.id}</p>

        <p>Created: {product.created}</p>

        <div className="badge-active">
          Active
        </div>
      </div>
    </div>
  );
}