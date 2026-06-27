export default function ProductCard({

product

}){


return (

<div className="product-card">


<div className="product-image">


<i className="bi bi-box-seam"></i>


</div>



<div className="product-info">


<h5>

{product.name}

</h5>


<p>

Product ID :

{product.id}

</p>



<div className="badge-active">

Active

</div>


</div>


</div>

)

}