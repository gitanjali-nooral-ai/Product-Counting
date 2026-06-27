import {
useEffect,
useState
}
from "react";


import api from "../api/api";


import "../styles/statistic.css";



export default function Statistics(){


const [data,setData]=useState(null);



useEffect(()=>{


loadStats();


},[]);





async function loadStats(){


try{


const current =
await api.get(
"/statistics/current"
);


const today =
await api.get(
"/statistics/today"
);


const daily =
await api.get(
"/statistics/daily"
);



setData({

current:current.data,

today:today.data,

daily:daily.data

});


}

catch(err){

console.log(err);

}


}





if(!data)

return <h3>Loading...</h3>;





return (

<div>


<div className="page-title">


<h2>

Statistics

</h2>


<p>

Detection analytics

</p>


</div>





<div className="row g-4">


<div className="col-md-4">


<div className="analytics-card">


<h6>

Current Count

</h6>


<h1>

{
data.current.live_count

}

</h1>


</div>


</div>





<div className="col-md-4">


<div className="analytics-card">


<h6>

Today Count

</h6>


<h1>

{
data.today.count

}

</h1>


</div>


</div>





<div className="col-md-4">


<div className="analytics-card">


<h6>

Active Product

</h6>


<h3>

{

data.current.product.name ||

"N/A"

}

</h3>


</div>


</div>



</div>






<div className="chart-box mt-4">


<h5>

Daily Detection Trend

</h5>



{

data.daily.data.map(item=>(


<div

className="chart-row"

key={item.date}

>


<span>

{item.date}

</span>



<div

className="bar"

style={{

width:

`${item.count*5}px`

}}

/>


<strong>

{item.count}

</strong>



</div>


))


}



</div>



</div>

)

}