import { useEffect, useState } from "react";
import api from "../api/api";
import ProductCard from "../components/ProductCard";
import "../styles/product.css";

export default function Products() {
  const [products, setProducts] = useState([]);
  const [name, setName] = useState("");
  const [image, setImage] = useState(null);

  useEffect(() => {
    loadProducts();
  }, []);

  async function loadProducts() {
    try {
      const res = await api.get("/products/");
      setProducts(res.data.products);
    } catch (err) {
      console.log(err);
    }
  }

  async function handleUpload(e) {
    e.preventDefault();

    if (!name || !image) {
      alert("Please enter a product name and select an image.");
      return;
    }

    const formData = new FormData();
    formData.append("name", name);
    formData.append("image", image);

    try {
      await api.post("/products/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setName("");
      setImage(null);
      document.getElementById("imageInput").value = "";

      loadProducts();
    } catch (err) {
      console.log(err);
      alert("Upload failed");
    }
  }

  return (
    <div>
      <div className="page-title">
        <h2>Products</h2>
        <p>Register detection products</p>
      </div>

      {/* Upload Form */}
      <form className="upload-form" onSubmit={handleUpload}>
        <input
          type="text"
          placeholder="Product Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          id="imageInput"
          type="file"
          accept=".jpg,.jpeg,.png"
          onChange={(e) => setImage(e.target.files[0])}
        />

        <button type="submit">
          Upload Product
        </button>
      </form>

      <div className="product-grid">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
          />
        ))}
      </div>
    </div>
  );
}