import {
useEffect,
useState
}
from "react";


import api from "../api/api";


import ProductCard from "../components/ProductCard";


import "../styles/product.css";



export default function Products(){


const [products,setProducts]=useState([]);



useEffect(()=>{

loadProducts();

},[]);




async function loadProducts(){


try{


const res =
await api.get("/products/");


setProducts(
res.data.products
);


}

catch(error){

console.log(error);

}


}





return (


<div>


<div className="page-title">


<h2>

Products

</h2>


<p>

Registered detection products

</p>


</div>





<div className="product-grid">


{

products.map(product=>(


<ProductCard

key={product.id}

product={product}

/>


))


}



</div>



</div>


)

}