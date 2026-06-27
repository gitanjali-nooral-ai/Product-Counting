import {
useEffect,
useState
}
from "react";


import api from "../api/api";


import "../styles/report.css";



export default function Reports(){


const [events,setEvents]=useState([]);



useEffect(()=>{


load();


},[]);




async function load(){


const res =
await api.get(
"/reports/counts"
);


setEvents(
res.data.events
);


}




function download(){


window.open(

"http://localhost:8000/reports/csv"

);


}




return (

<div>


<div className="page-title">


<h2>

Reports

</h2>


<p>

Detection history export

</p>


</div>





<button

className="btn btn-primary mb-4"

onClick={download}

>

<i className="bi bi-download"></i>

Export CSV

</button>





<div className="report-box">


<table className="table table-dark">


<thead>

<tr>

<th>

Product

</th>


<th>

Track ID

</th>


<th>

Time

</th>


</tr>

</thead>



<tbody>


{

events.map(e=>(


<tr key={e.event_id}>


<td>

{e.product_name}

</td>


<td>

#{e.track_id}

</td>


<td>

{e.counted_at}

</td>


</tr>


))


}


</tbody>


</table>


</div>


</div>


)

}